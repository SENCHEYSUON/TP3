import pandas as pd

def normalize_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    if column not in df.columns:
        raise KeyError(f"Column '{column}' does not exist in DataFrame")

    # Avoid modifying original DataFrame
    result = df.copy()

    col_min = result[column].min()
    col_max = result[column].max()

    # Avoid division by zero (all values same)
    if col_min == col_max:
        result[column] = 0.0
        return result

    result[column] = (result[column] - col_min) / (col_max - col_min)
    return result
