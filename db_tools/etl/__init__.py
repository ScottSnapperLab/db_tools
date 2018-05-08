"""Provide top level code in support of extract-transform-load type operations."""
import pandas as pd
import numpy as np

from box import Box

import pendulum as pen


def get_failed_values(df, col):
    failed = col.validate(col.recode(df), failed_only=True)
    return df[col.name].iloc[failed.index]


def is_subset(x, ref_set):
    """Return ``True`` if ``x`` is a subset of ``ref_set``."""
    if not isinstance(ref_set, set):
        ref_set = set(ref_set)

    if isinstance(x, (list, tuple, set)):
        set_x = set(x)
    else:
        set_x = set([x])

    return set_x.issubset(ref_set)


def time_string_to_time(time_string):
    """Return datetime.time instance from a time string."""
    try:
        return pen.parse(time_string).time()
    except TypeError:
        if pd.isnull(time_string):
            return pd.NaT


def which_columns(df, test_func):
    """Return a list of column names that evaluate to True when passed to test_func."""
    return list(df.columns[df.apply(test_func)])


def are_lists(series):
    """Return True if any items in series contain a list."""

    def test(value):
        """Return True if value is a list."""
        return isinstance(value, list)

    return series.apply(test).any()


# def lists_columns(df):
#     """Return a list of column names whose values are lists."""
#     return list(df.columns[df.apply(column_is_list)])


def are_empty(series):
    """Return True if all items in series evaluate to empty."""

    def test(value):
        """Return True if value is considered empty."""
        empty_values = [list(), dict(), tuple(), str(), np.nan, pd.NaT, None]
        if value in empty_values:
            return True
        else:
            return False

    return series.apply(test).all()


# def empty_columns(df):
#     """Return a list of column names that are completely empty."""
#     return list(df.columns[df.apply(column_is_empty)])


def split_table_by_column_value(df, column_name, drop_empty_columns=False):
    """Return a dict of DataFrames grouped by the values in column_name."""
    tables = {}

    for column_value in df[column_name].unique():
        tables[column_value] = df[df[column_name] == column_value].copy()

    if drop_empty_columns:
        for table in tables:
            drop_these = which_columns(tables[table], test_func=are_empty)
            tables[table] = tables[table].drop(columns=drop_these)

    return Box(tables)