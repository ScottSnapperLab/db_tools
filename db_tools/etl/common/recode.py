#!/usr/bin/env python
"""Provide code to recode columns common to many sources."""

# Imports
import pandas as pd

from db_tools.etl import time_string_to_time


def nan_to_none(series):
    """Return series after converting NaN-type objects to ``None``."""
    return series.where(pd.notna(series), None)


def to_str(series):
    """Return series with data re-cast as strings."""
    return series.astype(str)


def to_one_or_zero(series):
    """Recode series values to either [0,1,None]."""
    valid_vals = set([0, 1])
    series = series.fillna(0).astype(int)

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

    return series.apply(time_string_to_time)