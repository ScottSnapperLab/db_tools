"""Provide code to ETL redcap data dumps."""
import typing as typ
from collections import OrderedDict
import datetime as dt
import pendulum as pen

from logzero import logger as log

import pandas as pd
import numpy as np

from box import Box

from table_enforcer import Column, CompoundColumn, BaseColumn

import db_tools.etl.common as common
from db_tools.etl import is_subset

from dataclasses import dataclass

from . import loaders
from . import recode
from . import validate


def digest_ddict(ddict):
    """Return OrderedDict of RedCapColumnInfo objects.

    Args:
        ddict (pd.DataFrame): Loaded/recoded redcap data dictionary.
    """
    ddict = ddict.T[ddict.T["Field Type"] != 'descriptive'].T

    redcap_info_objs = OrderedDict()
    for info_obj in [RedCapColumnInfo(ddict[col_name]) for col_name in ddict.columns]:
        redcap_info_objs[info_obj.name] = info_obj
    return redcap_info_objs


def ccs_labels_to_mapper(series):
    """Convert the "Choices, Calculations, OR Slider Labels" string into dict."""

    def clean_key(key):
        key = key.replace('-', '_').lower()

        return key

    def clean_value(value):
        value = value.replace("<br><sup>", "SPLIT_HERE")
        value = value.split("SPLIT_HERE")[0]
        value = value.strip()

        return value

    try:
        labels = series["Choices, Calculations, OR Slider Labels"]
        choices = [i.strip() for i in labels.split("|")]
        split_choices = [c.split(',', maxsplit=1) for c in choices]
        stripped_split_choices = [[i.strip() for i in l] for l in split_choices]
        return {clean_key(key): clean_value(val) for key, val in stripped_split_choices}
    except (AttributeError, ValueError):
        return None


def checkbox_column_factory(column_info):
    """Return a fully populated compound column object based on the defintion in the ddict.

    Args:
        column_info (RedCapColumnInfo): A RedCapColumnInfo object.
    """

    # ### Transformation function
    def transformation(input_names, output_name):
        def func(df):
            cols = Box()
            cols[output_name] = df.apply(lambda row: tuple([row[col_name] for col_name in input_names]), axis=1)

            new_columns = pd.DataFrame(cols)
            return new_columns

        return func

    # ### Function to generate input columns
    def input_column(col_n, label):
        """Return initiated Column obj."""

        def valid_values(series):
            valid = [None, label]
            return series.apply(is_subset, ref_set=valid)

        def translate_column(series):
            def rcode(x):
                mapping = {0: None, 1: label}
                return mapping[x]

            return series.apply(rcode)

        return Column(
            name=f"{column_info.name}___{col_n}",
            dtype=(str, type(None)),
            unique=False,
            validators=[
                valid_values,
            ],
            recoders=[
                common.recode.to_one_or_zero,
                translate_column,
            ]
        )

    # ### Function to generate output columns
    def output_column(name, labels):
        """Return initiated Column obj."""

        def valid_values(series):
            valid = labels
            return series.apply(is_subset, ref_set=valid)

        return Column(
            name=name,
            dtype=list,
            unique=False,
            validators=[
                valid_values,
            ],
            recoders=[
                common.recode.setify_drop_nones,
            ],
        )

    label_mapper = {}
    label_mapper.update(column_info.options_labels)

    # Make input columns
    input_cols = []
    for col_n, label in label_mapper.items():
        input_cols.append(input_column(col_n, label))

    # Make output column
    output_cols = [output_column(name=column_info.name, labels=label_mapper.values())]

    # Make the CompoundColumn
    return CompoundColumn(
        input_columns=input_cols,
        output_columns=output_cols,
        column_transform=transformation(
            input_names=[col.name for col in input_cols],
            output_name=column_info.name,
        )
    )


def radio_dropdown_column_factory(column_info):
    """Return a fully initiated column object based on the defintion in the ddict.

    Args:
        column_info (RedCapColumnInfo): A RedCapColumnInfo object.
    """

    # ### Function to generate columns
    def build_column(name, labels):
        """Return initiated Column obj."""

        def valid_values(series):
            valid = list(labels) + [None]
            return series.apply(is_subset, ref_set=valid)

        def translate_column(series):
            def rcode(x):
                return label_mapper[x]

            return series.apply(rcode)

        return Column(
            name=name,
            dtype=(str, type(None)),
            unique=False,
            validators=[
                valid_values,
            ],
            recoders=[
                translate_column,
            ],
        )

    label_mapper = {}
    label_mapper.update(column_info.options_labels)
    label_mapper.update({np.nan: None})

    return build_column(
        name=column_info.name,
        labels=label_mapper.values(),
    )


def yesno_column_factory(column_info):
    """Return a fully initiated "yesno" type column object.

    Args:
        column_info (RedCapColumnInfo): A RedCapColumnInfo object.
    """

    def valid_values(series):
        valid = list(value_mapper.values())
        return series.apply(is_subset, ref_set=valid)

    def translate_column(series):
        def rcode(x):
            return value_mapper[x]

        return series.apply(rcode)

    value_mapper = {
        "0": "NO",
        "1": "YES",
        np.nan: None,
    }

    return Column(
        name=column_info.name,
        dtype=(str, type(None)),
        unique=False,
        validators=[
            valid_values,
        ],
        recoders=[
            translate_column,
        ],
    )


#TODO: Add custom range validators to column_object if the data is provided in the data_dict
@dataclass(init=False)
class RedCapColumnInfo(object):
    """FILL THIS IN."""

    name: str = None
    form_name: str = None
    section_header: str = None
    field_type: str = None
    field_label: str = None
    options_labels: dict = None
    validation_kind: str = None
    validation_min: typ.Any = None
    validation_max: typ.Any = None
    column_object: BaseColumn = None

    def __init__(self, ddict_col):
        """Initiate the TextTypeInfo object."""
        self.name = ddict_col.name
        self.form_name = ddict_col["Form Name"]
        self.section_header = ddict_col["Section Header"]
        self.field_type = ddict_col["Field Type"]
        self.field_label = ddict_col["Field Label"]

        self.options_labels = ccs_labels_to_mapper(ddict_col)

        self.validation_kind = ddict_col["Text Validation Type OR Show Slider Number"]
        self.validation_min = ddict_col["Text Validation Min"]
        self.validation_max = ddict_col["Text Validation Max"]

        self._cast_validation_limits()
        self._spawn_column_object()

    def _cast_validation_limits(self):
        """Recast self.validation_min/validation_max based on cast_map."""

        def build_robust_casting_func(func):
            """Return function to recast using ``func`` after adding error-catching logic."""

            def robust_casting_func(value):
                """Recast ``value`` with ``func`` unless ``func`` fails: then use fall-back."""
                try:
                    return func(value)
                except (ValueError, TypeError):
                    log.warn(
                        f"`{value}` failed to be recast with function `{func.__name__}`, Falling back to `str(value)`."
                    )
                    return str(value)

            return robust_casting_func

        cast_map = {
            "time": build_robust_casting_func(lambda txt: pen.parse(txt).time()),
            "alpha_only": build_robust_casting_func(str),
            "date_ymd": build_robust_casting_func(lambda txt: pen.parse(txt).date()),
            "date_mdy": build_robust_casting_func(lambda txt: pen.parse(txt).date()),
            "date_dmy": build_robust_casting_func(lambda txt: pen.parse(txt).date()),
            "integer": build_robust_casting_func(int),
            "number": build_robust_casting_func(float),
            "number_1dp": build_robust_casting_func(float),
            "number_4dp": build_robust_casting_func(float),
            np.nan: build_robust_casting_func(str),
        }

        recast = cast_map[self.validation_kind]
        self.validation_min = recast(self.validation_min)
        self.validation_max = recast(self.validation_max)

    def _spawn_column_object(self):
        """Create and store the Column Object."""
        fieldtype_to_factory = {
            "radio": radio_dropdown_column_factory,
            "text": text_column_factory,
            "checkbox": checkbox_column_factory,
            "dropdown": radio_dropdown_column_factory,
            "yesno": yesno_column_factory,
            "calc": calc_column_factory,
        }

        self.column_object = fieldtype_to_factory[self.field_type](self)


def text_column_factory(column_info):
    """Return a fully initiated column object based on the defintion in the ddict.

    Args:
        column_info (RedCapColumnInfo): A RedCapColumnInfo object.
    """

    validators = {
        'time': [common.validate.istime],
        'alpha_only': [common.validate.isalpha],
        'date_ymd': [validate.date_format],
        'date_mdy': [validate.date_format],
        'date_dmy': [validate.date_format],
        'integer': [],
        'number': [],
        'number_1dp': [],
        'number_4dp': [],
        np.nan: [],
    }

    recoders = {
        'time': [common.recode.to_hour_minute],
        'alpha_only': [common.recode.nan_to_none],
        'date_ymd': [common.recode.nan_to_none],
        'date_mdy': [common.recode.nan_to_none],
        'date_dmy': [common.recode.nan_to_none],
        'integer': [common.recode.nan_to_none],
        'number': [common.recode.nan_to_none],
        'number_1dp': [common.recode.nan_to_none],
        'number_4dp': [common.recode.nan_to_none],
        np.nan: [common.recode.nan_to_none],
    }

    dtype = {
        'time': (dt.time, type(pd.NaT)),
        'alpha_only': (str, type(None)),
        'date_ymd': (str, type(None)),
        'date_mdy': (str, type(None)),
        'date_dmy': (str, type(None)),
        'integer': (int, type(None)),
        'number': (float, type(None)),
        'number_1dp': (float, type(None)),
        'number_4dp': (float, type(None)),
        np.nan: (str, type(None)),
    }

    return Column(
        name=column_info.name,
        dtype=dtype[column_info.validation_kind],
        unique=False,
        validators=validators[column_info.validation_kind],
        recoders=recoders[column_info.validation_kind],
    )


def calc_column_factory(column_info):
    """Return a fully initiated column object based on the defintion in the ddict.

    Args:
        column_info (RedCapColumnInfo): A RedCapColumnInfo object.
    """
    return Column(
        name=column_info.name,
        dtype=(float, type(None)),
        unique=False,
        validators=[validate.valid_float],
        recoders=[common.recode.nan_to_none],
    )