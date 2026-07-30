# Day 1 - Docker Basics

**Date:** 12 July 2026

---

# Objective

Understand the fundamentals of Docker and set up a professional Data Engineering learning environment.

---

# Topics Covered

- What is Docker?
- Why Docker is used
- Docker Image
- Docker Container
- Docker Hub
- Docker Engine
- Running the first Docker container
- Project setup with Git & GitHub

---

# What is Docker?

Docker is a containerization platform that packages an application along with its dependencies so that it runs consistently across different environments.

---

# Why Docker?

- Consistent environments
- Lightweight compared to Virtual Machines
- Fast deployment
- Easy dependency management
- Portable applications

---

# Docker Architecture

```
Docker Hub
      │
      ▼
Docker Engine
      │
      ▼
Docker Image
      │
docker run
      ▼
Docker Container
```

---

# Docker Image

A Docker Image is a **read-only template** that contains:

- Application
- Libraries
- Dependencies
- Configuration
- Runtime

An image acts as a blueprint for creating containers.

---

# Docker Container

A Docker Container is a **running instance of an image**.

A container:

- Executes applications
- Uses CPU and RAM while running
- Has a writable filesystem
- Can be started, stopped, or removed

---

# Commands Learned

```bash
docker run hello-world
docker images
docker ps
docker ps -a
```

---

# Repository Created

```
DataEngineeringLab/
├── architecture/
├── datasets/
├── docker/
├── docs/
├── experiments/
├── scripts/
└── README.md
```

---

# Git Commands

```bash
git init
git add .
git commit -m "Initial commit"
git push
```

---

# Key Learnings

- Docker Images are templates.
- Containers are instances of images.
- One image can create multiple containers.
- Containers are isolated from the host machine.

---

# Interview Questions

### What is Docker?

Docker is a containerization platform that packages applications with their dependencies.

---

### Difference between Virtual Machine and Docker?

| Docker | Virtual Machine |
|---------|-----------------|
| Lightweight | Heavy |
| Shares Host OS | Separate Guest OS |
| Fast Startup | Slow Startup |

---

# Summary

Today I learned Docker fundamentals and created a professional GitHub repository for my Data Engineering learning journey.