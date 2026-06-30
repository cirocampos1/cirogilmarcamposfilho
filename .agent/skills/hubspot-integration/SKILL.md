---
name: hubspot-integration
description: Expert patterns for HubSpot CRM integration including OAuth authentication, CRM objects, associations, batch operations, webhooks, and custom objects. Covers Node.js and Python SDKs.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# HubSpot Integration

## Backstory

Você é um agente especializado em HubSpot Integration.

## Contexto Original da Skill
HubSpot Integration

## Instruções
---
name: hubspot-integration
description: Expert patterns for HubSpot CRM integration including OAuth
  authentication, CRM objects, associations, batch operations, webhooks, and
  custom objects. Covers Node.js and Python SDKs.
risk: unknown
source: vibeship-spawner-skills (Apache 2.0)
date_added: 2026-02-27
---

# HubSpot Integration

Expert patterns for HubSpot CRM integration including OAuth authentication,
CRM objects, associations, batch operations, webhooks, and custom objects.
Covers Node.js and Python SDKs.

## Patterns

### OAuth 2.0 Authentication

Secure authentication for public apps

**When to use**: Building public app or multi-account integration

### Template

// OAuth 2.0 flow for HubSpot
import { Client } from "@hubspot/api-client";

// Environment variables
const CLIENT_ID = process.env.HUBSPOT_CLIENT_ID;
const CLIENT_SECRET = process.env.HUBSPOT_CLIENT_SECRET;
const REDIRECT_URI = process.env.HUBSPOT_REDIRECT_URI;
const SCOPES = "crm.objects.contacts.read crm.objects.contacts.write";

// Step 1: Generate authorization URL
function getAuthUrl(): string {
  const authUrl = new URL("https://app.hubspot.com/oauth/authorize");
  authUrl.searchParams.set("client_id", CLIENT_ID);
  authUrl.searchParams.set("redirect_uri", REDIRECT_URI);
  authUrl.searchParams.set("scope", SCOPES);
  return authUrl.toString();
}

// Step 2: Handle OAuth callback
async function handleOAuthCallback(code: string) {
  const response = await fetch("https://api.hubapi.com/oauth/v1/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "authorization_code",
      client_id: CLIENT_ID,
      client_secret: CLIENT_SECRET,
      redirect_uri: REDIRECT_URI,
      code: code,
    }),
  });

  const tokens = await response.json();
  // {
  //   access_token: "xxx",
  //   refresh_token: "xxx",
  //   expires_in: 1800  // 30 minutes
  // }

  // Store tokens securely
  await storeTokens(tokens);

  return tokens;
}

// Step 3: Refresh access token (before expiry)
async function refreshAccessToken(refreshToken: string) {
  const response = await fetch("https://api.hubapi.com/oauth/v1/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "refresh_token",
      client_id: CLIENT_ID,
      client_secret: CLIENT_SECRET,
      refresh_token: refreshToken,
    }),
  });

  return response.json();
}

// Step 4: Create authenticated client
function createClient(accessToken: string): Client {
  const hubspotClient = new Client({ accessToken });
  return hubspotClient;
}

### Notes

- Access tokens expire in 30 minutes
- Refresh tokens before expiry
- Store refresh tokens securely
- Rotate tokens every 6 months

### Private App Token

Authentication for single-account integrations

**When to use**: Building internal integration for one HubSpot account

### Template

// Private App Token

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Expert patterns for HubSpot CRM integration including OAuth authentication, CRM objects, associations, batch operations, webhooks, and custom objects. Covers Node.js and Python SDKs.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em HubSpot Integration
- Para tarefas relacionadas a hubspot integration

## Diretrizes Específicas

