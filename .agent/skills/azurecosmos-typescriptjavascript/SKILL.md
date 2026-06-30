---
name: azurecosmos-typescriptjavascript
description: Data plane SDK for Azure Cosmos DB NoSQL API operations — CRUD on documents, queries, bulk operations.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# @azure/cosmos (TypeScript/JavaScript)

## Backstory

Você é um agente especializado em @azure/cosmos (TypeScript/JavaScript).

## Contexto Original da Skill
@azure/cosmos (TypeScript/JavaScript)

## Instruções
---
name: azure-cosmos-ts
description: Azure Cosmos DB JavaScript/TypeScript SDK (@azure/cosmos) for data plane operations. Use for CRUD operations on documents, queries, bulk operations, and container management.
risk: unknown
source: community
date_added: '2026-02-27'
---

# @azure/cosmos (TypeScript/JavaScript)

Data plane SDK for Azure Cosmos DB NoSQL API operations — CRUD on documents, queries, bulk operations.

> **⚠️ Data vs Management Plane**
> - **This SDK (@azure/cosmos)**: CRUD operations on documents, queries, stored procedures
> - **Management SDK (@azure/arm-cosmosdb)**: Create accounts, databases, containers via ARM

## Installation

```bash
npm install @azure/cosmos @azure/identity
```

**Current Version**: 4.9.0  
**Node.js**: >= 20.0.0

## Environment Variables

```bash
COSMOS_ENDPOINT=https://<account>.documents.azure.com:443/
COSMOS_DATABASE=<database-name>
COSMOS_CONTAINER=<container-name>
# For key-based auth only (prefer AAD)
COSMOS_KEY=<account-key>
```

## Authentication

### AAD with DefaultAzureCredential (Recommended)

```typescript
import { CosmosClient } from "@azure/cosmos";
import { DefaultAzureCredential } from "@azure/identity";

const client = new CosmosClient({
  endpoint: process.env.COSMOS_ENDPOINT!,
  aadCredentials: new DefaultAzureCredential(),
});
```

### Key-Based Authentication

```typescript
import { CosmosClient } from "@azure/cosmos";

// Option 1: Endpoint + Key
const client = new CosmosClient({
  endpoint: process.env.COSMOS_ENDPOINT!,
  key: process.env.COSMOS_KEY!,
});

// Option 2: Connection String
const client = new CosmosClient(process.env.COSMOS_CONNECTION_STRING!);
```

## Resource Hierarchy

```
CosmosClient
└── Database
    └── Container
        ├── Items (documents)
        ├── Scripts (stored procedures, triggers, UDFs)
        └── Conflicts
```

## Core Operations

### Database & Container Setup

```typescript
const { database } = await client.databases.createIfNotExists({
  id: "my-database",
});

const { container } = await database.containers.createIfNotExists({
  id: "my-container",
  partitionKey: { paths: ["/partitionKey"] },
});
```

### Create Document

```typescript
interface Product {
  id: string;
  partitionKey: string;
  name: string;
  price: number;
}

const item: Product = {
  id: "product-1",
  partitionKey: "electronics",
  name: "Laptop",
  price: 999.99,
};

const { resource } = await container.items.create<Product>(item);
```

### Read Document

```typescript
const { resource } = await container
  .item("product-1", "electronics") // id, partitionKey
  .read<Product>();

if (resource) {
  console.log(resource.name);
}
```

### Update Document (Replace)

```typescript
const { resource: existing } = await container
  .item("product-1", "electronics")
  .read<Product>();

if (existing) {
  existing.price = 899.99;
  const { resource: updated } = await container
    .item("product-1", "electronics")
    .replace<Product>(existing);
}
```

### Upsert Document

```types

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Data plane SDK for Azure Cosmos DB NoSQL API operations — CRUD on documents, queries, bulk operations.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em @azure/cosmos (TypeScript/JavaScript)
- Para tarefas relacionadas a azurecosmos typescriptjavascript

## Diretrizes Específicas

