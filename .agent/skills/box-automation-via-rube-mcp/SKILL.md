---
name: box-automation-via-rube-mcp
description: Automate Box operations including file upload/download, content search, folder management, collaboration, metadata queries, and sign requests through Composio's Box toolkit.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Box Automation via Rube MCP

## Backstory

Você é um agente especializado em Box Automation via Rube MCP.

## Contexto Original da Skill
Box Automation via Rube MCP

## Instruções
---
name: box-automation
description: "Automate Box operations including file upload/download, content search, folder management, collaboration, metadata queries, and sign requests through Composio's Box toolkit."
risk: critical
source: community
date_added: "2026-02-27"
---

# Box Automation via Rube MCP

Automate Box operations including file upload/download, content search, folder management, collaboration, metadata queries, and sign requests through Composio's Box toolkit.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Box connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `box`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.

1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `box`
3. If connection is not ACTIVE, follow the returned auth link to complete Box OAuth
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. Upload and Download Files

**When to use**: User wants to upload files to Box or download files from it

**Tool sequence**:
1. `BOX_SEARCH_FOR_CONTENT` - Find the target folder if path is unknown [Prerequisite]
2. `BOX_GET_FOLDER_INFORMATION` - Verify folder exists and get folder_id [Prerequisite]
3. `BOX_LIST_ITEMS_IN_FOLDER` - Browse folder contents and discover file IDs [Optional]
4. `BOX_UPLOAD_FILE` - Upload a file to a specific folder [Required for upload]
5. `BOX_DOWNLOAD_FILE` - Download a file by file_id [Required for download]
6. `BOX_CREATE_ZIP_DOWNLOAD` - Bundle multiple files/folders into a zip [Optional]

**Key parameters**:
- `parent_id`: Folder ID for upload destination (use `"0"` for root folder)
- `file`: FileUploadable object with `s3key`, `mimetype`, and `name` for uploads
- `file_id`: Unique file identifier for downloads
- `version`: Optional file version ID for downloading specific versions
- `fields`: Comma-separated list of attributes to return

**Pitfalls**:
- Uploading to a folder with existing filenames can trigger conflict behavior; decide overwrite vs rename semantics
- Files over 50MB should use chunk upload APIs (not available via standard tools)
- The `attributes` part of upload must come before the `file` part or you get HTTP 400 with `metadata_after_file_contents`
- File IDs and folder IDs are numeric strings extractable from Box web app URLs (e.g., `https://*.app.box.com/files/123` gives file_id `"123"`)

### 2. Search and Browse Content

**When to use**: User wants to find files, folders, or web links by name, content, or metadata

**Tool sequence**:
1. `BOX_SEARCH_FOR_CONTENT` - Full-text search across files, folders, and web links [Required]
2. `BOX_LIST_ITEMS_IN_FOLDER` - Browse contents of a specific folder [Optional]
3. `BOX_GET_FILE_INFORMATION` - Get deta

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate Box operations including file upload/download, content search, folder management, collaboration, metadata queries, and sign requests through Composio's Box toolkit.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Box Automation via Rube MCP
- Para tarefas relacionadas a box automation via rube mcp

## Diretrizes Específicas

