# Day 5 – Building the First ETL Pipeline

## Objective

Build a complete ETL (Extract, Transform, Load) pipeline using Python, Pandas, and PostgreSQL.

---

# Architecture

```text
employees.csv
      │
      ▼
Extract (Pandas)
      │
      ▼
Transform
      │
      ▼
Load (PostgreSQL)
      │
      ▼
SQL Validation
```

---

# Topics Covered

- Python Virtual Environment
- Package Management using pip
- requirements.txt
- Pandas DataFrame
- Reading CSV files
- Data Transformation
- PostgreSQL Connection using psycopg
- Environment Variables (.env)
- Transaction Management
- Error Handling
- ETL Project Structure

---

# Project Structure

```text
DataEngineeringLab/
│
├── .env
├── requirements.txt
├── datasets/
│   └── employees.csv
│
├── docker/
│
├── src/
│   ├── database.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
└── README.md
```

---

# Virtual Environment

Create

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

# Installed Packages

```bash
pip install pandas
pip install "psycopg[binary]"
pip install python-dotenv
```

---

# requirements.txt

Generate

```bash
pip freeze > requirements.txt
```

Install later

```bash
pip install -r requirements.txt
```

---

# ETL Components

## Extract

Responsibilities

- Read CSV
- Return DataFrame

Functions used

```python
pd.read_csv()
```

---

## Transform

Operations

- Remove whitespace
- Standardize text
- Remove duplicates
- Remove NULL values

Example

```python
df["name"] = df["name"].str.strip().str.title()

df["department"] = df["department"].str.strip().str.upper()

df = df.drop_duplicates()

df = df.dropna()
```

---

## Load

Responsibilities

- Connect PostgreSQL
- Insert records
- Commit transaction
- Rollback on failure
- Close connection

---

# PostgreSQL Connection

Connection Library

```text
psycopg
```

Connection created in

```text
database.py
```

Configuration stored in

```text
.env
```

---

# Environment Variables

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=de_lab
DB_USER=postgres
DB_PASSWORD=postgres
```

Benefits

- No hardcoded credentials
- Easy environment switching
- Better security
- Production standard

---

# Better .env Loading

```python
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")
```

Advantages

- Independent of execution directory
- More reliable
- Production friendly

---

# Transaction Handling

```text
Start Transaction
        │
        ▼
Insert Records
        │
        ▼
Commit
```

If error occurs

```text
Start Transaction
        │
        ▼
Insert
        │
        ▼
Exception
        │
        ▼
Rollback
```

---

# Error Handling

```python
try:
    ...
except:
    conn.rollback()
finally:
    cursor.close()
    conn.close()
```

Purpose

- Prevent partial inserts
- Release database resources
- Handle failures gracefully

---

# ETL Flow

```text
employees.csv
      │
      ▼
extract.py
      │
      ▼
transform.py
      │
      ▼
load.py
      │
      ▼
PostgreSQL
```

---

# Learning Outcomes

After Day 5, I can:

- Create Python virtual environments
- Install Python packages
- Manage dependencies using requirements.txt
- Read CSV files using Pandas
- Transform data
- Connect Python to PostgreSQL
- Insert records into PostgreSQL
- Handle transactions
- Use environment variables
- Build a modular ETL project

---

# Challenges Faced

### Virtual Environment

Problem

```
ensurepip is not available
```

Solution

```bash
sudo apt install python3-venv
```

---

### psycopg Error

Problem

```
no pq wrapper available
```

Solution

```bash
pip install "psycopg[binary]"
```

---

### PostgreSQL Authentication

Problem

```
password authentication failed
```

Solution

Updated database credentials to match the PostgreSQL Docker container configuration.

---

# Best Practices Learned

- Never hardcode database credentials
- Use `.env` for configuration
- Keep database connection in a separate module
- Use parameterized SQL queries
- Always commit transactions
- Rollback on failure
- Always close database connections
- Separate Extract, Transform, and Load logic
- Keep dependencies in `requirements.txt`

---

# Current ETL Pipeline

```text
CSV
 │
 ▼
Extract
 │
 ▼
Transform
 │
 ▼
Load
 │
 ▼
PostgreSQL
```

---

# Status

✅ Day 5 Completed Successfully

Built first working ETL pipeline using Python and PostgreSQL.