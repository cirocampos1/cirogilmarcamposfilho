---
name: azure-app-configuration-sdk-for-typescript
description: Centralized configuration management with feature flags and dynamic refresh.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure App Configuration SDK for TypeScript

## Backstory

Você é um agente especializado em Azure App Configuration SDK for TypeScript.

## Contexto Original da Skill
Azure App Configuration SDK for TypeScript

## Instruções
---
name: azure-appconfiguration-ts
description: "Centralized configuration management with feature flags and dynamic refresh."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure App Configuration SDK for TypeScript

Centralized configuration management with feature flags and dynamic refresh.

## Installation

```bash
# Low-level CRUD SDK
npm install @azure/app-configuration @azure/identity

# High-level provider (recommended for apps)
npm install @azure/app-configuration-provider @azure/identity

# Feature flag management
npm install @microsoft/feature-management
```

## Environment Variables

```bash
AZURE_APPCONFIG_ENDPOINT=https://<your-resource>.azconfig.io
# OR
AZURE_APPCONFIG_CONNECTION_STRING=Endpoint=https://...;Id=...;Secret=...
```

## Authentication

```typescript
import { AppConfigurationClient } from "@azure/app-configuration";
import { DefaultAzureCredential } from "@azure/identity";

// DefaultAzureCredential (recommended)
const client = new AppConfigurationClient(
  process.env.AZURE_APPCONFIG_ENDPOINT!,
  new DefaultAzureCredential()
);

// Connection string
const client2 = new AppConfigurationClient(
  process.env.AZURE_APPCONFIG_CONNECTION_STRING!
);
```

## CRUD Operations

### Create/Update Settings

```typescript
// Add new (fails if exists)
await client.addConfigurationSetting({
  key: "app:settings:message",
  value: "Hello World",
  label: "production",
  contentType: "text/plain",
  tags: { environment: "prod" },
});

// Set (create or update)
await client.setConfigurationSetting({
  key: "app:settings:message",
  value: "Updated value",
  label: "production",
});

// Update with optimistic concurrency
const existing = await client.getConfigurationSetting({ key: "myKey" });
existing.value = "new value";
await client.setConfigurationSetting(existing, { onlyIfUnchanged: true });
```

### Read Settings

```typescript
// Get single setting
const setting = await client.getConfigurationSetting({
  key: "app:settings:message",
  label: "production",  // optional
});
console.log(setting.value);

// List with filters
const settings = client.listConfigurationSettings({
  keyFilter: "app:*",
  labelFilter: "production",
});

for await (const setting of settings) {
  console.log(`${setting.key}: ${setting.value}`);
}
```

### Delete Settings

```typescript
await client.deleteConfigurationSetting({
  key: "app:settings:message",
  label: "production",
});
```

### Lock/Unlock (Read-Only)

```typescript
// Lock
await client.setReadOnly({ key: "myKey", label: "prod" }, true);

// Unlock
await client.setReadOnly({ key: "myKey", label: "prod" }, false);
```

## App Configuration Provider

### Load Configuration

```typescript
import { load } from "@azure/app-configuration-provider";
import { DefaultAzureCredential } from "@azure/identity";

const appConfig = await load(
  process.env.AZURE_APPCONFIG_ENDPOINT!,
  new DefaultAzureCredential(),
  {
    selectors: [
      { keyFilter: "app:*", labelFilter: "production" },

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Centralized configuration management with feature flags and dynamic refresh.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure App Configuration SDK for TypeScript
- Para tarefas relacionadas a azure app configuration sdk for typescript

## Diretrizes Específicas

