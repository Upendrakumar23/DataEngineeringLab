"""
Test blank validator with invalid data.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.blank_validator import validate_blanks


def test_blank_validator_negative():
    df = extract_csv(
        DATASET_DIR / "test" / "employees_blank.csv"
    )

    try:
        validate_blanks(df)
    except ValueError:
        print("✅ Blank validation test passed.")
    else:
        raise AssertionError("Expected ValueError was not raised.")


if __name__ == "__main__":
    test_blank_validator_negative()