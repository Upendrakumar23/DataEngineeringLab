"""
Application configuration.
Loads environment variables from the project's .env file.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# Database Configuration
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

# Application Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_DIR = os.getenv("LOG_DIR", "logs")

# Dataset Configuration
DATASET_DIR = BASE_DIR / "datasets"

# Validate required database configuration
required_configs = {
    "POSTGRES_HOST": DB_HOST,
    "POSTGRES_PORT": DB_PORT,
    "POSTGRES_DB": DB_NAME,
    "POSTGRES_USER": DB_USER,
    "POSTGRES_PASSWORD": DB_PASSWORD,
}

missing_configs = [key for key, value in required_configs.items() if not value]

if missing_configs:
    raise ValueError(
        f"Missing required environment variables: {', '.join(missing_configs)}"
    )

REQUIRED_COLUMNS = [
    "employee_code",
    "name",
    "department",
    "salary",
]
