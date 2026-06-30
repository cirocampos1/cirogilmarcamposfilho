---
name: dropbox-automation-via-rube-mcp
description: Automate Dropbox operations including file upload/download, search, folder management, sharing links, batch operations, and metadata retrieval through Composio's Dropbox toolkit.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Dropbox Automation via Rube MCP

## Backstory

Você é um agente especializado em Dropbox Automation via Rube MCP.

## Contexto Original da Skill
Dropbox Automation via Rube MCP

## Instruções
---
name: dropbox-automation
description: "Automate Dropbox file management, sharing, search, uploads, downloads, and folder operations via Rube MCP (Composio). Always search tools first for current schemas."
risk: critical
source: community
date_added: "2026-02-27"
---

# Dropbox Automation via Rube MCP

Automate Dropbox operations including file upload/download, search, folder management, sharing links, batch operations, and metadata retrieval through Composio's Dropbox toolkit.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Dropbox connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `dropbox`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.

1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `dropbox`
3. If connection is not ACTIVE, follow the returned auth link to complete Dropbox OAuth
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. Search for Files and Folders

**When to use**: User wants to find files or folders by name, content, or type

**Tool sequence**:
1. `DROPBOX_SEARCH_FILE_OR_FOLDER` - Search by query string with optional path scope and filters [Required]
2. `DROPBOX_SEARCH_CONTINUE` - Paginate through additional results using cursor [Required if has_more]
3. `DROPBOX_GET_METADATA` - Validate and get canonical path for a search result [Optional]
4. `DROPBOX_READ_FILE` - Read file content to verify it is the intended document [Optional]

**Key parameters**:
- `query`: Search string (case-insensitive, 1+ non-whitespace characters)
- `options.path`: Scope search to a folder (e.g., `"/Documents"`); empty string for root
- `options.file_categories`: Filter by type (`"image"`, `"document"`, `"pdf"`, `"folder"`, etc.)
- `options.file_extensions`: Filter by extension (e.g., `["jpg", "png"]`)
- `options.filename_only`: Set `true` to match filenames only (not content)
- `options.max_results`: Results per page (default 100, max 1000)

**Pitfalls**:
- Search returns `has_more: true` with a `cursor` when more results exist; MUST continue to avoid silently missing matches
- Maximum 10,000 matches total across all pages of search + search_continue
- `DROPBOX_GET_METADATA` returned `path_display` may differ in casing from user input; always use the returned canonical path
- File content from `DROPBOX_READ_FILE` may be returned as base64-encoded `file_content_bytes`; decode before parsing

### 2. Upload and Download Files

**When to use**: User wants to upload files to Dropbox or download files from it

**Tool sequence**:
1. `DROPBOX_UPLOAD_FILE` - Upload a file to a specified path [Required for upload]
2. `DROPBOX_READ_FILE` - Download/read a file from Dropbox [Required for download]
3. `DROPBOX_DOWNLOAD_ZIP` - 

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate Dropbox operations including file upload/download, search, folder management, sharing links, batch operations, and metadata retrieval through Composio's Dropbox toolkit.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Dropbox Automation via Rube MCP
- Para tarefas relacionadas a dropbox automation via rube mcp

## Diretrizes Específicas

