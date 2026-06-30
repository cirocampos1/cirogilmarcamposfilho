---
name: event-store-design
description: Comprehensive guide to designing event stores for event-sourced applications.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Event Store Design

## Backstory

Você é um agente especializado em Event Store Design.

## Contexto Original da Skill
Event Store Design

## Instruções
---
name: event-store-design
description: "Design and implement event stores for event-sourced systems. Use when building event sourcing infrastructure, choosing event store technologies, or implementing event persistence patterns."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Event Store Design

Comprehensive guide to designing event stores for event-sourced applications.

## Do not use this skill when

- The task is unrelated to event store design
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Designing event sourcing infrastructure
- Choosing between event store technologies
- Implementing custom event stores
- Optimizing event storage and retrieval
- Setting up event store schemas
- Planning for event store scaling

## Core Concepts

### 1. Event Store Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Event Store                       │
├─────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   Stream 1   │  │   Stream 2   │  │   Stream 3   │ │
│  │ (Aggregate)  │  │ (Aggregate)  │  │ (Aggregate)  │ │
│  ├─────────────┤  ├─────────────┤  ├─────────────┤ │
│  │ Event 1     │  │ Event 1     │  │ Event 1     │ │
│  │ Event 2     │  │ Event 2     │  │ Event 2     │ │
│  │ Event 3     │  │ ...         │  │ Event 3     │ │
│  │ ...         │  │             │  │ Event 4     │ │
│  └─────────────┘  └─────────────┘  └─────────────┘ │
├─────────────────────────────────────────────────────┤
│  Global Position: 1 → 2 → 3 → 4 → 5 → 6 → ...     │
└─────────────────────────────────────────────────────┘
```

### 2. Event Store Requirements

| Requirement       | Description                        |
| ----------------- | ---------------------------------- |
| **Append-only**   | Events are immutable, only appends |
| **Ordered**       | Per-stream and global ordering     |
| **Versioned**     | Optimistic concurrency control     |
| **Subscriptions** | Real-time event notifications      |
| **Idempotent**    | Handle duplicate writes safely     |

## Technology Comparison

| Technology       | Best For                  | Limitations                      |
| ---------------- | ------------------------- | -------------------------------- |
| **EventStoreDB** | Pure event sourcing       | Single-purpose                   |
| **PostgreSQL**   | Existing Postgres stack   | Manual implementation            |
| **Kafka**        | High-throughput streaming | Not ideal for per-stream queries |
| **DynamoDB**     | Serverless, AWS-native    | Query limitations                |
| **Marten**       | .NET ecosystems           | .NET specific                    |

## Te

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Comprehensive guide to designing event stores for event-sourced applications.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Event Store Design
- Para tarefas relacionadas a event store design

## Diretrizes Específicas

