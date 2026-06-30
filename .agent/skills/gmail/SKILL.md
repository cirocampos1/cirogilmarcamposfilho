---
name: gmail
description: Lightweight Gmail integration with standalone OAuth authentication. No MCP server required.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Gmail

## Backstory

Você é um agente especializado em Gmail.

## Contexto Original da Skill
Gmail

## Instruções
---
name: gmail-automation
description: "Lightweight Gmail integration with standalone OAuth authentication. No MCP server required."
license: Apache-2.0
risk: critical
source: community
metadata:
  author: sanjay3290
  version: "1.0"
---

# Gmail

Lightweight Gmail integration with standalone OAuth authentication. No MCP server required.

> **⚠️ Requires Google Workspace account.** Personal Gmail accounts are not supported.

## When to Use

- You need to search, read, or send Gmail messages from the command line without an MCP server.
- You are automating inbox workflows for a Google Workspace account.
- You want a lightweight Gmail integration backed by standalone OAuth scripts.

## First-Time Setup

Authenticate with Google (opens browser):
```bash
python scripts/auth.py login
```

Check authentication status:
```bash
python scripts/auth.py status
```

Logout when needed:
```bash
python scripts/auth.py logout
```

## Commands

All operations via `scripts/gmail.py`. Auto-authenticates on first use if not logged in.

### Search Emails

```bash
# Search with Gmail query syntax
python scripts/gmail.py search "from:someone@example.com is:unread"

# Search recent emails (no query returns all)
python scripts/gmail.py search --limit 20

# Filter by label
python scripts/gmail.py search --label INBOX --limit 10

# Include spam and trash
python scripts/gmail.py search "subject:important" --include-spam-trash
```

### Read Email Content

```bash
# Get full message content
python scripts/gmail.py get MESSAGE_ID

# Get just metadata (headers)
python scripts/gmail.py get MESSAGE_ID --format metadata

# Get minimal response (IDs only)
python scripts/gmail.py get MESSAGE_ID --format minimal
```

### Send Emails

```bash
# Send a simple email
python scripts/gmail.py send --to "user@example.com" --subject "Hello" --body "Message body"

# Send with CC and BCC
python scripts/gmail.py send --to "user@example.com" --cc "cc@example.com" --bcc "bcc@example.com" \
  --subject "Team Update" --body "Update message"

# Send from an alias (must be configured in Gmail settings)
python scripts/gmail.py send --to "user@example.com" --subject "Hello" --body "Message" \
  --from "Mile9 Accounts <accounts@mile9.io>"

# Send HTML email
python scripts/gmail.py send --to "user@example.com" --subject "HTML Email" \
  --body "<h1>Hello</h1><p>HTML content</p>" --html
```

### Draft Management

```bash
# Create a draft
python scripts/gmail.py create-draft --to "user@example.com" --subject "Draft Subject" \
  --body "Draft content"

# Send an existing draft
python scripts/gmail.py send-draft DRAFT_ID
```

### Modify Messages (Labels)

```bash
# Mark as read (remove UNREAD label)
python scripts/gmail.py modify MESSAGE_ID --remove-label UNREAD

# Mark as unread
python scripts/gmail.py modify MESSAGE_ID --add-label UNREAD

# Archive (remove from INBOX)
python scripts/gmail.py modify MESSAGE_ID --remove-label INBOX

# Star a message
python scripts/gmail.py modify MESSAGE_ID --add-label STA

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Lightweight Gmail integration with standalone OAuth authentication. No MCP server required.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Gmail
- Para tarefas relacionadas a gmail

## Diretrizes Específicas

