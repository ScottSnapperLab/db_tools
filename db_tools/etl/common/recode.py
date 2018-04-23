#!/usr/bin/env python
"""Provide code to recode columns common to many sources."""

# Imports
import pandas as pd
import numpy as np

import db_tools.etl as etl


def nan_to_none(series):
    """Return series after converting NaN-type objects to ``None``."""
    return series.where(pd.notna(series), None)


def to_str(series):
    """Return series with data re-cast as strings."""
    return series.astype(str)


def to_int_or_nan(series):
    """Return series with values converted to int (if possible) allowing for NaNs."""

    def recode(value):
        try:
            return etl.recast.as_integer(value)
        except ValueError as err:
            if err.args[0] == "cannot convert float NaN to integer":
                return np.nan
            elif err.args[0] == "invalid literal for int() with base 10: 'nan'":
                return np.nan
            else:
                raise

    return series.apply(recode)


def to_one_or_zero(series):
    """Recode series values to either [0,1,np.nan]."""
    valid_vals = set([0, 1, np.nan])
    # series = series.fillna(0).astype(int)

    obs_vals = set(series.unique())

    if not obs_vals.issubset(valid_vals):
        invalid_vals = obs_vals - valid_vals
        raise ValueError(f"Encountered non-valid values: {invalid_vals}.")

    return series


def setify_drop_nones(series):
    """Convert to sets and drop ``None`` values."""

    def drop_nones(x):
        x.discard(None)
        return x

    return series.apply(lambda x: set(x)).apply(drop_nones).apply(list)


def to_hour_minute(series):
    """Convert a string to a time object."""

    return series.apply(etl.time_string_to_time)