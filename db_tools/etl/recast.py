"""Provide code to recast values from one type (usually str) to another."""
import pandas as pd
import pendulum as pen


# Recasting functions
def as_time(value):
    """Return value recast as time."""
    try:
        return pen.parse(value).time()
    except TypeError:
        return pd.NaT


def as_string(value):
    """Return value recast as string."""
    return str(value)


def as_date(value):
    """Return value recast as date."""
    try:
        return pen.parse(value).date()
    except TypeError:
        return pd.NaT


def as_integer(value):
    """Return value recast as integer."""
    return int(value)


def as_float(value):
    """Return value recast as float."""
    return float(value)