"""
Test null validator with invalid data.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.null_validator import validate_nulls


def test_null_validator_negative():
    df = extract_csv(DATASET_DIR / "test" / "employees_null.csv")

    try:
        validate_nulls(df)
    except ValueError:
        print("✅ Null validation test passed.")
    else:
        raise AssertionError("Expected ValueError was not raised.")


if __name__ == "__main__":
    test_null_validator_negative()