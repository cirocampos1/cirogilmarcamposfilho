---
name: setup
description: > **Tip:** This skill works well with Sonnet. Run `/model sonnet` before invoking for faster generation.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Setup

## Backstory

Você é um agente especializado em Setup.

## Contexto Original da Skill
Setup

## Instruções
---
name: monte-carlo-validation-notebook
description: "Generates SQL validation notebooks for dbt PR changes with before/after comparison queries."
category: data
risk: safe
source: community
source_repo: monte-carlo-data/mc-agent-toolkit
source_type: community
date_added: "2026-04-08"
author: monte-carlo-data
tags: [data-observability, validation, dbt, monte-carlo, sql-notebook]
tools: [claude, cursor, codex]
---

> **Tip:** This skill works well with Sonnet. Run `/model sonnet` before invoking for faster generation.

Generate a SQL Notebook with validation queries for dbt changes.

**Arguments:** $ARGUMENTS

Parse the arguments:
- **Target** (required): first argument — a GitHub PR URL or local dbt repo path
- **MC Base URL** (optional): `--mc-base-url <URL>` — defaults to `https://getmontecarlo.com`
- **Models** (optional): `--models <model1,model2,...>` — comma-separated list of model filenames (without `.sql` extension) to generate queries for. Only these models will be included. By default, all changed models are included up to a maximum of 10.

---

# Setup

**Prerequisites:**
- **`gh`** (GitHub CLI) — required for PR mode. Must be authenticated (`gh auth status`).
- **`python3`** — required for helper scripts.
- **`pyyaml`** — install with `pip3 install pyyaml` (or `pip install pyyaml`, `uv pip install pyyaml`, etc.)

**Note:** Generated SQL uses ANSI-compatible syntax that works across Snowflake, BigQuery, Redshift, and Athena. Minor adjustments may be needed for specific warehouse quirks.

This skill includes two helper scripts in `${CLAUDE_PLUGIN_ROOT}/skills/monte-carlo-validation-notebook/scripts/`:

- **`resolve_dbt_schema.py`** - Resolves dbt model output schemas from `dbt_project.yml` routing rules and model config overrides.
- **`generate_notebook_url.py`** - Encodes notebook YAML into a base64 import URL and opens it in the browser.

# Mode Detection

Auto-detect mode from the target argument:
- If target looks like a URL (contains `://` or `github.com`) -> **PR mode**
- If target is a path (`.`, `/path/to/repo`, relative path) -> **Local mode**

---

# Context

This command generates a SQL Notebook containing validation queries for dbt changes. The notebook can be opened in the MC Bridge SQL Notebook interface for interactive validation.

The output is an import URL that opens directly in the notebook interface:
```
<MC_BASE_URL>/notebooks/import#<base64-encoded-yaml>
```

**Key Features:**
- **Database Parameters**: Two `text` parameters (`prod_db` and `dev_db`) for selecting databases
- **Schema Inference**: Automatically infers schema per model from `dbt_project.yml` and model configs
- **Single-table queries**: Basic validation queries using `{{prod_db}}.<SCHEMA>.<TABLE>`
- **Comparison queries**: Before/after queries comparing `{{prod_db}}` vs `{{dev_db}}`
- **Flexible usage**: Users can set both parameters to the same database for single-database analysis

# Notebook YAML Spec Reference

Key structure:
```yaml
version: 1

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

> **Tip:** This skill works well with Sonnet. Run `/model sonnet` before invoking for faster generation.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Setup
- Para tarefas relacionadas a setup

## Diretrizes Específicas

