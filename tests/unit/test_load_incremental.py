"""
Unit tests for load_incremental.py
"""

from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
from psycopg import DatabaseError

from src.load_incremental import load_data


@patch("src.load_incremental.get_connection")
def test_load_success(mock_get_connection):
    """
    Verify successful batch loading into the database.
    """

    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    df = pd.DataFrame(
        {
            "employee_code": ["EMP001", "EMP002"],
            "name": ["Alice", "Bob"],
            "department": ["HR", "IT"],
            "salary": [50000, 60000],
        }
    )

    rows = load_data(df, batch_size=1000)

    assert rows == 2

    mock_cursor.executemany.assert_called_once()
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()


@patch("src.load_incremental.get_connection")
def test_load_database_error(mock_get_connection):
    """
    Verify rollback when a database error occurs.
    """

    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    mock_cursor.executemany.side_effect = DatabaseError("Insert Failed")

    df = pd.DataFrame(
        {
            "employee_code": ["EMP001"],
            "name": ["Alice"],
            "department": ["HR"],
            "salary": [50000],
        }
    )

    with pytest.raises(DatabaseError):
        load_data(df)

    mock_conn.rollback.assert_called_once()
    mock_conn.close.assert_called_once()


@patch("src.load_incremental.get_connection")
def test_load_unexpected_error(mock_get_connection):
    """
    Verify rollback when an unexpected exception occurs.
    """

    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    mock_cursor.executemany.side_effect = RuntimeError("Unexpected Failure")

    df = pd.DataFrame(
        {
            "employee_code": ["EMP001"],
            "name": ["Alice"],
            "department": ["HR"],
            "salary": [50000],
        }
    )

    with pytest.raises(RuntimeError):
        load_data(df)

    mock_conn.rollback.assert_called_once()
    mock_conn.close.assert_called_once()
