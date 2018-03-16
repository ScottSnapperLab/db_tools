#!/usr/bin/env python
"""Provide code to recode columns from redcap db dumps."""

def digits_only(series):
    '''delete all non-numeric characters'''
    return pd.Series(series).str.replace(r'[^0-9]','')

def pad_mrn(series):
    '''pad left with zeros if less than 7 characters'''
    return pd.Series(series).str.zfill(7)

