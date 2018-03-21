"""Provide code in support of extract-transform-load type operations used across many data sources."""

import pendulum as pen
import pandas as pd

from . import loaders
from . import recode
from . import validate


__all__ = [
    "recode",
    "validate",
    "loaders",
]


def time_string_to_time(time_string):
    """Return datetime.time instance from a time string."""
    try:
        return pen.parse(time_string).time()
    except TypeError:
        if pd.isnull(time_string):
            return pd.NaT