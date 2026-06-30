---
name: monte-carlo-monitor-creation-skill
description: This skill teaches you to create Monte Carlo monitors correctly via MCP. Every creation tool runs in **dry-run mode** and returns monitors-as-code (MaC) YAML. No monitors are created directly -- the u
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Monte Carlo Monitor Creation Skill

## Backstory

Você é um agente especializado em Monte Carlo Monitor Creation Skill.

## Contexto Original da Skill
Monte Carlo Monitor Creation Skill

## Instruções
---
name: monte-carlo-monitor-creation
description: "Guides creation of Monte Carlo monitors via MCP tools, producing monitors-as-code YAML for CI/CD deployment."
category: data
risk: safe
source: community
source_repo: monte-carlo-data/mc-agent-toolkit
source_type: community
date_added: "2026-04-08"
author: monte-carlo-data
tags: [data-observability, monitoring, monte-carlo, monitors-as-code]
tools: [claude, cursor, codex]
---

# Monte Carlo Monitor Creation Skill

This skill teaches you to create Monte Carlo monitors correctly via MCP. Every creation tool runs in **dry-run mode** and returns monitors-as-code (MaC) YAML. No monitors are created directly -- the user applies the YAML via the Monte Carlo CLI or CI/CD.

Reference files live next to this skill file. **Use the Read tool** (not MCP resources) to access them:

- Metric monitor details: `references/metric-monitor.md` (relative to this file)
- Validation monitor details: `references/validation-monitor.md` (relative to this file)
- Custom SQL monitor details: `references/custom-sql-monitor.md` (relative to this file)
- Comparison monitor details: `references/comparison-monitor.md` (relative to this file)
- Table monitor details: `references/table-monitor.md` (relative to this file)

## When to activate this skill

Activate when the user:

- Asks to create, add, or set up a monitor (e.g. "add a monitor for...", "create a freshness check on...", "set up validation for...")
- Mentions monitoring a specific table, field, or metric
- Wants to check data quality rules or enforce data contracts
- Asks about monitoring options for a table or dataset
- Requests monitors-as-code YAML generation
- Wants to add monitoring after new transformation logic (when the prevent skill is not active)

## When NOT to activate this skill

Do not activate when the user is:

- Just querying data or exploring table contents
- Triaging or responding to active alerts (use the prevent skill's Workflow 3)
- Running impact assessments before code changes (use the prevent skill's Workflow 4)
- Asking about existing monitor configuration (use `getMonitors` directly)
- Editing or deleting existing monitors

---

## Available MCP tools

All tools are available via the `monte-carlo` MCP server.

| Tool                         | Purpose                                                    |
| ---------------------------- | ---------------------------------------------------------- |
| `testConnection`             | Verify auth and connectivity before starting               |
| `search`                     | Find tables/assets by name; use `include_fields` for columns |
| `getTable`                   | Schema, stats, metadata, domain membership, capabilities   |
| `getValidationPredicates`    | List available validation rule types for a warehouse       |
| `getDomains`                 | List MC domains (only needed if table has no domain info)  |
| `createMetricMonitorMac`     | Generate metric monitor YAML (dry-run)             

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

This skill teaches you to create Monte Carlo monitors correctly via MCP. Every creation tool runs in **dry-run mode** and returns monitors-as-code (MaC) YAML. No monitors are created directly -- the u

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Monte Carlo Monitor Creation Skill
- Para tarefas relacionadas a monte carlo monitor creation skill

## Diretrizes Específicas

