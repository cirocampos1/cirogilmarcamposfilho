---
name: freshdesk-automation-via-rube-mcp
description: Automate Freshdesk customer support workflows including ticket management, contact and company operations, notes, replies, and ticket search through Composio's Freshdesk toolkit.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Freshdesk Automation via Rube MCP

## Backstory

Você é um agente especializado em Freshdesk Automation via Rube MCP.

## Contexto Original da Skill
Freshdesk Automation via Rube MCP

## Instruções
---
name: freshdesk-automation
description: "Automate Freshdesk helpdesk operations including tickets, contacts, companies, notes, and replies via Rube MCP (Composio). Always search tools first for current schemas."
risk: critical
source: community
date_added: "2026-02-27"
---

# Freshdesk Automation via Rube MCP

Automate Freshdesk customer support workflows including ticket management, contact and company operations, notes, replies, and ticket search through Composio's Freshdesk toolkit.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Freshdesk connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `freshdesk`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.

1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `freshdesk`
3. If connection is not ACTIVE, follow the returned auth link to complete Freshdesk authentication
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. Create and Manage Tickets

**When to use**: User wants to create a new support ticket, update an existing ticket, or view ticket details.

**Tool sequence**:
1. `FRESHDESK_SEARCH_CONTACTS` - Find requester by email to get requester_id [Optional]
2. `FRESHDESK_LIST_TICKET_FIELDS` - Check available custom fields and statuses [Optional]
3. `FRESHDESK_CREATE_TICKET` - Create a new ticket with subject, description, requester info [Required]
4. `FRESHDESK_UPDATE_TICKET` - Modify ticket status, priority, assignee, or other fields [Optional]
5. `FRESHDESK_VIEW_TICKET` - Retrieve full ticket details by ID [Optional]

**Key parameters for FRESHDESK_CREATE_TICKET**:
- `subject`: Ticket subject (required)
- `description`: HTML content of the ticket (required)
- `email`: Requester email (at least one requester identifier required)
- `requester_id`: User ID of requester (alternative to email)
- `status`: 2=Open, 3=Pending, 4=Resolved, 5=Closed (default 2)
- `priority`: 1=Low, 2=Medium, 3=High, 4=Urgent (default 1)
- `source`: 1=Email, 2=Portal, 3=Phone, 7=Chat (default 2)
- `responder_id`: Agent ID to assign the ticket to
- `group_id`: Group to assign the ticket to
- `tags`: Array of tag strings
- `custom_fields`: Object with `cf_<field_name>` keys

**Pitfalls**:
- At least one requester identifier is required: `requester_id`, `email`, `phone`, `facebook_id`, `twitter_id`, or `unique_external_id`
- If `phone` is provided without `email`, then `name` becomes mandatory
- `description` supports HTML formatting
- `attachments` field expects multipart/form-data format, not file paths or URLs
- Custom field keys must be prefixed with `cf_` (e.g., `cf_reference_number`)
- Status and priority are integers, not strings

### 2. Search and Filter Tickets

**When to use**: User

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate Freshdesk customer support workflows including ticket management, contact and company operations, notes, replies, and ticket search through Composio's Freshdesk toolkit.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Freshdesk Automation via Rube MCP
- Para tarefas relacionadas a freshdesk automation via rube mcp

## Diretrizes Específicas

