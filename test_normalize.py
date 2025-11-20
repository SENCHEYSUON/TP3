import pandas as pd
import pytest
from TP3.normalization import normalize_column   # function not created yet (TDD!)

def test_normalized_values_between_0_and_1():
    df = pd.DataFrame({"score": [10, 20, 30]})

    result = normalize_column(df, "score")

    # All values must be between 0 and 1
    assert result["score"].min() >= 0
    assert result["score"].max() <= 1


def test_column_length_unchanged():
    df = pd.DataFrame({"value": [5, 10, 15, 20]})

    result = normalize_column(df, "value")

    assert len(result) == len(df)


def test_invalid_column_name_raises_keyerror():
    df = pd.DataFrame({"age": [1, 2, 3]})

    with pytest.raises(KeyError):
        normalize_column(df, "salary")  # salary does not exist
