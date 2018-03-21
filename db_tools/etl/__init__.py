"""Provide top level code in support of extract-transform-load type operations."""
import pandas as pd

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



