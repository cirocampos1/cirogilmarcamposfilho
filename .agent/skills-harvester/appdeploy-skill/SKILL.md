---
name: appdeploy-skill
description: Deploy web apps to AppDeploy via HTTP API.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# AppDeploy Skill

## Backstory

Você é um agente especializado em AppDeploy Skill.

## Contexto Original da Skill
AppDeploy Skill

## Instruções
---
name: appdeploy
description: "Deploy web apps with backend APIs, database, and file storage. Use when the user asks to deploy or publish a website or web app and wants a public URL. Uses HTTP API via curl."
risk: safe
source: "AppDeploy (MIT)"
date_added: "2026-02-27"
---

# AppDeploy Skill

Deploy web apps to AppDeploy via HTTP API.

## When to Use This Skill

- Use when planning or building apps and web apps
- Use when deploying an app to a public URL
- Use when publishing a website or web app
- Use when the user says "deploy this", "make this live", or "give me a URL"
- Use when updating an already-deployed app

## Setup (First Time Only)

1. **Check for existing API key:**
   - Look for a `.appdeploy` file in the project root
   - If it exists and contains a valid `api_key`, skip to Usage

2. **If no API key exists, register and get one:**
   ```bash
   curl -X POST https://api-v2.appdeploy.ai/mcp/api-key \
     -H "Content-Type: application/json" \
     -d '{"client_name": "claude-code"}'
   ```

   Response:
   ```json
   {
     "api_key": "ak_...",
     "user_id": "agent-claude-code-a1b2c3d4",
     "created_at": 1234567890,
     "message": "Save this key securely - it cannot be retrieved later"
   }
   ```

3. **Save credentials to `.appdeploy`:**
   ```json
   {
     "api_key": "ak_...",
     "endpoint": "https://api-v2.appdeploy.ai/mcp"
   }
   ```

   Add `.appdeploy` to `.gitignore` if not already present.

## Usage

Make JSON-RPC calls to the MCP endpoint:

```bash
curl -X POST {endpoint} \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer {api_key}" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "{tool_name}",
      "arguments": { ... }
    }
  }'
```

## Workflow

1. **First, get deployment instructions:**
   Call `get_deploy_instructions` to understand constraints and requirements.

2. **Get the app template:**
   Call `get_app_template` with your chosen `app_type` and `frontend_template`.

3. **Deploy the app:**
   Call `deploy_app` with your app files. For new apps, set `app_id` to `null`.

4. **Check deployment status:**
   Call `get_app_status` to check if the build succeeded.

5. **View/manage your apps:**
   Use `get_apps` to list your deployed apps.

## Available Tools

### get_deploy_instructions

Use this when you are about to call deploy_app in order to get the deployment constraints and hard rules. You must call this tool before starting to generate any code. This tool returns instructions only and does not deploy anything.

**Parameters:**


### deploy_app

Use this when the user asks to deploy or publish a website or web app and wants a public URL.
Before generating files or calling this tool, you must call get_deploy_instructions and follow its constraints.

**Parameters:**
  - `app_id`: any (required) - existing app id to update, or null for new app
  - `app_type`: string (required) - app

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Deploy web apps to AppDeploy via HTTP API.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em AppDeploy Skill
- Para tarefas relacionadas a appdeploy skill

## Diretrizes Específicas

