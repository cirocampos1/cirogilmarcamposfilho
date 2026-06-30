---
name: supabase-automation-via-rube-mcp
description: Automate Supabase operations including database queries, table schema inspection, SQL execution, project and organization management, storage buckets, edge functions, and service health monitoring thr
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Supabase Automation via Rube MCP

## Backstory

Você é um agente especializado em Supabase Automation via Rube MCP.

## Contexto Original da Skill
Supabase Automation via Rube MCP

## Instruções
---
name: supabase-automation
description: "Automate Supabase database queries, table management, project administration, storage, edge functions, and SQL execution via Rube MCP (Composio). Always search tools first for current schemas."
risk: critical
source: community
date_added: "2026-02-27"
---

# Supabase Automation via Rube MCP

Automate Supabase operations including database queries, table schema inspection, SQL execution, project and organization management, storage buckets, edge functions, and service health monitoring through Composio's Supabase toolkit.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Supabase connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `supabase`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.

1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `supabase`
3. If connection is not ACTIVE, follow the returned auth link to complete Supabase authentication
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. Query and Manage Database Tables

**When to use**: User wants to read data from tables, inspect schemas, or perform CRUD operations

**Tool sequence**:
1. `SUPABASE_LIST_ALL_PROJECTS` - List projects to find the target project_ref [Prerequisite]
2. `SUPABASE_LIST_TABLES` - List all tables and views in the database [Prerequisite]
3. `SUPABASE_GET_TABLE_SCHEMAS` - Get detailed column types, constraints, and relationships [Prerequisite for writes]
4. `SUPABASE_SELECT_FROM_TABLE` - Query rows with filtering, sorting, and pagination [Required for reads]
5. `SUPABASE_BETA_RUN_SQL_QUERY` - Execute arbitrary SQL for complex queries, inserts, updates, or deletes [Required for writes]

**Key parameters for SELECT_FROM_TABLE**:
- `project_ref`: 20-character lowercase project reference
- `table`: Table or view name to query
- `select`: Comma-separated column list (supports nested selections and JSON paths like `profile->avatar_url`)
- `filters`: Array of filter objects with `column`, `operator`, `value`
- `order`: Sort expression like `created_at.desc`
- `limit`: Max rows to return (minimum 1)
- `offset`: Rows to skip for pagination

**PostgREST filter operators**:
- `eq`, `neq`: Equal / not equal
- `gt`, `gte`, `lt`, `lte`: Comparison operators
- `like`, `ilike`: Pattern matching (case-sensitive / insensitive)
- `is`: IS check (for null, true, false)
- `in`: In a list of values
- `cs`, `cd`: Contains / contained by (arrays)
- `fts`, `plfts`, `phfts`, `wfts`: Full-text search variants

**Key parameters for RUN_SQL_QUERY**:
- `ref`: Project reference (20 lowercase letters, pattern `^[a-z]{20}$`)
- `query`: Valid PostgreSQL SQL statement
- `read_only`: Boolean to force read-only transaction (saf

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate Supabase operations including database queries, table schema inspection, SQL execution, project and organization management, storage buckets, edge functions, and service health monitoring thr

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Supabase Automation via Rube MCP
- Para tarefas relacionadas a supabase automation via rube mcp

## Diretrizes Específicas

