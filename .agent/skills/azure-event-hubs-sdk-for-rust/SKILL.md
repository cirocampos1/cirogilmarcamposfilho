---
name: azure-event-hubs-sdk-for-rust
description: Client library for Azure Event Hubs — big data streaming platform and event ingestion service.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Event Hubs SDK for Rust

## Backstory

Você é um agente especializado em Azure Event Hubs SDK for Rust.

## Contexto Original da Skill
Azure Event Hubs SDK for Rust

## Instruções
---
name: azure-eventhub-rust
description: Azure Event Hubs SDK for Rust. Use for sending and receiving events, streaming data ingestion.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure Event Hubs SDK for Rust

Client library for Azure Event Hubs — big data streaming platform and event ingestion service.

## Installation

```sh
cargo add azure_messaging_eventhubs azure_identity
```

## Environment Variables

```bash
EVENTHUBS_HOST=<namespace>.servicebus.windows.net
EVENTHUB_NAME=<eventhub-name>
```

## Key Concepts

- **Namespace** — container for Event Hubs
- **Event Hub** — stream of events partitioned for parallel processing
- **Partition** — ordered sequence of events
- **Producer** — sends events to Event Hub
- **Consumer** — receives events from partitions

## Producer Client

### Create Producer

```rust
use azure_identity::DeveloperToolsCredential;
use azure_messaging_eventhubs::ProducerClient;

let credential = DeveloperToolsCredential::new(None)?;
let producer = ProducerClient::builder()
    .open("<namespace>.servicebus.windows.net", "eventhub-name", credential.clone())
    .await?;
```

### Send Single Event

```rust
producer.send_event(vec![1, 2, 3, 4], None).await?;
```

### Send Batch

```rust
let batch = producer.create_batch(None).await?;
batch.try_add_event_data(b"event 1".to_vec(), None)?;
batch.try_add_event_data(b"event 2".to_vec(), None)?;

producer.send_batch(batch, None).await?;
```

## Consumer Client

### Create Consumer

```rust
use azure_messaging_eventhubs::ConsumerClient;

let credential = DeveloperToolsCredential::new(None)?;
let consumer = ConsumerClient::builder()
    .open("<namespace>.servicebus.windows.net", "eventhub-name", credential.clone())
    .await?;
```

### Receive Events

```rust
// Open receiver for specific partition
let receiver = consumer.open_partition_receiver("0", None).await?;

// Receive events
let events = receiver.receive_events(100, None).await?;
for event in events {
    println!("Event data: {:?}", event.body());
}
```

### Get Event Hub Properties

```rust
let properties = consumer.get_eventhub_properties(None).await?;
println!("Partitions: {:?}", properties.partition_ids);
```

### Get Partition Properties

```rust
let partition_props = consumer.get_partition_properties("0", None).await?;
println!("Last sequence number: {}", partition_props.last_enqueued_sequence_number);
```

## Best Practices

1. **Reuse clients** — create once, send many events
2. **Use batches** — more efficient than individual sends
3. **Check batch capacity** — `try_add_event_data` returns false when full
4. **Process partitions in parallel** — each partition can be consumed independently
5. **Use consumer groups** — isolate different consuming applications
6. **Handle checkpointing** — use `azure_messaging_eventhubs_checkpointstore_blob` for distributed consumers

## Checkpoint Store (Optional)

For distributed consumers with checkpointing:

```sh
cargo add azure_messaging_eventhubs_checkpo

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Client library for Azure Event Hubs — big data streaming platform and event ingestion service.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Event Hubs SDK for Rust
- Para tarefas relacionadas a azure event hubs sdk for rust

## Diretrizes Específicas

