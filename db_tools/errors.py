#!/usr/bin/env python
"""Provide error classes."""

# Imports
from db_tools import __author__, __email__


class DBToolsError(Exception):
    """Base error class."""


class NotImplementedYet(NotImplementedError, DBToolsError):
    """Raise when a section of code that has been left for another time is asked to execute."""

    def __init__(self, msg=None):
        """Set up the Exception."""
        if msg is None:
            msg = f"That bonehead {__author__} should really hear your rage about this disgraceful oversight! Feel free to tell them at {__email__}"
            self.args = (msg, *self.args)
