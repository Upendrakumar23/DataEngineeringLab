import pandas as pd


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform employee data.
    """

    # Remove leading/trailing spaces
    df["name"] = df["name"].str.strip()
    df["department"] = df["department"].str.strip()

    # Standardize names
    df["name"] = df["name"].str.title()

    # Standardize department names
    df["department"] = df["department"].str.strip().str.upper()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    print("\nData After Transformation")
    print("-" * 40)
    print(df.head())

    return df