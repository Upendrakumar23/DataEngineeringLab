# Day 3 - PostgreSQL in Docker

**Date:** 15 July 2026

---

# Objective

Run a real PostgreSQL server inside Docker and understand persistent storage.

---

# Topics Covered

- PostgreSQL Image
- Running PostgreSQL
- Port Mapping
- Environment Variables
- docker exec
- psql
- Database creation
- Why Docker Volumes are needed

---

# Pull PostgreSQL Image

```bash
docker pull postgres:16
```

Docker downloads the PostgreSQL image from Docker Hub.

---

# Run PostgreSQL

```bash
docker run -d \
--name postgres-lab \
-e POSTGRES_PASSWORD=postgres123 \
-p 5432:5432 \
postgres:16
```

---

# Understanding the Command

| Option | Meaning |
|---------|----------|
| -d | Detached Mode |
| --name | Container Name |
| -e | Environment Variable |
| -p | Port Mapping |
| postgres:16 | Docker Image |

---

# Port Mapping

```
Host Machine
Port 5432
      │
      ▼
Docker Container
Port 5432
      │
      ▼
PostgreSQL Server
```

---

# Connect to PostgreSQL

```bash
docker exec -it postgres-lab psql -U postgres
```

---

# Create Database

```sql
CREATE DATABASE de_lab;
```

---

# Connect Database

```sql
\c de_lab
```

---

# Create Table

```sql
CREATE TABLE employees(
id INT PRIMARY KEY,
name VARCHAR(100),
department VARCHAR(50)
);
```

---

# Insert Data

```sql
INSERT INTO employees VALUES
(1,'Upendra','Data Engineering'),
(2,'Rahul','Analytics');
```

---

# Query Data

```sql
SELECT * FROM employees;
```

---

# Container Storage

Without Docker Volume:

```
Container
│
├── PostgreSQL
├── Database
└── Writable Filesystem
```

Deleting the container also deletes the writable filesystem.

---

# Why Docker Volumes?

A Docker Volume stores data outside the container.

```
Docker Volume
      ▲
      │
Container
      │
PostgreSQL
```

Benefits:

- Data persistence
- Container recreation
- Backup
- Production ready

---

# Key Learnings

- PostgreSQL is a long-running application.
- A container runs as long as its main process runs.
- Databases should never rely on the container's writable filesystem.
- Docker Volumes provide persistent storage.

---

# Interview Questions

### Why doesn't hello-world keep running?

Because its main process finishes immediately, causing the container to exit.

---

### Why does PostgreSQL keep running?

Because the PostgreSQL server continues waiting for client connections.

---

### Why should production databases use Docker Volumes?

Docker Volumes preserve data independently of the container. If a container is deleted, the data stored in the volume remains available.

---

# Summary

Today I deployed my first PostgreSQL server inside Docker, connected using `psql`, created a database, and understood why persistent storage with Docker Volumes is essential for production databases.