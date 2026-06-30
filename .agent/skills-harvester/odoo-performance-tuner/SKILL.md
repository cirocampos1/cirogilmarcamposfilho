---
name: odoo-performance-tuner
description: This skill helps diagnose and resolve Odoo performance problems — from slow page loads and database bottlenecks to worker misconfiguration and memory bloat. It covers PostgreSQL query tuning, Odoo wor
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Odoo Performance Tuner

## Backstory

Você é um agente especializado em Odoo Performance Tuner.

## Contexto Original da Skill
Odoo Performance Tuner

## Instruções
---
name: odoo-performance-tuner
description: "Expert guide for diagnosing and fixing Odoo performance issues: slow queries, worker configuration, memory limits, PostgreSQL tuning, and profiling tools."
risk: safe
source: "self"
---

# Odoo Performance Tuner

## Overview

This skill helps diagnose and resolve Odoo performance problems — from slow page loads and database bottlenecks to worker misconfiguration and memory bloat. It covers PostgreSQL query tuning, Odoo worker settings, and built-in profiling tools.

## When to Use This Skill

- Odoo is slow in production (slow page loads, timeouts).
- Getting `MemoryError` or `Worker timeout` errors in logs.
- Diagnosing a slow database query using Odoo's profiler.
- Tuning `odoo.conf` for a specific server spec.

## How It Works

1. **Activate**: Mention `@odoo-performance-tuner` and describe your performance issue.
2. **Diagnose**: Share relevant log lines or config and receive a root cause analysis.
3. **Fix**: Get exact configuration changes with explanations.

## Examples

### Example 1: Recommended Worker Configuration

```ini
# odoo.conf — tuned for a 4-core, 8GB RAM server

workers = 9                   # (CPU_cores × 2) + 1 — never set to 0 in production
max_cron_threads = 2          # background cron jobs; keep ≤ 2 to preserve user-facing capacity
limit_memory_soft = 1610612736  # 1.5 GB — worker is recycled gracefully after this
limit_memory_hard = 2147483648  # 2.0 GB — worker is killed immediately; prevents OOM crashes
limit_time_cpu = 600          # max CPU seconds per request
limit_time_real = 1200        # max wall-clock seconds per request
limit_request = 8192          # max requests before worker recycles (prevents memory leaks)
```

### Example 2: Find Slow Queries with PostgreSQL

```sql
-- Step 1: Enable pg_stat_statements extension (run once as postgres superuser)
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Step 2: Also add to postgresql.conf and reload:
-- shared_preload_libraries = 'pg_stat_statements'
-- log_min_duration_statement = 1000   -- log queries taking > 1 second

-- Step 3: Find the top 10 slowest average queries
SELECT
    LEFT(query, 100) AS query_snippet,
    round(mean_exec_time::numeric, 2) AS avg_ms,
    calls,
    round(total_exec_time::numeric, 2) AS total_ms
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- Step 4: Check for missing indexes causing full table scans
SELECT schemaname, tablename, attname, n_distinct, correlation
FROM pg_stats
WHERE tablename = 'sale_order_line'
  AND correlation < 0.5   -- low correlation = poor index efficiency
ORDER BY n_distinct DESC;
```

### Example 3: Use Odoo's Built-In Profiler

```text
Prerequisites: Run Odoo with ?debug=1 in the URL to enable debug mode.

Menu: Settings → Technical → Profiling

Steps:
  1. Click "Enable Profiling" — set a duration (e.g., 60 seconds)
  2. Navigate to and reproduce the slow action
  3. Return to Settings → Technical → Profiling → View Results

What to look 

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

This skill helps diagnose and resolve Odoo performance problems — from slow page loads and database bottlenecks to worker misconfiguration and memory bloat. It covers PostgreSQL query tuning, Odoo wor

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Odoo Performance Tuner
- Para tarefas relacionadas a odoo performance tuner

## Diretrizes Específicas

