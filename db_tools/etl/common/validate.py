#!/usr/bin/env python
"""Provide code to validate columns common to many sources."""

import datetime as dt
import pandas as pd


def isalpha(series):
    """Enforce that values contain only letters."""
    return series.astype(str).str.isalpha()


def istime(series):
    """Enforce that the values are time-like"""

    def test(value):
        valid_types = (
            dt.time,
            type(pd.NaT),
        )
        return isinstance(value, valid_types)

    return series.apply(test)
