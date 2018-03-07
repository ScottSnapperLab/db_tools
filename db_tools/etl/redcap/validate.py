#!/usr/bin/env python
"""Provide code to validate columns from redcap db dumps."""

import datetime


def date_format(series):
    def validate_date(date_text):

        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            #             raise
            if date_text == "None":
                return True
            else:
                return False

    return series.astype(str).apply(validate_date)


def valid_float(series):
    def is_float(s):
        try:
            float(s)
            return True
        except ValueError:
            if s == "None":
                return True
            else:
                return False

    return series.astype(str).apply(is_float)
