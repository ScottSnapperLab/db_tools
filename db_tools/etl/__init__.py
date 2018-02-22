"""Provide top level code in support of extract-transform-load type operations."""


def is_subset(x, ref_set):
    """Return ``True`` if ``x`` is a subset of ``ref_set``."""
    if not isinstance(ref_set, set):
        ref_set = set(ref_set)

    if isinstance(x, (list, tuple, set)):
        set_x = set(x)
    else:
        set_x = set([x])

    return set_x.issubset(ref_set)
