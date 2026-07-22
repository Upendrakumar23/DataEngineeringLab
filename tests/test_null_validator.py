"""
Test null validator.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.null_validator import validate_nulls


def test_null_validator():
    df = extract_csv(DATASET_DIR / "employees.csv")

    validate_nulls(df)

    print("✅ Null validator test passed.")


if __name__ == "__main__":
    test_null_validator()