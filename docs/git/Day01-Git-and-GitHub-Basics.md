# Day 1 - Git & GitHub Basics

**Date:** 15 July 2026

---

# Objective

Understand the fundamentals of Git and GitHub, initialize a repository, connect it to GitHub, and push the first project.

---

# Topics Covered

- What is Version Control?
- What is Git?
- What is GitHub?
- Local Repository
- Remote Repository
- Git Workflow
- Initial Project Setup

---

# What is Version Control?

Version Control is a system that tracks changes made to files over time. It enables developers to:

- Maintain project history
- Collaborate with teams
- Restore previous versions
- Track who made changes

---

# What is Git?

Git is a **distributed version control system** used to manage source code and track changes during software development.

### Advantages

- Fast
- Distributed
- Reliable
- Supports branching and merging
- Maintains complete project history

---

# What is GitHub?

GitHub is a cloud-based platform that hosts Git repositories.

It provides:

- Remote repository storage
- Collaboration
- Code review
- Pull Requests
- CI/CD Integration
- Issue Tracking

---

# Git Architecture

```
Working Directory
        │
        ▼
   git add
        │
        ▼
Staging Area
        │
git commit
        ▼
Local Repository
        │
git push
        ▼
GitHub Repository
```

---

# Repository Created

```
DataEngineeringLab/
├── README.md
├── architecture/
├── datasets/
├── docker/
├── docs/
├── experiments/
└── scripts/
```

---

# Commands Learned

## Check Git Version

```bash
git --version
```

---

## Initialize Repository

```bash
git init
```

Creates a new Git repository in the current directory.

---

## Check Repository Status

```bash
git status
```

Shows:

- Modified files
- New files
- Deleted files
- Files ready for commit

---

## Add Files

### Single File

```bash
git add README.md
```

### All Files

```bash
git add .
```

Moves changes to the staging area.

---

## Commit Changes

```bash
git commit -m "Initial commit"
```

Creates a snapshot of the staged changes.

---

## Connect Remote Repository

```bash
git remote add origin <repository-url>
```

Example:

```bash
git remote add origin https://github.com/username/DataEngineeringLab.git
```

---

## Verify Remote

```bash
git remote -v
```

Displays configured remote repositories.

---

## Push to GitHub

```bash
git push -u origin main
```

Uploads commits to the remote repository.

---

# Git Workflow

```
Create File
      │
      ▼
git status
      │
      ▼
git add
      │
      ▼
git commit
      │
      ▼
git push
```

---

# Frequently Used Commands

| Command | Description |
|----------|-------------|
| `git status` | Check repository status |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit staged changes |
| `git push` | Push commits to GitHub |
| `git pull` | Download latest changes |
| `git log` | View commit history |
| `git diff` | View changes |
| `git remote -v` | View configured remotes |

---

# Key Learnings

- Git tracks project history.
- GitHub stores repositories remotely.
- Every commit represents a project snapshot.
- Files must be staged before committing.
- Local commits are not visible on GitHub until pushed.

---

# Common Mistakes

### Forgetting to Stage Files

Incorrect:

```bash
git commit -m "Update README"
```

Correct:

```bash
git add .
git commit -m "Update README"
```

---

### Forgetting to Push

After committing locally:

```bash
git push
```

Otherwise, GitHub will not reflect the latest changes.

---

# Interview Questions

### What is Git?

Git is a distributed version control system used to track changes in source code and manage software development.

---

### Difference between Git and GitHub?

| Git | GitHub |
|-----|---------|
| Version Control System | Cloud Hosting Platform |
| Runs locally | Runs on the cloud |
| Tracks changes | Stores Git repositories |

---

### What is a Commit?

A commit is a snapshot of the project's staged changes at a specific point in time.

---

### What is the Staging Area?

The staging area is an intermediate space where changes are prepared before creating a commit.

---

### Difference between git add and git commit?

| git add | git commit |
|----------|------------|
| Stages changes | Saves staged changes as a snapshot |

---

# Reflection

## What I Learned

- Initialized my first Git repository.
- Connected a local repository to GitHub.
- Understood the Git workflow.
- Created and pushed my first commits.

---

## Mistakes I Made

- Initially confused the staging area with committing.
- Needed to verify the remote repository configuration before pushing.

---

## Questions for Future Learning

- What is branching?
- What is merging?
- What is rebase?
- What is cherry-pick?
- How do Pull Requests work?

---

## Next Steps

- Learn Git branching.
- Learn merge conflicts.
- Understand Git workflows used in professional software development.
- Practice collaborative development using feature branches.