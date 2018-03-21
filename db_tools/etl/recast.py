"""Provide code to recast values from one type (usually str) to another."""
import pendulum as pen


# Recasting functions
def as_time(value):
    """Return value recast as time."""
    return pen.parse(value).time()


def as_string(value):
    """Return value recast as string."""
    return str(value)


def as_date(value):
    """Return value recast as date."""
    return pen.parse(value).date()


def as_integer(value):
    """Return value recast as integer."""
    return int(value)


def as_float(value):
    """Return value recast as float."""
    return float(value)