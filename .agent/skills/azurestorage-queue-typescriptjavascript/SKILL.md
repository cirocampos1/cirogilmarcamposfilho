---
name: azurestorage-queue-typescriptjavascript
description: SDK for Azure Queue Storage operations — send, receive, peek, and manage messages in queues.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# @azure/storage-queue (TypeScript/JavaScript)

## Backstory

Você é um agente especializado em @azure/storage-queue (TypeScript/JavaScript).

## Contexto Original da Skill
@azure/storage-queue (TypeScript/JavaScript)

## Instruções
---
name: azure-storage-queue-ts
description: Azure Queue Storage JavaScript/TypeScript SDK (@azure/storage-queue) for message queue operations. Use for sending, receiving, peeking, and deleting messages in queues.
risk: unknown
source: community
date_added: '2026-02-27'
---

# @azure/storage-queue (TypeScript/JavaScript)

SDK for Azure Queue Storage operations — send, receive, peek, and manage messages in queues.

## Installation

```bash
npm install @azure/storage-queue @azure/identity
```

**Current Version**: 12.x  
**Node.js**: >= 18.0.0

## Environment Variables

```bash
AZURE_STORAGE_ACCOUNT_NAME=<account-name>
AZURE_STORAGE_ACCOUNT_KEY=<account-key>
# OR connection string
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=...
```

## Authentication

### DefaultAzureCredential (Recommended)

```typescript
import { QueueServiceClient } from "@azure/storage-queue";
import { DefaultAzureCredential } from "@azure/identity";

const accountName = process.env.AZURE_STORAGE_ACCOUNT_NAME!;
const client = new QueueServiceClient(
  `https://${accountName}.queue.core.windows.net`,
  new DefaultAzureCredential()
);
```

### Connection String

```typescript
import { QueueServiceClient } from "@azure/storage-queue";

const client = QueueServiceClient.fromConnectionString(
  process.env.AZURE_STORAGE_CONNECTION_STRING!
);
```

### StorageSharedKeyCredential (Node.js only)

```typescript
import { QueueServiceClient, StorageSharedKeyCredential } from "@azure/storage-queue";

const accountName = process.env.AZURE_STORAGE_ACCOUNT_NAME!;
const accountKey = process.env.AZURE_STORAGE_ACCOUNT_KEY!;

const sharedKeyCredential = new StorageSharedKeyCredential(accountName, accountKey);
const client = new QueueServiceClient(
  `https://${accountName}.queue.core.windows.net`,
  sharedKeyCredential
);
```

### SAS Token

```typescript
import { QueueServiceClient } from "@azure/storage-queue";

const accountName = process.env.AZURE_STORAGE_ACCOUNT_NAME!;
const sasToken = process.env.AZURE_STORAGE_SAS_TOKEN!;

const client = new QueueServiceClient(
  `https://${accountName}.queue.core.windows.net${sasToken}`
);
```

## Client Hierarchy

```
QueueServiceClient (account level)
└── QueueClient (queue level)
    └── Messages (send, receive, peek, delete)
```

## Queue Operations

### Create Queue

```typescript
const queueClient = client.getQueueClient("my-queue");
await queueClient.create();

// Or create if not exists
await queueClient.createIfNotExists();
```

### List Queues

```typescript
for await (const queue of client.listQueues()) {
  console.log(queue.name);
}

// With prefix filter
for await (const queue of client.listQueues({ prefix: "task-" })) {
  console.log(queue.name);
}
```

### Delete Queue

```typescript
await queueClient.delete();

// Or delete if exists
await queueClient.deleteIfExists();
```

### Get Queue Properties

```typescript
const properties = await queueClient.getProperties();
console.log("Approximate message count:", pr

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

SDK for Azure Queue Storage operations — send, receive, peek, and manage messages in queues.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em @azure/storage-queue (TypeScript/JavaScript)
- Para tarefas relacionadas a azurestorage queue typescriptjavascript

## Diretrizes Específicas

