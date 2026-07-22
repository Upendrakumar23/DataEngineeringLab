"""
Test duplicate validator.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.duplicate_validator import validate_duplicates


def test_duplicate_validator():
    df = extract_csv(DATASET_DIR / "employees.csv")

    validate_duplicates(df)

    print("✅ Duplicate validator test passed.")


if __name__ == "__main__":
    test_duplicate_validator()