# 🚀 DataEngineeringLab

> A production-ready Data Engineering project demonstrating modern ETL development using Python, PostgreSQL, Docker, automated testing, and GitHub Actions CI/CD.

![Python](https://img.shields.io/badge/Python-3.8-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 About the Project

**DataEngineeringLab** is my hands-on learning repository for mastering modern Data Engineering concepts by building production-style ETL pipelines.

The goal is not only to write ETL code, but also to follow software engineering best practices such as modular architecture, configuration management, logging, automated testing, transaction handling, code quality checks, and Continuous Integration (CI/CD).

This repository documents my journey from Python fundamentals to building scalable data engineering solutions with technologies such as PySpark, Airflow, Kafka, dbt, and AWS.

---

# 🎯 Project Objectives

- Learn Data Engineering through practical projects
- Build production-ready ETL pipelines
- Write clean, maintainable, and testable code
- Apply software engineering best practices
- Automate quality checks with CI/CD
- Continuously expand toward modern data platforms

---

# ✨ Features

## ETL Pipeline

- CSV Data Extraction
- Data Validation
- Data Transformation
- Incremental Loading (UPSERT)
- Batch Processing
- Transaction Management
- Rollback Support
- Execution Summary
- Structured Logging

---

## Data Validation

- File Validation
- Schema Validation
- Null Validation
- Blank Value Validation
- Duplicate Validation
- Salary Validation

---

## Testing

### Unit Testing

- Extract Module
- Transform Module
- Validation Modules
- Database Module
- Logger Module
- Incremental Loader

### Integration Testing

- Complete ETL Pipeline
- Incremental Loading
- UPSERT Verification
- Transaction Rollback

---

## Code Quality

- Black
- isort
- Flake8

---

## CI/CD

Implemented using **GitHub Actions**

Pipeline automatically performs:

- Checkout Repository
- Setup Python
- Install Dependencies
- Start PostgreSQL
- Create Database Schema
- Run Black
- Run isort
- Run Flake8
- Execute Unit Tests
- Execute Integration Tests
- Generate Code Coverage
- Upload Coverage Reports

---

# 🛠 Technology Stack

| Category         | Technology           |
| ---------------- | -------------------- |
| Language         | Python 3.8           |
| Database         | PostgreSQL 16        |
| Data Processing  | Pandas               |
| Containerization | Docker               |
| Version Control  | Git & GitHub         |
| Testing          | Pytest               |
| Code Quality     | Black, isort, Flake8 |
| CI/CD            | GitHub Actions       |
| IDE              | VS Code              |
| Environment      | WSL2 Ubuntu          |

---

# 🏗 Architecture

## ETL Workflow

```text
CSV
 │
 ▼
Extract
 │
 ▼
Validation
 │
 ▼
Transformation
 │
 ▼
Incremental Loader
 │
 ▼
PostgreSQL

# 📂 Repository Structure

```text
DataEngineeringLab/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── architecture/
├── datasets/
├── docker/
├── docs/
├── experiments/
├── logs/
├── scripts/
├── src/
│   ├── validations/
│   ├── config.py
│   ├── database.py
│   ├── extract.py
│   ├── transform.py
│   ├── load_incremental.py
│   ├── logger.py
│   └── main.py
│
├── tests/
│   ├── integration/
│   └── unit/
│
├── .env.example
├── requirements.txt
├── README.md
└── LICENSE
```
---

# 📋 Prerequisites

Before running this project, ensure the following software is installed on your system.

| Software              | Version      |
| --------------------- | ------------ |
| Python                | 3.8 or later |
| PostgreSQL            | 16           |
| Docker                | Latest       |
| Docker Compose        | Latest       |
| Git                   | Latest       |
| VS Code (Recommended) | Latest       |

Verify your installation:

```bash
python --version
docker --version
docker compose version
git --version
```

---

# 📥 Clone Repository

Clone the repository from GitHub.

```bash
git clone https://github.com/Upendrakumar23/DataEngineeringLab.git

cd DataEngineeringLab
```

---

# 🐍 Create Python Virtual Environment

Create and activate a virtual environment.

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

---

# 📦 Install Dependencies

Install all required Python packages.

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

Verify installation.

```bash
pip list
```

---

# ⚙️ Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=de_lab
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password

LOG_LEVEL=INFO
LOG_DIR=logs
```

> **Note:** Never commit your actual `.env` file to GitHub. Use `.env.example` as a template.

---

# 🐳 Start PostgreSQL using Docker

Start the PostgreSQL container.

```bash
docker compose up -d
```

Verify that the container is running.

```bash
docker ps
```

Expected output:

```
postgres-lab
```

---

# 🗄 Database Initialization

If the database and table are not already created, initialize PostgreSQL.

Connect to PostgreSQL:

```bash
docker exec -it postgres-lab psql -U postgres -d de_lab
```

Create the employees table:

```sql
CREATE TABLE IF NOT EXISTS employees (
    employee_code VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary NUMERIC(10,2)
);
```

Exit PostgreSQL:

```sql
\q
```

---

# ▶️ Run the ETL Pipeline

Execute the ETL pipeline.

```bash
python -m src.main
```

Expected workflow:

```text
Validate Source File
        │
        ▼
Extract CSV
        │
        ▼
Validate Data
        │
        ▼
Transform Data
        │
        ▼
Incremental UPSERT
        │
        ▼
PostgreSQL
```

---

# 📂 Logs

Execution logs are generated automatically.

Location:

```text
logs/
```

Example log output:

```text
INFO  Starting ETL Pipeline
INFO  Validating source file
INFO  Extracting records
INFO  Transforming records
INFO  Loading records
INFO  ETL Pipeline Completed Successfully
```

---

# 🧪 Running Tests

Run all tests.

```bash
pytest
```

Run only unit tests.

```bash
pytest tests/unit
```

Run only integration tests.

```bash
pytest tests/integration
```

Generate code coverage.

```bash
pytest --cov=src --cov-report=html
```

Coverage report:

```text
htmlcov/index.html
```

---

# 🔄 Continuous Integration (CI/CD)

This project uses **GitHub Actions** for Continuous Integration.

The pipeline automatically performs:

- Checkout Repository
- Setup Python Environment
- Install Dependencies
- Start PostgreSQL Service
- Create Database Schema
- Run Black
- Run isort
- Run Flake8
- Execute Unit Tests
- Execute Integration Tests
- Generate Code Coverage
- Upload Coverage Reports

Workflow file:

```text
.github/workflows/python-ci.yml
```

---

# 📸 Screenshots

### GitHub Actions

> Add screenshot after first successful workflow.

```text
docs/screenshots/github-actions-success.png
```

---

### ETL Execution

> Add terminal execution screenshot.

```text
docs/screenshots/etl-execution.png
```

---

### Code Coverage

> Add HTML coverage report screenshot.

```text
docs/screenshots/coverage-report.png
```
---

# 🛠 Tech Stack

| Category         | Technologies          |
| ---------------- | --------------------- |
| Language         | Python                |
| Database         | PostgreSQL            |
| Containerization | Docker                |
| Version Control  | Git & GitHub          |
| Testing          | Pytest, unittest.mock |
| Data Processing  | Pandas                |
| Logging          | Python Logging        |
| Environment      | WSL2 Ubuntu, VS Code  |

---

# ✅ Features Implemented

## ETL Pipeline

- CSV Extraction
- Data Validation
- Data Transformation
- Incremental UPSERT Loading
- Batch Loading
- Transaction Management
- Rollback Support
- Execution Summary
- Structured Logging

---

## Data Validation

- File Validation
- Schema Validation
- Null Validation
- Blank Value Validation
- Duplicate Validation
- Salary Validation

---

## Testing

### Unit Testing

- Extract Module
- Transform Module
- Validation Modules
- Database Module
- Logger Module
- Incremental Loader

### Integration Testing

- Complete ETL Pipeline
- Incremental Loading
- UPSERT Verification
- Transaction Rollback

---

# 📈 Current Learning Progress

| Module                   | Status      |
| ------------------------ | ----------- |
| Engineering Workspace    | ✅ Completed |
| Git & GitHub             | ✅ Completed |
| Linux Basics             | ✅ Completed |
| Docker Fundamentals      | ✅ Completed |
| PostgreSQL with Docker   | ✅ Completed |
| Python ETL Development   | ✅ Completed |
| Data Validation          | ✅ Completed |
| Logging                  | ✅ Completed |
| Refactoring              | ✅ Completed |
| Unit Testing             | ✅ Completed |
| Integration Testing      | ✅ Completed |
| Code Quality             | ⏳ Planned   |
| CI/CD (GitHub Actions)   | ⏳ Planned   |
| Apache Spark             | ⏳ Planned   |
| Airflow                  | ⏳ Planned   |
| Kafka                    | ⏳ Planned   |
| dbt                      | ⏳ Planned   |
| AWS                      | ⏳ Planned   |
| End-to-End Data Pipeline | ⏳ Planned   |

---

# 📊 Project Highlights

- Modular ETL Architecture
- Configuration Management
- Environment Variables (.env)
- Production-style Logging
- Incremental Data Loading (UPSERT)
- Transaction Handling
- Automated Testing
- Clean Project Structure
- Industry-standard Coding Practices

---

# 🎯 Upcoming Learning

- Code Quality (Black, Flake8, isort)
- GitHub Actions (CI/CD)
- Test Coverage Reports
- Apache Spark
- Airflow Orchestration
- Kafka Streaming
- dbt Transformations
- AWS Data Engineering Services
- End-to-End Data Engineering Pipeline

---

# 👨‍💻 Author

**Upendra Kumar**

Learning Data Engineering through practical, production-style projects.
