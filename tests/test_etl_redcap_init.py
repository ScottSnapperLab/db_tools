"""Provide code to ETL redcap data dumps."""
from pathlib import Path
import pytest

from table_enforcer import Column, CompoundColumn
import db_tools.errors as e
from db_tools.etl import redcap

from .helpers import checking_jsons as json


@pytest.fixture
def dd_csv_path():
    """Provide path to test data_dict.csv."""
    return Path("tests/files/data_dict.csv")


@pytest.fixture
def dd_json_path():
    """Provide path to test data_dict.csv."""
    return Path("tests/files/data_dict.json")


@pytest.fixture
def dd_df(dd_csv_path):
    """Provide loaded data_dict as dataframe."""
    return redcap.load_data_dict(dd_csv_path)


###################################


def test_load_data_dict(dd_csv_path, dd_json_path):
    """Ensure that the loaded data_dict looks as it should."""
    dd = redcap.load_data_dict(dd_csv_path).reset_index()

    assert json.check_json_string(df=dd, json_str=dd_json_path)


def test_ccs_labels_to_mapper(dd_df):
    """Ensure that ccs_labels_to_mapper produces expected results."""
    value_mapper_ref = {
        '1': 'CHIMP (X06-10-0470)',
        '2': 'Oral microbiome (X09-10-0535)',
        '3': 'Grand Lee Genetics (04-12-173R)',
        '4': 'Bousvaros Immunoregulation (98-12-206R)',
        '5': 'Biorepository (P00000529)',
    }

    value_mapper = redcap.ccs_labels_to_mapper(dd_df.prior_protocol_number)

    assert value_mapper_ref == value_mapper


def test_checkbox_column_factory(dd_df):
    """Ensure that checkbox_column_factory produces expected results."""
    checkbox = redcap.checkbox_column_factory(ddict=dd_df, ddict_col="sampletype")

    # is correct type
    assert isinstance(checkbox, CompoundColumn)

    # input_columns/output_columns are correct [name]
    assert [col.name for col in checkbox.input_columns] == [
        'sampletype___1',
        'sampletype___3',
        'sampletype___4',
        'sampletype___5',
        'sampletype___6',
        'sampletype___7',
        'sampletype___2',
        'sampletype___8',
    ]
    assert [col.name for col in checkbox.output_columns] == ['sampletype']

    # input_columns/output_columns are correct [dtype]
    assert set([col.dtype for col in checkbox.input_columns]) == set([(str, type(None))])
    assert [col.dtype for col in checkbox.output_columns] == [list]

    # input_columns/output_columns are correct [unique]
    assert not any([col.unique for col in checkbox.input_columns])  # all should be false
    assert [col.unique for col in checkbox.output_columns] == [False]


def test_radio_dropdown_column_factory(dd_df):
    """Ensure that radio_dropdown_column_factory produces expected results."""
    dropdown = redcap.radio_dropdown_column_factory(ddict=dd_df, ddict_col="meddraae1")
    radio = redcap.radio_dropdown_column_factory(ddict=dd_df, ddict_col="visitcategory")

    # is correct type
    assert isinstance(dropdown, Column)
    assert isinstance(radio, Column)

    # columns are correct [name]
    assert dropdown.name == "meddraae1"
    assert radio.name == "visitcategory"

    # columns are correct [dtype]
    assert dropdown.dtype == (str, type(None))
    assert radio.dtype == (str, type(None))

    # columns are correct [unique] -> should be False
    assert not dropdown.unique
    assert not radio.unique


def test_yesno_column_factory(dd_df):
    """Ensure that yesno_column_factory produces expected results."""
    yesno = redcap.yesno_column_factory(ddict_col="consent")
    assert yesno.dtype == (str, type(None))
    assert yesno.name == "consent"
    assert not yesno.unique  # should be False
