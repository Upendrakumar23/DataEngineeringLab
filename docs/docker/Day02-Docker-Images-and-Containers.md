# Day 2 - Docker Images and Containers

**Date:** 14 July 2026

---

# Objective

Understand the lifecycle of Docker Images and Containers.

---

# Topics Covered

- Image lifecycle
- Container lifecycle
- docker run
- docker start
- docker stop
- docker rm
- Image storage
- Why hello-world behaves differently

---

# Docker Image Lifecycle

```
Docker Hub
      │
docker pull
      ▼
Local Image
      │
docker run
      ▼
Container
```

---

# Container Lifecycle

```
docker run
      │
      ▼
Running
      │
docker stop
      ▼
Stopped
      │
docker start
      ▼
Running
      │
docker rm
      ▼
Deleted
```

---

# Important Commands

## Download Image

```bash
docker pull hello-world
```

---

## Create Container

```bash
docker run hello-world
```

---

## List Images

```bash
docker images
```

---

## Running Containers

```bash
docker ps
```

---

## All Containers

```bash
docker ps -a
```

---

## Start Existing Container

```bash
docker start <container-id>
```

---

## Stop Container

```bash
docker stop <container-id>
```

---

## Remove Container

```bash
docker rm <container-id>
```

---

# Key Concepts

## docker run

Creates a **new container** from an image.

---

## docker start

Starts an **existing stopped container**.

---

## Why second docker run doesn't download again?

Docker checks whether the image already exists locally.

If available, it creates a new container without downloading the image.

---

# Image vs Container

| Image | Container |
|---------|----------|
| Blueprint | Running Instance |
| Read Only | Writable |
| Can create multiple containers | Created from image |

---

# What happens when container is deleted?

- Container removed
- Writable filesystem removed
- Image remains

---

# What happens when image is deleted?

Docker downloads it again from Docker Hub during the next `docker run`.

---

# Key Learnings

- Images are reusable.
- Containers are disposable.
- Multiple containers can be created from one image.
- docker run always creates a new container.
- docker start reuses an existing container.

---

# Interview Questions

### Difference between docker run and docker start?

`docker run`

- Creates a new container.
- Starts it.

`docker start`

- Starts an existing stopped container.
- Does not create a new one.

---

# Summary

Today I understood Docker Image and Container lifecycle along with how Docker manages images locally.