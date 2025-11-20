# test_clean_data.py
import pandas as pd
import pytest
from data import clean_data

def test_remove_duplicates():
    data = {
        "name": ["A", "A", "B"],
        "age": [20, 20, 30]
    }
    df = pd.DataFrame(data)

    cleaned = clean_data(df)

    # Expect only unique rows remain: rows for "A" (one) and "B"
    assert len(cleaned) == 2
    # No duplicated rows
    assert cleaned.duplicated().sum() == 0

def test_remove_nulls():
    data = {
        "name": ["A", None, "B"],
        "age": [20, 25, None]
    }
    df = pd.DataFrame(data)

    cleaned = clean_data(df)

    # No nulls anywhere
    assert cleaned.isnull().sum().sum() == 0
    # Only the first row ("A",20) has no nulls, so expect 1 row
    assert len(cleaned) == 1
    # Check the remaining row has expected values
    assert cleaned.iloc[0]["name"] == "A"
    assert cleaned.iloc[0]["age"] == 20

def test_rows_decrease_after_cleaning():
    data = {
        "name": ["A", "A", None],
        "age": [20, 20, 30]
    }
    df = pd.DataFrame(data)

    cleaned = clean_data(df)

    assert len(cleaned) < len(df)



# how to run a single test function with pytest -q test_clean_data.py::test_remove_nulls.
