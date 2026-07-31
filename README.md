# 🚀 DataEngineeringLab

> **A production-ready Data Engineering project demonstrating modern ETL development using Python, PostgreSQL, Docker, automated testing, and GitHub Actions CI/CD.**

![Python](https://img.shields.io/badge/Python-3.8-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📑 Table of Contents

- [🚀 DataEngineeringLab](#-dataengineeringlab)
- [📑 Table of Contents](#-table-of-contents)
- [📖 About the Project](#-about-the-project)
- [📊 Project Summary](#-project-summary)
- [🎯 Project Objectives](#-project-objectives)
- [✨ Features](#-features)
  - [ETL Pipeline](#etl-pipeline)
  - [Data Validation](#data-validation)
  - [Testing](#testing)
    - [Unit Testing](#unit-testing)
    - [Integration Testing](#integration-testing)
  - [Code Quality](#code-quality)
  - [Continuous Integration (CI/CD)](#continuous-integration-cicd)
- [🛠 Technology Stack](#-technology-stack)
- [🏗 Architecture](#-architecture)
  - [ETL Workflow](#etl-workflow)
- [📂 Repository Structure](#-repository-structure)
- [🚀 Getting Started](#-getting-started)
- [📋 Prerequisites](#-prerequisites)
- [⚡ Quick Start](#-quick-start)
- [📥 Clone Repository](#-clone-repository)
- [🐍 Create Python Virtual Environment](#-create-python-virtual-environment)
  - [Linux / macOS](#linux--macos)
  - [Windows](#windows)
- [📦 Install Dependencies](#-install-dependencies)
- [⚙️ Configure Environment Variables](#️-configure-environment-variables)
- [🐳 Start PostgreSQL](#-start-postgresql)
- [🗄 Database Initialization](#-database-initialization)
- [▶️ Run the ETL Pipeline](#️-run-the-etl-pipeline)
- [📂 Logs](#-logs)
- [🧪 Running Tests](#-running-tests)
- [🔄 Continuous Integration (CI/CD)](#-continuous-integration-cicd)
- [📸 Screenshots](#-screenshots)
  - [GitHub Actions](#github-actions)
  - [ETL Pipeline Execution](#etl-pipeline-execution)
  - [Code Coverage Report](#code-coverage-report)
- [📈 Learning Progress](#-learning-progress)
- [🗺 Roadmap](#-roadmap)
  - [✅ Completed](#-completed)
  - [🚧 Next Phase](#-next-phase)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)
- [⭐ Support](#-support)
- [🙏 Acknowledgements](#-acknowledgements)
  - [📬 Feedback](#-feedback)

---

# 📖 About the Project

**DataEngineeringLab** is my hands-on learning repository focused on mastering modern **Data Engineering** concepts by building production-ready ETL pipelines.

The project goes beyond writing ETL scripts by applying software engineering best practices, including:

- Modular Architecture
- Configuration Management
- Data Validation
- Structured Logging
- Incremental Loading (UPSERT)
- Transaction Management
- Automated Testing
- Code Quality
- Continuous Integration (CI/CD)

This repository documents my learning journey from Python-based ETL development toward advanced technologies including **PySpark**, **Apache Airflow**, **Kafka**, **dbt**, **AWS**, and modern Data Lakehouse architectures.

---

# 📊 Project Summary

| Item             | Details                       |
| ---------------- | ----------------------------- |
| Project Name     | DataEngineeringLab            |
| Project Type     | Production-style ETL Pipeline |
| Language         | Python 3.8                    |
| Database         | PostgreSQL 16                 |
| Containerization | Docker                        |
| Data Processing  | Pandas                        |
| Testing          | Pytest                        |
| CI/CD            | GitHub Actions                |
| Architecture     | Modular ETL                   |
| Current Status   | Production Ready              |

---

# 🎯 Project Objectives

The primary objectives of this repository are to:

- Learn Data Engineering through practical projects
- Build production-ready ETL pipelines
- Write clean, maintainable, and testable code
- Apply software engineering best practices
- Automate testing and deployments
- Gain hands-on experience with modern Data Engineering tools
- Build a professional portfolio for Data Engineering roles

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

## Continuous Integration (CI/CD)

Implemented using **GitHub Actions**

The automated pipeline performs:

- Checkout Repository
- Setup Python Environment
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
             CSV Dataset
                  │
                  ▼
          Extract Data
                  │
                  ▼
          Validate Data
                  │
                  ▼
         Transform Data
                  │
                  ▼
 Incremental UPSERT Loader
                  │
                  ▼
            PostgreSQL
```

> **Note:** This text-based diagram will be replaced with a Mermaid architecture diagram in the next documentation module.

---

# 📂 Repository Structure

```text
DataEngineeringLab/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── architecture/          # Architecture diagrams
├── datasets/              # Sample datasets
├── docker/                # Docker configuration
├── docs/                  # Documentation
├── experiments/           # Learning experiments
├── logs/                  # ETL execution logs
├── scripts/               # Utility scripts
│
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
├── LICENSE
├── CONTRIBUTING.md
└── CHANGELOG.md
```

---

# 🚀 Getting Started

Follow the steps below to set up and run the project on your local machine.

---

# 📋 Prerequisites

Ensure the following software is installed before running this project.

| Software              | Version      |
| --------------------- | ------------ |
| Python                | 3.8 or later |
| PostgreSQL            | 16           |
| Docker                | Latest       |
| Docker Compose        | Latest       |
| Git                   | Latest       |
| VS Code (Recommended) | Latest       |

Verify the installation:

```bash
python --version
docker --version
docker compose version
git --version
```

---

# ⚡ Quick Start

Clone the repository and run the ETL pipeline.

```bash
git clone https://github.com/Upendrakumar23/DataEngineeringLab.git

cd DataEngineeringLab

python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt

docker compose up -d

python -m src.main
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

## Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

## Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

---

# 📦 Install Dependencies

Upgrade pip.

```bash
pip install --upgrade pip
```

Install project dependencies.

```bash
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

# 🐳 Start PostgreSQL

Start PostgreSQL using Docker Compose.

```bash
docker compose up -d
```

Verify that the container is running.

```bash
docker ps
```

Expected output:

```text
postgres-lab
```

---

# 🗄 Database Initialization

If the database has not already been initialized, create the `employees` table.

Connect to PostgreSQL.

```bash
docker exec -it postgres-lab psql -U postgres -d de_lab
```

Execute the following SQL.

```sql
CREATE TABLE IF NOT EXISTS employees (
    employee_code VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary NUMERIC(10,2)
);
```

Exit PostgreSQL.

```sql
\q
```

---

# ▶️ Run the ETL Pipeline

Execute the pipeline.

```bash
python -m src.main
```

ETL execution flow.

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

Execution logs are automatically generated.

Location:

```text
logs/
```

Example output.

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

Run unit tests.

```bash
pytest tests/unit
```

Run integration tests.

```bash
pytest tests/integration
```

Generate coverage report.

```bash
pytest --cov=src --cov-report=html
```

Coverage report location.

```text
htmlcov/index.html
```

---

# 🔄 Continuous Integration (CI/CD)

This project uses **GitHub Actions** to automate code quality and testing.

The CI pipeline performs the following tasks automatically.

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

Workflow location.

```text
.github/workflows/python-ci.yml
```

---

# 📸 Screenshots

## GitHub Actions

Add a screenshot after the first successful workflow execution.

```text
docs/screenshots/github-actions-success.png
```

---

## ETL Pipeline Execution

Add the terminal output screenshot.

```text
docs/screenshots/etl-execution.png
```

---

## Code Coverage Report

Add the HTML coverage report screenshot.

```text
docs/screenshots/coverage-report.png
```

---

# 📈 Learning Progress

| Module                              | Status      |
| ----------------------------------- | ----------- |
| Engineering Workspace               | ✅ Completed |
| Git & GitHub                        | ✅ Completed |
| Linux Fundamentals                  | ✅ Completed |
| Docker                              | ✅ Completed |
| PostgreSQL                          | ✅ Completed |
| Python ETL Development              | ✅ Completed |
| Data Validation                     | ✅ Completed |
| Logging                             | ✅ Completed |
| Refactoring                         | ✅ Completed |
| Unit Testing                        | ✅ Completed |
| Integration Testing                 | ✅ Completed |
| Code Quality (Black, isort, Flake8) | ✅ Completed |
| GitHub Actions CI/CD                | ✅ Completed |
| Apache Spark                        | ⏳ Planned   |
| Apache Airflow                      | ⏳ Planned   |
| Kafka                               | ⏳ Planned   |
| dbt                                 | ⏳ Planned   |
| AWS                                 | ⏳ Planned   |
| Snowflake                           | ⏳ Planned   |
| End-to-End Data Platform            | ⏳ Planned   |

---

# 🗺 Roadmap

## ✅ Completed

- Python ETL Pipeline
- PostgreSQL Integration
- Docker
- Data Validation
- Structured Logging
- Incremental Loading (UPSERT)
- Transaction Management
- Unit Testing
- Integration Testing
- Code Quality
- GitHub Actions CI/CD

---

## 🚧 Next Phase

- Apache Spark
- Apache Airflow
- Kafka
- dbt
- MinIO
- AWS S3
- AWS Glue
- Redshift
- Snowflake
- Data Lakehouse Architecture

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

Please read **CONTRIBUTING.md** before contributing.

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for details.

---

# 👨‍💻 Author

**Upendra Kumar**

Data Engineer | Continuous Learner

**GitHub**

https://github.com/Upendrakumar23

**Project Repository**

https://github.com/Upendrakumar23/DataEngineeringLab

---

# ⭐ Support

If you found this repository useful, please consider giving it a ⭐ on GitHub.

Your support motivates me to continue building production-grade Data Engineering projects and sharing my learning journey.

---

# 🙏 Acknowledgements

This repository represents my continuous learning journey toward becoming a professional Data Engineer.

Every module is built incrementally using industry-standard software engineering practices with a strong focus on:

- Clean Code
- Modular Design
- Automated Testing
- CI/CD
- Production Readiness
- Maintainability
- Continuous Learning

---

## 📬 Feedback

Suggestions, improvements, and constructive feedback are always welcome.

Feel free to open an issue or submit a pull request if you have ideas to improve this project.

Happy Learning! 🚀
