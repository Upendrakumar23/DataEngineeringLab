"""
Test duplicate validator with duplicate records.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.duplicate_validator import validate_duplicates


def test_duplicate_validator_negative():
    df = extract_csv(
        DATASET_DIR / "test" / "employees_duplicate.csv"
    )

    try:
        validate_duplicates(df)
    except ValueError:
        print("✅ Duplicate validation test passed.")
    else:
        raise AssertionError("Expected ValueError was not raised.")


if __name__ == "__main__":
    test_duplicate_validator_negative()