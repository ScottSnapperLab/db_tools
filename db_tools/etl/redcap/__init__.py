"""Provide code to ETL redcap data dumps."""
import pandas as pd
import numpy as np

from box import Box

from table_enforcer import Column, CompoundColumn

from db_tools.etl.common.recode import to_one_or_zero, setify_drop_nones
from db_tools.etl import is_subset

from . import loaders
from . import recode
from . import validate


def load_data_dict(path):
    """Load a redcap data_dict file and transpose it so that column names represent actual column names."""
    return pd.read_csv(path).set_index("Variable / Field Name").T


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


def checkbox_column_factory(ddict, ddict_col):
    """Return a fully populated compound column object based on the defintion in the ddict.

    Args:
        ddict (DataFrame): A redcap data-dict loaded with ``load_data_dict``.
        ddict_col (str): The name of the checkbox-type column to process.
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
            name=f"{ddict_col}___{col_n}",
            dtype=(str, type(None)),
            unique=False,
            validators=[valid_values],
            recoders=[to_one_or_zero, translate_column]
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
            validators=[valid_values],
            recoders=[setify_drop_nones],
        )

    label_mapper = ccs_labels_to_mapper(ddict[ddict_col])

    # Make input columns
    input_cols = []
    for col_n, label in label_mapper.items():
        input_cols.append(input_column(col_n, label))

    # Make output column
    output_cols = [output_column(name=ddict_col, labels=label_mapper.values())]

    # Make the CompoundColumn
    return CompoundColumn(
        input_columns=input_cols,
        output_columns=output_cols,
        column_transform=transformation(input_names=[col.name for col in input_cols], output_name=ddict_col)
    )


def radio_dropdown_column_factory(ddict, ddict_col):
    """Return a fully initiated column object based on the defintion in the ddict.

    Args:
        ddict (DataFrame): A redcap data-dict loaded with ``load_data_dict``.
        ddict_col (str): The name of the radio-type column to process.
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
            validators=[valid_values],
            recoders=[translate_column],
        )

    label_mapper = ccs_labels_to_mapper(ddict[ddict_col])
    label_mapper.update({np.nan: None})

    return build_column(name=ddict_col, labels=label_mapper.values())


def yesno_column_factory(ddict_col):
    """Return a fully initiated "yesno" type column object.

    Args:
        ddict_col (str): The name of the yesno-type column to process.
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
        np.nan: np.nan,
    }

    return Column(
        name=ddict_col,
        dtype=(str, type(None)),
        unique=False,
        validators=[valid_values],
        recoders=[translate_column],
    )