#!/usr/bin/env python
"""Provide code to organize the validation and recoding of redcap db dumps."""
import pandas as pd

from table_enforcer import Column, Enforcer
from db_tools import etl


def load_data_dict(path):
    """Load a redcap data_dict file and transpose it so that column names represent actual column names."""
    return pd.read_csv(path, dtype=str).set_index("Variable / Field Name").T


def load_registry(data_path, ddict_path, validate=True):
    """Load recode and validate a registry data dump."""

    redcap_event_name = Column(
        name="redcap_event_name",
        dtype=(str, type(None)),
        unique=False,
        validators=[etl.redcap.validate.valid_registry_event_name],
        recoders=[etl.common.recode.nan_to_none],
    )

    dd = load_data_dict(path=ddict_path)
    data = pd.read_csv(data_path, dtype=str)

    col_info_objs = etl.redcap.digest_ddict(dd)
    enforcer = Enforcer([redcap_event_name] + [col.column_object for col in col_info_objs.values()])

    return enforcer.recode(data, validate=validate)
