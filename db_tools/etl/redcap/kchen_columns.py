#!/usr/bin/env python
"""Columns created by Kelly Chen that have been pushed."""

from table_enforcer import Column

from db_tools.etl import common, redcap

import pandas as pd


mrn_reg = Column(
            name='mrn',
            dtype=(str, type(None)),
            unique=True,
            validators=[integer, seven_chs],
            recoders=[rcdcmn.nan_to_none, digits_only, pad_mrn])