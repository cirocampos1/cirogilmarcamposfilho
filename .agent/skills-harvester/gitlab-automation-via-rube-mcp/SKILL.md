---
name: gitlab-automation-via-rube-mcp
description: Automate GitLab operations including project management, issue tracking, merge request workflows, CI/CD pipeline monitoring, branch management, and user administration through Composio's GitLab toolki
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# GitLab Automation via Rube MCP

## Backstory

Você é um agente especializado em GitLab Automation via Rube MCP.

## Contexto Original da Skill
GitLab Automation via Rube MCP

## Instruções
---
name: gitlab-automation
description: "Automate GitLab project management, issues, merge requests, pipelines, branches, and user operations via Rube MCP (Composio). Always search tools first for current schemas."
risk: critical
source: community
date_added: "2026-02-27"
---

# GitLab Automation via Rube MCP

Automate GitLab operations including project management, issue tracking, merge request workflows, CI/CD pipeline monitoring, branch management, and user administration through Composio's GitLab toolkit.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active GitLab connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `gitlab`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.

1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `gitlab`
3. If connection is not ACTIVE, follow the returned auth link to complete GitLab OAuth
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. Manage Issues

**When to use**: User wants to create, update, list, or search issues in a GitLab project

**Tool sequence**:
1. `GITLAB_GET_PROJECTS` - Find the target project and get its ID [Prerequisite]
2. `GITLAB_LIST_PROJECT_ISSUES` - List and filter issues for a project [Required]
3. `GITLAB_CREATE_PROJECT_ISSUE` - Create a new issue [Required for create]
4. `GITLAB_UPDATE_PROJECT_ISSUE` - Update an existing issue (title, labels, state, assignees) [Required for update]
5. `GITLAB_LIST_PROJECT_USERS` - Find user IDs for assignment [Optional]

**Key parameters**:
- `id`: Project ID (integer) or URL-encoded path (e.g., `"my-group/my-project"`)
- `title`: Issue title (required for creation)
- `description`: Issue body text (max 1,048,576 characters)
- `labels`: Comma-separated label names (e.g., `"bug,critical"`)
- `add_labels` / `remove_labels`: Add or remove labels without replacing all
- `state`: Filter by `"all"`, `"opened"`, or `"closed"`
- `state_event`: `"close"` or `"reopen"` to change issue state
- `assignee_ids`: Array of user IDs; use `[0]` to unassign all
- `issue_iid`: Internal issue ID within the project (required for updates)
- `milestone`: Filter by milestone title
- `search`: Search in title and description
- `scope`: `"created_by_me"`, `"assigned_to_me"`, or `"all"`
- `page` / `per_page`: Pagination (default per_page: 20)

**Pitfalls**:
- `id` accepts either integer project ID or URL-encoded path; wrong IDs yield 4xx errors
- `issue_iid` is the project-internal ID (shown as #42), different from the global issue ID
- Labels in `labels` field replace ALL existing labels; use `add_labels`/`remove_labels` for incremental changes
- Setting `assignee_ids` to empty array does NOT unassign; use `[0]` instead
- `updated_at` field requires ad

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate GitLab operations including project management, issue tracking, merge request workflows, CI/CD pipeline monitoring, branch management, and user administration through Composio's GitLab toolki

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em GitLab Automation via Rube MCP
- Para tarefas relacionadas a gitlab automation via rube mcp

## Diretrizes Específicas

