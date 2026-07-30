"""
Unit tests for src.main
"""

from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.main import main


@patch("src.main.logger")
@patch("src.main.load_data")
@patch("src.main.transform_data")
@patch("src.main.validate_data")
@patch("src.main.extract_csv")
@patch("src.main.validate_file")
def test_main_success(
    mock_validate_file,
    mock_extract_csv,
    mock_validate_data,
    mock_transform_data,
    mock_load_data,
    mock_logger,
):
    """
    Verify that the ETL pipeline executes successfully.
    """

    sample_df = pd.DataFrame(
        {
            "employee_code": ["EMP001"],
            "name": ["John"],
            "department": ["IT"],
            "salary": [50000],
        }
    )

    # Arrange
    mock_extract_csv.return_value = sample_df
    mock_transform_data.return_value = sample_df
    mock_load_data.return_value = 1

    # Act
    main()

    # Assert
    mock_validate_file.assert_called_once()

    mock_extract_csv.assert_called_once()

    mock_validate_data.assert_called_once_with(sample_df)

    mock_transform_data.assert_called_once_with(sample_df)

    mock_load_data.assert_called_once_with(sample_df)

    mock_logger.info.assert_called()


@patch("src.main.logger")
@patch("src.main.validate_file")
def test_main_validation_failure(
    mock_validate_file,
    mock_logger,
):
    """
    Verify that exceptions are logged and re-raised.
    """

    mock_validate_file.side_effect = FileNotFoundError(
        "employees.csv not found"
    )

    with pytest.raises(FileNotFoundError):
        main()

    mock_logger.exception.assert_called_once_with(
        "ETL Pipeline failed."
    )
