---
name: calendly-automation-via-rube-mcp
description: Automate Calendly operations including event listing, invitee management, scheduling link creation, availability queries, and organization administration through Composio's Calendly toolkit.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Calendly Automation via Rube MCP

## Backstory

Você é um agente especializado em Calendly Automation via Rube MCP.

## Contexto Original da Skill
Calendly Automation via Rube MCP

## Instruções
---
name: calendly-automation
description: "Automate Calendly scheduling, event management, invitee tracking, availability checks, and organization administration via Rube MCP (Composio). Always search tools first for current schemas."
risk: critical
source: community
date_added: "2026-02-27"
---

# Calendly Automation via Rube MCP

Automate Calendly operations including event listing, invitee management, scheduling link creation, availability queries, and organization administration through Composio's Calendly toolkit.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Calendly connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `calendly`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas
- Many operations require the user's Calendly URI, obtained via `CALENDLY_GET_CURRENT_USER`

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.

1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `calendly`
3. If connection is not ACTIVE, follow the returned auth link to complete Calendly OAuth
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. List and View Scheduled Events

**When to use**: User wants to see their upcoming, past, or filtered Calendly events

**Tool sequence**:
1. `CALENDLY_GET_CURRENT_USER` - Get authenticated user URI and organization URI [Prerequisite]
2. `CALENDLY_LIST_EVENTS` - List events scoped by user, organization, or group [Required]
3. `CALENDLY_GET_EVENT` - Get detailed info for a specific event by UUID [Optional]

**Key parameters**:
- `user`: Full Calendly API URI (e.g., `https://api.calendly.com/users/{uuid}`) - NOT `"me"`
- `organization`: Full organization URI for org-scoped queries
- `status`: `"active"` or `"canceled"`
- `min_start_time` / `max_start_time`: UTC timestamps (e.g., `2024-01-01T00:00:00.000000Z`)
- `invitee_email`: Filter events by invitee email (filter only, not a scope)
- `sort`: `"start_time:asc"` or `"start_time:desc"`
- `count`: Results per page (default 20)
- `page_token`: Pagination token from previous response

**Pitfalls**:
- Exactly ONE of `user`, `organization`, or `group` must be provided - omitting or combining scopes fails
- The `user` parameter requires the full API URI, not `"me"` - use `CALENDLY_GET_CURRENT_USER` first
- `invitee_email` is a filter, not a scope; you still need one of user/organization/group
- Pagination uses `count` + `page_token`; loop until `page_token` is absent for complete results
- Admin rights may be needed for organization or group scope queries

### 2. Manage Event Invitees

**When to use**: User wants to see who is booked for events or get invitee details

**Tool sequence**:
1. `CALENDLY_LIST_EVENTS` - Find the target event(s) [Prerequisite]
2. `CALENDLY_LIST_EVENT_INVITEES` - List all invite

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate Calendly operations including event listing, invitee management, scheduling link creation, availability queries, and organization administration through Composio's Calendly toolkit.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Calendly Automation via Rube MCP
- Para tarefas relacionadas a calendly automation via rube mcp

## Diretrizes Específicas

