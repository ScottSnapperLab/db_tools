#!/usr/bin/env python
"""Provide code to organize the validation and recoding of redcap db dumps."""
import pandas as pd


def load_data_dict(path):
    """Load a redcap data_dict file and transpose it so that column names represent actual column names."""
    return pd.read_csv(path, dtype=str).set_index("Variable / Field Name").T