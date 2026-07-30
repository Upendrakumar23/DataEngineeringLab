# DataEngineeringLab
# Day 7 - Dremio PostgreSQL Connection Troubleshooting

## Objective

Connect Dremio to the PostgreSQL Docker container.

---

## Problem

While adding PostgreSQL as a source in Dremio, the following error occurred:

```
Could not connect to postgres_lab,
check your JDBC connection information and credentials.
```

---

## Initial Assumptions

Possible reasons:

- PostgreSQL container not running
- Dremio container not running
- Wrong Docker network
- JDBC Driver missing
- Wrong hostname
- Wrong credentials
- PostgreSQL not listening on TCP

---

## Step 1

Verified containers

```bash
docker ps
```

Result

```
postgres-lab
dremio-lab
```

Both containers were healthy.

---

## Step 2

Verified Docker Networks

Initially

```
postgres_default

dremio_default
```

Problem:

Containers were on different Docker networks.

Created a shared network.

```bash
docker network create de-network
```

Updated both docker-compose.yml files

```yaml
networks:
  - de-network

networks:
  de-network:
    external: true
```

---

## Step 3

Verified Docker DNS

Inside Dremio container

```bash
getent hosts postgres-lab
```

Output

```
172.20.0.2 postgres-lab
```

Docker DNS was working.

---

## Step 4

Verified TCP connectivity

Inside Dremio

```bash
timeout 5 bash -c '</dev/tcp/postgres-lab/5432'
```

Output

```
Connected
```

Network connectivity was successful.

---

## Step 5

Verified PostgreSQL

Connected using

```sql
\conninfo
```

Checked

```sql
SHOW listen_addresses;

SHOW port;
```

Output

```
listen_addresses = *

port = 5432
```

PostgreSQL was accepting TCP connections.

---

## Root Cause

The hostname entered in Dremio was

```
postgres_lab
```

The correct Docker hostname is

```
postgres-lab
```

Reason:

Docker DNS resolves container names.

Container Name

```
postgres-lab
```

Docker DNS

```
postgres-lab
↓

172.20.0.2
```

Using

```
postgres_lab
```

does not exist in Docker DNS.

---

## Correct Dremio Configuration

Name

```
postgres_lab
```

Host

```
postgres-lab
```

Port

```
5432
```

Database

```
de_lab
```

Username

```
postgres
```

Password

```
postgres
```

Encrypt Connection

```
Disabled
```

Authentication

```
Master Credentials
```

---

## Final Architecture

```
                de-network

      +---------------------------+

      |                           |

PostgreSQL                 Dremio

postgres-lab              dremio-lab

172.20.0.2                172.20.0.3

      |                           |

      +-----------Docker-----------+

                  |

             employees table

                  |

             Virtual Dataset
```

---

## Lessons Learned

- Docker networking is critical.
- Containers communicate using container/service names.
- Always verify:
  - Network
  - DNS
  - TCP
  - Database
  - Authentication
- Never assume the root cause.
- Troubleshoot layer by layer.

---

## Resume Value

Hands-on experience with:

- Docker Networking
- PostgreSQL
- Dremio
- Infrastructure Debugging
- Container Communication
- Enterprise Data Platform Setup
