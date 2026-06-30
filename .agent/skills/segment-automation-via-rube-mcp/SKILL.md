---
name: segment-automation-via-rube-mcp
description: Automate Segment customer data platform operations through Composio's Segment toolkit via Rube MCP.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Segment Automation via Rube MCP

## Backstory

Você é um agente especializado em Segment Automation via Rube MCP.

## Contexto Original da Skill
Segment Automation via Rube MCP

## Instruções
---
name: segment-automation
description: "Automate Segment tasks via Rube MCP (Composio): track events, identify users, manage groups, page views, aliases, batch operations. Always search tools first for current schemas."
risk: critical
source: community
date_added: "2026-02-27"
---

# Segment Automation via Rube MCP

Automate Segment customer data platform operations through Composio's Segment toolkit via Rube MCP.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Segment connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `segment`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.


1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `segment`
3. If connection is not ACTIVE, follow the returned auth link to complete Segment authentication
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. Track Events

**When to use**: User wants to send event data to Segment for downstream destinations

**Tool sequence**:
1. `SEGMENT_TRACK` - Send a single track event [Required]

**Key parameters**:
- `userId`: User identifier (required if no `anonymousId`)
- `anonymousId`: Anonymous identifier (required if no `userId`)
- `event`: Event name (e.g., 'Order Completed', 'Button Clicked')
- `properties`: Object with event-specific properties
- `timestamp`: ISO 8601 timestamp (optional; defaults to server time)
- `context`: Object with contextual metadata (IP, user agent, etc.)

**Pitfalls**:
- At least one of `userId` or `anonymousId` is required
- `event` name is required and should follow consistent naming conventions
- Properties are freeform objects; ensure consistent schema across events
- Timestamp must be ISO 8601 format (e.g., '2024-01-15T10:30:00Z')
- Events are processed asynchronously; successful API response means accepted, not delivered

### 2. Identify Users

**When to use**: User wants to associate traits with a user profile in Segment

**Tool sequence**:
1. `SEGMENT_IDENTIFY` - Set user traits and identity [Required]

**Key parameters**:
- `userId`: User identifier (required if no `anonymousId`)
- `anonymousId`: Anonymous identifier
- `traits`: Object with user properties (email, name, plan, etc.)
- `timestamp`: ISO 8601 timestamp
- `context`: Contextual metadata

**Pitfalls**:
- At least one of `userId` or `anonymousId` is required
- Traits are merged with existing traits, not replaced
- To remove a trait, set it to `null`
- Identify calls should be made before track calls for new users
- Avoid sending PII in traits unless destinations are configured for it

### 3. Batch Operations

**When to use**: User wants to send multiple events, identifies, or other calls in a single request

**Tool sequence**:
1. `SEGMENT_BATCH`

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate Segment customer data platform operations through Composio's Segment toolkit via Rube MCP.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Segment Automation via Rube MCP
- Para tarefas relacionadas a segment automation via rube mcp

## Diretrizes Específicas

