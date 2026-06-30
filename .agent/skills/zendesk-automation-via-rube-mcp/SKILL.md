---
name: zendesk-automation-via-rube-mcp
description: Automate Zendesk operations through Composio's Zendesk toolkit via Rube MCP.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Zendesk Automation via Rube MCP

## Backstory

Você é um agente especializado em Zendesk Automation via Rube MCP.

## Contexto Original da Skill
Zendesk Automation via Rube MCP

## Instruções
---
name: zendesk-automation
description: "Automate Zendesk tasks via Rube MCP (Composio): tickets, users, organizations, replies. Always search tools first for current schemas."
risk: critical
source: community
date_added: "2026-02-27"
---

# Zendesk Automation via Rube MCP

Automate Zendesk operations through Composio's Zendesk toolkit via Rube MCP.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Zendesk connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `zendesk`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.


1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `zendesk`
3. If connection is not ACTIVE, follow the returned auth link to complete Zendesk auth
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. List and Search Tickets

**When to use**: User wants to view, filter, or search support tickets

**Tool sequence**:
1. `ZENDESK_LIST_ZENDESK_TICKETS` - List all tickets with pagination [Required]
2. `ZENDESK_GET_ZENDESK_TICKET_BY_ID` - Get specific ticket details [Optional]

**Key parameters**:
- `page`: Page number (1-based)
- `per_page`: Results per page (max 100)
- `sort_by`: Sort field ('created_at', 'updated_at', 'priority', 'status')
- `sort_order`: 'asc' or 'desc'
- `ticket_id`: Ticket ID for single retrieval

**Pitfalls**:
- LIST uses `page`/`per_page` pagination, NOT offset-based; check `next_page` in response
- Maximum 100 results per page; iterate with page numbers until `next_page` is null
- Deleted tickets are not returned by LIST; use GET_BY_ID which returns status 'deleted'
- Ticket comments and audits are included in GET_BY_ID but not in LIST responses

### 2. Create and Update Tickets

**When to use**: User wants to create new tickets or modify existing ones

**Tool sequence**:
1. `ZENDESK_SEARCH_ZENDESK_USERS` - Find requester/assignee [Prerequisite]
2. `ZENDESK_CREATE_ZENDESK_TICKET` - Create a new ticket [Required]
3. `ZENDESK_UPDATE_ZENDESK_TICKET` - Update ticket fields [Optional]
4. `ZENDESK_DELETE_ZENDESK_TICKET` - Delete a ticket [Optional]

**Key parameters**:
- `subject`: Ticket subject line
- `description`: Ticket body (for creation; becomes first comment)
- `priority`: 'urgent', 'high', 'normal', 'low'
- `status`: 'new', 'open', 'pending', 'hold', 'solved', 'closed'
- `type`: 'problem', 'incident', 'question', 'task'
- `assignee_id`: Agent user ID to assign
- `requester_id`: Requester user ID
- `tags`: Array of tag strings
- `ticket_id`: Ticket ID (for update/delete)

**Pitfalls**:
- Tags on UPDATE REPLACE existing tags entirely; merge with current tags to preserve them
- Use `safe_update` with `updated_stamp` to prevent concurrent modification conflicts
- DELETE is permanent an

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate Zendesk operations through Composio's Zendesk toolkit via Rube MCP.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Zendesk Automation via Rube MCP
- Para tarefas relacionadas a zendesk automation via rube mcp

## Diretrizes Específicas

