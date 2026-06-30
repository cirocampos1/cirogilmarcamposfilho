---
name: azure-event-hubs-sdk-for-typescript
description: High-throughput event streaming and real-time data ingestion.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Event Hubs SDK for TypeScript

## Backstory

Você é um agente especializado em Azure Event Hubs SDK for TypeScript.

## Contexto Original da Skill
Azure Event Hubs SDK for TypeScript

## Instruções
---
name: azure-eventhub-ts
description: "High-throughput event streaming and real-time data ingestion."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure Event Hubs SDK for TypeScript

High-throughput event streaming and real-time data ingestion.

## Installation

```bash
npm install @azure/event-hubs @azure/identity
```

For checkpointing with consumer groups:
```bash
npm install @azure/eventhubs-checkpointstore-blob @azure/storage-blob
```

## Environment Variables

```bash
EVENTHUB_NAMESPACE=<namespace>.servicebus.windows.net
EVENTHUB_NAME=my-eventhub
STORAGE_ACCOUNT_NAME=<storage-account>
STORAGE_CONTAINER_NAME=checkpoints
```

## Authentication

```typescript
import { EventHubProducerClient, EventHubConsumerClient } from "@azure/event-hubs";
import { DefaultAzureCredential } from "@azure/identity";

const fullyQualifiedNamespace = process.env.EVENTHUB_NAMESPACE!;
const eventHubName = process.env.EVENTHUB_NAME!;
const credential = new DefaultAzureCredential();

// Producer
const producer = new EventHubProducerClient(fullyQualifiedNamespace, eventHubName, credential);

// Consumer
const consumer = new EventHubConsumerClient(
  "$Default", // Consumer group
  fullyQualifiedNamespace,
  eventHubName,
  credential
);
```

## Core Workflow

### Send Events

```typescript
const producer = new EventHubProducerClient(namespace, eventHubName, credential);

// Create batch and add events
const batch = await producer.createBatch();
batch.tryAdd({ body: { temperature: 72.5, deviceId: "sensor-1" } });
batch.tryAdd({ body: { temperature: 68.2, deviceId: "sensor-2" } });

await producer.sendBatch(batch);
await producer.close();
```

### Send to Specific Partition

```typescript
// By partition ID
const batch = await producer.createBatch({ partitionId: "0" });

// By partition key (consistent hashing)
const batch = await producer.createBatch({ partitionKey: "device-123" });
```

### Receive Events (Simple)

```typescript
const consumer = new EventHubConsumerClient("$Default", namespace, eventHubName, credential);

const subscription = consumer.subscribe({
  processEvents: async (events, context) => {
    for (const event of events) {
      console.log(`Partition: ${context.partitionId}, Body: ${JSON.stringify(event.body)}`);
    }
  },
  processError: async (err, context) => {
    console.error(`Error on partition ${context.partitionId}: ${err.message}`);
  },
});

// Stop after some time
setTimeout(async () => {
  await subscription.close();
  await consumer.close();
}, 60000);
```

### Receive with Checkpointing (Production)

```typescript
import { EventHubConsumerClient } from "@azure/event-hubs";
import { ContainerClient } from "@azure/storage-blob";
import { BlobCheckpointStore } from "@azure/eventhubs-checkpointstore-blob";

const containerClient = new ContainerClient(
  `https://${storageAccount}.blob.core.windows.net/${containerName}`,
  credential
);

const checkpointStore = new BlobCheckpointStore(containerClient);

const consu

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

High-throughput event streaming and real-time data ingestion.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Event Hubs SDK for TypeScript
- Para tarefas relacionadas a azure event hubs sdk for typescript

## Diretrizes Específicas

