"""
Test file validator with a missing file.
"""

from pathlib import Path

from src.validations.file_validator import validate_file


def test_missing_file():
    try:
        validate_file(Path("datasets/not_exists.csv"))
    except FileNotFoundError:
        print("✅ Missing file validation passed.")
    else:
        raise AssertionError("Expected FileNotFoundError was not raised.")


if __name__ == "__main__":
    test_missing_file()