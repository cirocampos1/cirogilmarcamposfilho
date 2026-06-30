---
name: pagerduty-automation-via-rube-mcp
description: Automate PagerDuty incident management and operations through Composio's PagerDuty toolkit via Rube MCP.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# PagerDuty Automation via Rube MCP

## Backstory

Você é um agente especializado em PagerDuty Automation via Rube MCP.

## Contexto Original da Skill
PagerDuty Automation via Rube MCP

## Instruções
---
name: pagerduty-automation
description: "Automate PagerDuty tasks via Rube MCP (Composio): manage incidents, services, schedules, escalation policies, and on-call rotations. Always search tools first for current schemas."
risk: critical
source: community
date_added: "2026-02-27"
---

# PagerDuty Automation via Rube MCP

Automate PagerDuty incident management and operations through Composio's PagerDuty toolkit via Rube MCP.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active PagerDuty connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `pagerduty`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.


1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `pagerduty`
3. If connection is not ACTIVE, follow the returned auth link to complete PagerDuty authentication
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. Manage Incidents

**When to use**: User wants to create, update, acknowledge, or resolve incidents

**Tool sequence**:
1. `PAGERDUTY_FETCH_INCIDENT_LIST` - List incidents with filters [Required]
2. `PAGERDUTY_RETRIEVE_INCIDENT_BY_INCIDENT_ID` - Get specific incident details [Optional]
3. `PAGERDUTY_CREATE_INCIDENT_RECORD` - Create a new incident [Optional]
4. `PAGERDUTY_UPDATE_INCIDENT_BY_ID` - Update incident status or assignment [Optional]
5. `PAGERDUTY_POST_INCIDENT_NOTE_USING_ID` - Add a note to an incident [Optional]
6. `PAGERDUTY_SNOOZE_INCIDENT_BY_DURATION` - Snooze an incident for a period [Optional]

**Key parameters**:
- `statuses[]`: Filter by status ('triggered', 'acknowledged', 'resolved')
- `service_ids[]`: Filter by service IDs
- `urgencies[]`: Filter by urgency ('high', 'low')
- `title`: Incident title (for creation)
- `service`: Service object with `id` and `type` (for creation)
- `status`: New status for update operations

**Pitfalls**:
- Incident creation requires a `service` object with both `id` and `type: 'service_reference'`
- Status transitions follow: triggered -> acknowledged -> resolved
- Cannot transition from resolved back to triggered directly
- `PAGERDUTY_UPDATE_INCIDENT_BY_ID` requires the incident ID as a path parameter
- Snooze duration is in seconds; the incident re-triggers after the snooze period

### 2. Inspect Incident Alerts and Analytics

**When to use**: User wants to review alerts within an incident or analyze incident metrics

**Tool sequence**:
1. `PAGERDUTY_GET_ALERTS_BY_INCIDENT_ID` - List alerts for an incident [Required]
2. `PAGERDUTY_GET_INCIDENT_ALERT_DETAILS` - Get details of a specific alert [Optional]
3. `PAGERDUTY_FETCH_INCIDENT_ANALYTICS_BY_ID` - Get incident analytics/metrics [Optional]

**Key parameters**:
- `incident_id`: The incident ID
- `alert_id`: Spec

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate PagerDuty incident management and operations through Composio's PagerDuty toolkit via Rube MCP.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em PagerDuty Automation via Rube MCP
- Para tarefas relacionadas a pagerduty automation via rube mcp

## Diretrizes Específicas

