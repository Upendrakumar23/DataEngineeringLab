"""
Test blank validator.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.blank_validator import validate_blanks


def test_blank_validator():
    df = extract_csv(DATASET_DIR / "employees.csv")

    validate_blanks(df)

    print("✅ Blank validator test passed.")


if __name__ == "__main__":
    test_blank_validator()