import pandas as pd


def extract(csv_path):
    """
    Read employee data from a CSV file.
    """
    df = pd.read_csv(csv_path)

    print("\nData Loaded Successfully")
    print("-" * 40)
    print(df.head())

    return df