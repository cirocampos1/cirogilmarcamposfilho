---
name: azure-postgresql-for-typescript-node-postgres
description: Connect to Azure Database for PostgreSQL Flexible Server using the `pg` (node-postgres) package with support for password and Microsoft Entra ID (passwordless) authentication.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure PostgreSQL for TypeScript (node-postgres)

## Backstory

Você é um agente especializado em Azure PostgreSQL for TypeScript (node-postgres).

## Contexto Original da Skill
Azure PostgreSQL for TypeScript (node-postgres)

## Instruções
---
name: azure-postgres-ts
description: Connect to Azure Database for PostgreSQL Flexible Server from Node.js/TypeScript using the pg (node-postgres) package.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure PostgreSQL for TypeScript (node-postgres)

Connect to Azure Database for PostgreSQL Flexible Server using the `pg` (node-postgres) package with support for password and Microsoft Entra ID (passwordless) authentication.

## Installation

```bash
npm install pg @azure/identity
npm install -D @types/pg
```

## Environment Variables

```bash
# Required
AZURE_POSTGRESQL_HOST=<server>.postgres.database.azure.com
AZURE_POSTGRESQL_DATABASE=<database>
AZURE_POSTGRESQL_PORT=5432

# For password authentication
AZURE_POSTGRESQL_USER=<username>
AZURE_POSTGRESQL_PASSWORD=<password>

# For Entra ID authentication
AZURE_POSTGRESQL_USER=<entra-user>@<server>   # e.g., user@contoso.com
AZURE_POSTGRESQL_CLIENTID=<managed-identity-client-id>  # For user-assigned identity
```

## Authentication

### Option 1: Password Authentication

```typescript
import { Client, Pool } from "pg";

const client = new Client({
  host: process.env.AZURE_POSTGRESQL_HOST,
  database: process.env.AZURE_POSTGRESQL_DATABASE,
  user: process.env.AZURE_POSTGRESQL_USER,
  password: process.env.AZURE_POSTGRESQL_PASSWORD,
  port: Number(process.env.AZURE_POSTGRESQL_PORT) || 5432,
  ssl: { rejectUnauthorized: true }  // Required for Azure
});

await client.connect();
```

### Option 2: Microsoft Entra ID (Passwordless) - Recommended

```typescript
import { Client, Pool } from "pg";
import { DefaultAzureCredential } from "@azure/identity";

// For system-assigned managed identity
const credential = new DefaultAzureCredential();

// For user-assigned managed identity
// const credential = new DefaultAzureCredential({
//   managedIdentityClientId: process.env.AZURE_POSTGRESQL_CLIENTID
// });

// Acquire access token for Azure PostgreSQL
const tokenResponse = await credential.getToken(
  "https://ossrdbms-aad.database.windows.net/.default"
);

const client = new Client({
  host: process.env.AZURE_POSTGRESQL_HOST,
  database: process.env.AZURE_POSTGRESQL_DATABASE,
  user: process.env.AZURE_POSTGRESQL_USER,  // Entra ID user
  password: tokenResponse.token,             // Token as password
  port: Number(process.env.AZURE_POSTGRESQL_PORT) || 5432,
  ssl: { rejectUnauthorized: true }
});

await client.connect();
```

## Core Workflows

### 1. Single Client Connection

```typescript
import { Client } from "pg";

const client = new Client({
  host: process.env.AZURE_POSTGRESQL_HOST,
  database: process.env.AZURE_POSTGRESQL_DATABASE,
  user: process.env.AZURE_POSTGRESQL_USER,
  password: process.env.AZURE_POSTGRESQL_PASSWORD,
  port: 5432,
  ssl: { rejectUnauthorized: true }
});

try {
  await client.connect();
  
  const result = await client.query("SELECT NOW() as current_time");
  console.log(result.rows[0].current_time);
} finally {
  await client.end();  // Always close conn

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Connect to Azure Database for PostgreSQL Flexible Server using the `pg` (node-postgres) package with support for password and Microsoft Entra ID (passwordless) authentication.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure PostgreSQL for TypeScript (node-postgres)
- Para tarefas relacionadas a azure postgresql for typescript node postgres

## Diretrizes Específicas

