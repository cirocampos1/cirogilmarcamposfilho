---
name: make-automation-via-rube-mcp
description: Automate Make (formerly Integromat) operations through Composio's Make toolkit via Rube MCP.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Make Automation via Rube MCP

## Backstory

Você é um agente especializado em Make Automation via Rube MCP.

## Contexto Original da Skill
Make Automation via Rube MCP

## Instruções
---
name: make-automation
description: "Automate Make (Integromat) tasks via Rube MCP (Composio): operations, enums, language and timezone lookups. Always search tools first for current schemas."
risk: critical
source: community
date_added: "2026-02-27"
---

# Make Automation via Rube MCP

Automate Make (formerly Integromat) operations through Composio's Make toolkit via Rube MCP.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Make connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `make`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.


1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `make`
3. If connection is not ACTIVE, follow the returned auth link to complete Make authentication
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. Get Operations Data

**When to use**: User wants to retrieve operation logs or usage data from Make scenarios

**Tool sequence**:
1. `MAKE_GET_OPERATIONS` - Retrieve operation records [Required]

**Key parameters**:
- Check current schema via RUBE_SEARCH_TOOLS for available filters
- May include date range, scenario ID, or status filters

**Pitfalls**:
- Operations data may be paginated; check for pagination tokens
- Date filters must match expected format from schema
- Large result sets should be filtered by date range or scenario

### 2. List Available Languages

**When to use**: User wants to see supported languages for Make scenarios or interfaces

**Tool sequence**:
1. `MAKE_LIST_ENUMS_LANGUAGES` - Get all supported language codes [Required]

**Key parameters**:
- No required parameters; returns complete language list

**Pitfalls**:
- Language codes follow standard locale format (e.g., 'en', 'fr', 'de')
- List is static and rarely changes; cache results when possible

### 3. List Available Timezones

**When to use**: User wants to see supported timezones for scheduling Make scenarios

**Tool sequence**:
1. `MAKE_LIST_ENUMS_TIMEZONES` - Get all supported timezone identifiers [Required]

**Key parameters**:
- No required parameters; returns complete timezone list

**Pitfalls**:
- Timezone identifiers use IANA format (e.g., 'America/New_York', 'Europe/London')
- List is static and rarely changes; cache results when possible
- Use these exact timezone strings when configuring scenario schedules

### 4. Scenario Configuration Lookup

**When to use**: User needs to configure scenarios with correct language and timezone values

**Tool sequence**:
1. `MAKE_LIST_ENUMS_LANGUAGES` - Get valid language codes [Required]
2. `MAKE_LIST_ENUMS_TIMEZONES` - Get valid timezone identifiers [Required]

**Key parameters**:
- No parameters needed for either call

**Pitfalls**:
- Always verify lang

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate Make (formerly Integromat) operations through Composio's Make toolkit via Rube MCP.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Make Automation via Rube MCP
- Para tarefas relacionadas a make automation via rube mcp

## Diretrizes Específicas

