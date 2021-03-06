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


def integer(series):
    '''test that not None-type data items are only integers'''
    return series.astype(str).str.isnumeric()

def seven_chs(series):
    '''test that not None-type data items are seven characters long'''
    return series.str.len() == 7

def valid_registry_event_name(series):
    valid = [
        'registration_visit_arm_1',
        'baseline_visit_arm_1',
        'followup_visit_1_arm_1',
        'followup_visit_2_arm_1',
        'followup_visit_3_arm_1',
        'followup_visit_4_arm_1',
        'surgeries_arm_1',
        'hospitalizations_arm_1',
    ]

    return series.isin(valid)