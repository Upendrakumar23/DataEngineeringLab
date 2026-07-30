# Day 07 - Local AI Development Environment (Ollama + Continue + VS Code)

**Project:** DataEngineeringLab
**Date:** 22 July 2026

---

# Objective

Replace cloud-based AI coding assistants (limited tokens) with a fully local AI coding environment using Ollama and VS Code.

---

# Architecture

```
                     Windows 11
                          │
                Ollama (Local LLM Server)
                          │
             qwen2.5-coder:7b (4.7 GB)
                          │
                  HTTP API (localhost:11434)
                          │
                     Continue Extension
                          │
                     VS Code (WSL)
                          │
               DataEngineeringLab Project
                          │
               Python • PostgreSQL • Docker
```

---

# System Configuration

| Component | Details |
|-----------|---------|
| OS | Windows 11 |
| Development Environment | WSL2 Ubuntu |
| RAM | 16 GB |
| WSL Memory | 12 GB |
| Swap | 8 GB |
| CPU | Intel i7-11390H |
| GPU | NVIDIA MX450 (2 GB) |
| IDE | Visual Studio Code |

---

# WSL Optimization

Created:

```
C:\Users\upend\.wslconfig
```

Configuration:

```ini
[wsl2]
memory=12GB
processors=4
swap=8GB
localhostForwarding=true
```

Restarted WSL:

```powershell
wsl --shutdown
```

Verified:

```bash
free -h
```

Output:

```
Memory : ~11 GB
Swap   : 8 GB
```

---

# Ollama Installation

Installed Ollama for Windows.

Verification:

```powershell
ollama --version
```

Example Output:

```
ollama version 0.32.1
```

---

# Installed Local Model

Downloaded coding model:

```powershell
ollama pull qwen2.5-coder:7b
```

Model Size:

```
4.7 GB
```

Verification:

```powershell
ollama list
```

Output:

```
qwen2.5-coder:7b
```

---

# Testing Ollama

Started interactive session:

```powershell
ollama run qwen2.5-coder:7b
```

Example Prompt:

```
Write a Python ETL to load CSV into PostgreSQL.
```

Result:

- Model generated Python code successfully.

---

# VS Code Extensions

## Installed Extensions

| Extension | Purpose |
|-----------|----------|
| Continue | AI Assistant |
| Python | Python Development |
| Pylance | IntelliSense |
| Debugpy | Debugging |
| Python Environments | Environment Management |
| GitLens | Git Integration |
| SQLTools | Database Support |
| Docker Containers | Docker |
| Remote WSL | WSL Development |
| Remote Containers | Containers |
| YAML | YAML Support |
| Rainbow CSV | CSV Visualization |
| Markdown All in One | Documentation |
| Material Icon Theme | Icons |
| Error Lens | Inline Errors |
| Even Better TOML | TOML Support |
| Jupyter | Notebook Support |
| PowerShell | Windows Terminal |

---

# Continue Configuration

Continue automatically detected:

```
qwen2.5-coder:7b
```

Provider:

```
Ollama
```

Connection:

```
http://localhost:11434
```

No API key required.

---

# Workspace Setup

Always open project from WSL.

Recommended:

```bash
cd /mnt/d/Projects/DataEngineeringLab

code .
```

Verified Working Directory:

```bash
pwd
```

Output:

```
/mnt/d/Projects/DataEngineeringLab
```

---

# Continue Usage

## Chat Mode (Recommended)

Use context provider.

Example:

```
@database.py

Explain this module.
```

Example:

```
@test_logger.py

Review this test file.
```

Example:

```
@src

Suggest production improvements.
```

---

# Agent Mode

Observation:

Agent mode generated tool calls such as:

```
ls

file_content

file_glob_search

code_review
```

However, Continue 2.0 did not execute these tool calls correctly in the current configuration.

Current Recommendation:

Use **Chat Mode + Context Providers (@)** for daily development.

---

# AI Prompt Examples

## Explain

```
@database.py

Explain this module.
```

---

## Review

```
@src

Review this module like a Senior Python Data Engineer.
```

---

## Optimize

```
@load.py

Suggest performance improvements.
```

---

## Testing

```
@tests

Review existing unit tests.
Suggest missing test cases.
```

---

## Documentation

```
@README.md

Update documentation based on recent changes.
```

---

# AI Workflow

Recommended workflow:

```
Read Code
        ↓
Understand Code
        ↓
Review Suggestions
        ↓
Accept or Reject
        ↓
Implement
        ↓
Test
```

Avoid blindly accepting AI-generated code.

---

# Lessons Learned

✔ Local AI eliminates API costs.

✔ Local AI has no token limitations.

✔ Context providers (@file) produce better results than generic prompts.

✔ AI suggestions must always be reviewed.

✔ Continue Chat Mode is stable and effective.

✔ Agent Mode requires additional configuration before production use.

---

# Future Improvements

- Configure MCP (Model Context Protocol)
- PostgreSQL Integration
- Docker Integration
- Git Integration
- AI Prompt Library
- Project-specific AI Rules
- Black Formatter
- Ruff Linter
- Pytest Integration
- Pre-commit Hooks

---

# Outcome

Successfully built a local AI-assisted development environment.

Current Stack:

```
Windows 11
        │
WSL2 Ubuntu
        │
VS Code
        │
Continue
        │
Ollama
        │
qwen2.5-coder:7b
        │
DataEngineeringLab
```

The environment is now ready to assist in developing production-style Python ETL pipelines, PostgreSQL integrations, Docker workflows, and future technologies such as dbt, PySpark, Airflow, and Kafka.
