from database import get_connection


def load(df):
    """
    Load employee data into PostgreSQL.
    """

    conn = None
    cursor = None

    try:
        # Create database connection
        conn = get_connection()
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO employees (name, department, salary)
            VALUES (%s, %s, %s)
        """

        # Insert each row
        for _, row in df.iterrows():
            cursor.execute(
                insert_query,
                (
                    row["name"],
                    row["department"],
                    row["salary"],
                ),
            )

        # Commit transaction
        conn.commit()

        print(f"\nSuccessfully loaded {len(df)} records into employees table.")

    except Exception as e:
        if conn:
            conn.rollback()

        print(f"\nError while loading data: {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

        print("Database connection closed.")