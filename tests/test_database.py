"""
Test database connection.
"""

from src.database import get_connection


def test_connection():
    conn = None

    try:
        conn = get_connection()

        print("✅ Database connection successful.")

    except Exception as e:
        print(f"❌ Database connection failed: {e}")

    finally:
        if conn:
            conn.close()
            print("✅ Database connection closed.")


if __name__ == "__main__":
    test_connection()
