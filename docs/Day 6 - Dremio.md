# Data Engineering Lab - Day 6
## Topic: Dockerizing Dremio OSS

**Date:** 22 July 2026

---

# Objective

Deploy Dremio OSS using Docker as the SQL Lakehouse Engine for the Data Engineering Lab.

---

# Why Dremio?

Dremio is **not a database**.

It is a **Lakehouse SQL Engine** that allows querying data from multiple sources without copying data.

Supported sources include:

- PostgreSQL
- Oracle
- SQL Server
- MinIO (S3)
- Iceberg
- Delta Lake
- Hive
- Nessie
- MongoDB
- Local Files

---

# Current Lab Architecture

```
                +----------------+
                |   Python ETL   |
                +-------+--------+
                        |
                        |
                 PostgreSQL 16
                        |
                        |
                   Dremio OSS
                        |
                  SQL Analytics
```

---

# Docker Image

Pulled official image

```bash
docker pull dremio/dremio-oss
```

Verify

```bash
docker images
```

Output

```
dremio/dremio-oss:latest
```

---

# Project Structure

```
DataEngineeringLab/

docker/
│
├── postgres/
│
└── dremio/
      │
      ├── docker-compose.yml
      └── .env
```

---

# .env

```properties
DREMIO_CONTAINER=dremio-lab

DREMIO_WEB_PORT=9047
DREMIO_CLIENT_PORT=31010
DREMIO_COORDINATOR_PORT=45678
DREMIO_FLIGHT_PORT=32010
```

---

# docker-compose.yml

```yaml
services:
  dremio:
    image: dremio/dremio-oss:latest
    container_name: ${DREMIO_CONTAINER}

    ports:
      - "${DREMIO_WEB_PORT}:9047"
      - "${DREMIO_CLIENT_PORT}:31010"
      - "${DREMIO_COORDINATOR_PORT}:45678"
      - "${DREMIO_FLIGHT_PORT}:32010"

    volumes:
      - dremio-data:/opt/dremio/data

    restart: unless-stopped

volumes:
  dremio-data:
```

---

# Start Container

```bash
docker compose up -d
```

---

# Verify

```bash
docker ps
```

Expected

```
postgres-lab
dremio-lab
```

---

# Access Dremio

```
http://localhost:9047
```

Created Admin User

```
Username : upendra27
pass: Up@9955622976
```

---

# Issue Faced

Browser showed

```
ERR_EMPTY_RESPONSE
```

---

# Root Cause

Dremio failed during startup because the metadata directory owner did not match the user running inside the container.

Error

```
Process user (dremio) doesn't match local catalog db owner (ubuntu)
```

Reason

A bind-mounted local directory (`./data`) retained ownership information from WSL, while Dremio inside the container runs as the `dremio` user.

---

# Resolution

Replaced bind mount

```yaml
./data:/opt/dremio/data
```

with Docker Named Volume

```yaml
volumes:
  dremio-data:/opt/dremio/data
```

Advantages

- Eliminates WSL permission issues
- Better portability
- Production-friendly
- Easier backups
- Cleaner Docker configuration

---

# Commands Learned

Pull image

```bash
docker pull dremio/dremio-oss
```

Start container

```bash
docker compose up -d
```

Stop container

```bash
docker compose down
```

View logs

```bash
docker logs dremio-lab
```

Follow logs

```bash
docker logs -f dremio-lab
```

Running containers

```bash
docker ps
```

Docker images

```bash
docker images
```

Docker volumes

```bash
docker volume ls
```

---

# Key Learnings

- Dremio is a SQL Lakehouse Engine.
- Dremio is not a storage system.
- Docker Named Volumes are preferred over bind mounts for application data.
- Reading container logs is the first step when debugging startup issues.
- Container ownership and file permissions matter, especially with WSL.

---

# Production Architecture

```
                Python ETL
                     |
         +-----------+-----------+
         |                       |
    PostgreSQL              MinIO (Future)
         |                       |
         +-----------+-----------+
                     |
                  Dremio
                     |
                SQL Analytics
                     |
              dbt / Power BI
```

---

# Next Session (Day 8)

- Connect PostgreSQL to Dremio
- Query employees table
- Understand Sources
- Understand Spaces
- Create first Virtual Dataset (VDS)
- Learn Physical Dataset (PDS)
- Introduction to Dremio Semantic Layer

---

# Status

| Component           | Status |
| ------------------- | ------ |
| Docker              | ✅      |
| PostgreSQL          | ✅      |
| Python ETL          | ✅      |
| Dremio OSS          | ✅      |
| Admin User          | ✅      |
| Docker Named Volume | ✅      |

---

## Mentor Notes

Today's objective was not only to install Dremio but also to understand how a production-ready Docker deployment differs from a quick local setup. By switching to a named Docker volume, the lab is now better prepared for the upcoming integration with PostgreSQL, MinIO, PySpark, Iceberg, and dbt.
