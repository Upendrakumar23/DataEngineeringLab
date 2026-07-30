"""
Test master validator.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.validator import validate_data


def test_validator():
    file_path = DATASET_DIR / "employees.csv"

    df = extract_csv(file_path)

    validate_data(df)

    print("✅ All validations passed.")


if __name__ == "__main__":
    test_validator()
