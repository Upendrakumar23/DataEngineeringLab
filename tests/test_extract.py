"""
Test CSV extraction.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv


def test_extract():
    df = extract_csv(DATASET_DIR / "employees.csv")

    print("✅ CSV extracted successfully.\n")
    print(df.head())


if __name__ == "__main__":
    test_extract()
