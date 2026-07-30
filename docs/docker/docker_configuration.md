# Docker Configuration Guide

## Purpose

This document explains how the PostgreSQL Docker environment is organized in the **DataEngineeringLab** project.

---

# Project Structure

```text
DataEngineeringLab/
│
├── docker/
│   └── postgres/
│       ├── docker-compose.yml
│       ├── .env
│       └── init.sql
│
├── scripts/
│   ├── start_db.sh
│   ├── stop_db.sh
│   └── connect_db.sh
│
├── config/
│   └── db.conf
│
└── docs/
```

---

# Configuration Files

## 1. .env

**Location**

```text
docker/postgres/.env
```

This file stores Docker Compose environment variables.

Example:

```properties
POSTGRES_CONTAINER=postgres-lab
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=de_lab
POSTGRES_PORT=5432
```

Benefits:

* Avoids hardcoded values
* Easy to change environment settings
* Used by Docker Compose

---

## 2. docker-compose.yml

This file defines the PostgreSQL container.

Example:

```yaml
services:

  postgres:
    image: postgres:16

    container_name: ${POSTGRES_CONTAINER}

    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}

    ports:
      - "${POSTGRES_PORT}:5432"

    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

    restart: unless-stopped

volumes:
  postgres_data:
```

---

## 3. config/db.conf

Purpose:

* Shared configuration for Bash scripts
* Loads Docker environment variables

Example:

```bash
#!/bin/bash

PROJECT_ROOT="/mnt/d/Projects/DataEngineeringLab"
DOCKER_DIR="$PROJECT_ROOT/docker/postgres"

set -a
source "$DOCKER_DIR/.env"
set +a

COMPOSE_FILE="docker-compose.yml"
```

---

# Bash Scripts

All scripts load the configuration from `db.conf`.

```bash
source "$(dirname "$0")/../config/db.conf"
```

This makes variables such as:

* POSTGRES_CONTAINER
* POSTGRES_DB
* POSTGRES_USER
* POSTGRES_PORT

available to every script.

---

## start_db.sh

Starts PostgreSQL.

Command:

```bash
./scripts/start_db.sh
```

---

## stop_db.sh

Stops PostgreSQL.

Command:

```bash
./scripts/stop_db.sh
```

---

## connect_db.sh

Connects to PostgreSQL.

Command:

```bash
./scripts/connect_db.sh
```

---

# Why use variables?

Instead of hardcoding:

```bash
docker exec -it postgres-lab psql -U postgres -d de_lab
```

we use:

```bash
docker exec -it "$POSTGRES_CONTAINER" \
    psql -U "$POSTGRES_USER" \
    -d "$POSTGRES_DB"
```

Advantages:

* Easier maintenance
* Less duplication
* Consistent configuration
* Easy to rename containers or databases

---

# Common Issues

## Error

```text
$'\r': command not found
```

Cause:

Windows (CRLF) line endings.

Fix:

* Save files with **LF** line endings.
* Or run:

```bash
dos2unix config/db.conf
dos2unix scripts/*.sh
```

---

## Error

```text
No such file or directory
```

Cause:

Incorrect path to `.env`.

Verify:

```bash
ls docker/postgres/.env
```

---

# Best Practices

* Keep Docker-related configuration inside `docker/postgres/`.
* Never hardcode container names or database names in scripts.
* Use `.env` for Docker Compose variables.
* Use `db.conf` as the single configuration loader for Bash scripts.
* Use `set -e` in Bash scripts to stop execution on errors.
* Store helper scripts under the `scripts/` directory.
* Document changes under the `docs/` directory.

---

# Frequently Used Commands

Start database:

```bash
./scripts/start_db.sh
```

Stop database:

```bash
./scripts/stop_db.sh
```

Connect to PostgreSQL:

```bash
./scripts/connect_db.sh
```

Check running containers:

```bash
docker ps
```

View logs:

```bash
docker logs postgres-lab
```

---

# Learning Outcome

After completing this setup, you should understand:

* Docker Compose
* Environment variables
* Configuration management
* Bash scripting
* Separation of configuration and automation
* Database container lifecycle
* Industry-standard project organization
