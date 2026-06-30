---
name: cosmos-db-service-implementation
description: Build production-grade Azure Cosmos DB NoSQL services following clean code, security best practices, and TDD principles.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Cosmos DB Service Implementation

## Backstory

Você é um agente especializado em Cosmos DB Service Implementation.

## Contexto Original da Skill
Cosmos DB Service Implementation

## Instruções
---
name: azure-cosmos-db-py
description: "Build production-grade Azure Cosmos DB NoSQL services following clean code, security best practices, and TDD principles."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Cosmos DB Service Implementation

Build production-grade Azure Cosmos DB NoSQL services following clean code, security best practices, and TDD principles.

## Installation

```bash
pip install azure-cosmos azure-identity
```

## Environment Variables

```bash
COSMOS_ENDPOINT=https://<account>.documents.azure.com:443/
COSMOS_DATABASE_NAME=<database-name>
COSMOS_CONTAINER_ID=<container-id>
# For emulator only (not production)
COSMOS_KEY=<emulator-key>
```

## Authentication

**DefaultAzureCredential (preferred)**:
```python
from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential

client = CosmosClient(
    url=os.environ["COSMOS_ENDPOINT"],
    credential=DefaultAzureCredential()
)
```

**Emulator (local development)**:
```python
from azure.cosmos import CosmosClient

client = CosmosClient(
    url="https://localhost:8081",
    credential=os.environ["COSMOS_KEY"],
    connection_verify=False
)
```

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         FastAPI Router                          │
│  - Auth dependencies (get_current_user, get_current_user_required)
│  - HTTP error responses (HTTPException)                         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                        Service Layer                            │
│  - Business logic and validation                                │
│  - Document ↔ Model conversion                                  │
│  - Graceful degradation when Cosmos unavailable                 │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                     Cosmos DB Client Module                     │
│  - Singleton container initialization                           │
│  - Dual auth: DefaultAzureCredential (Azure) / Key (emulator)   │
│  - Async wrapper via run_in_threadpool                          │
└─────────────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Client Module Setup

Create a singleton Cosmos client with dual authentication:

```python
# db/cosmos.py
from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential
from starlette.concurrency import run_in_threadpool

_cosmos_container = None

def _is_emulator_endpoint(endpoint: str) -> bool:
    return "localhost" in endpoint or "127.0.0.1" in endpoint

async def get_container():
    global _cosmos_container
    if _cosmos_container is None:
        if _is_emulator_endpoint(settings.cosmos_endpoint):
            

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Build production-grade Azure Cosmos DB NoSQL services following clean code, security best practices, and TDD principles.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Cosmos DB Service Implementation
- Para tarefas relacionadas a cosmos db service implementation

## Diretrizes Específicas

