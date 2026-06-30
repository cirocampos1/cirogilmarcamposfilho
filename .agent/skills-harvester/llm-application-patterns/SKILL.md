---
name: llm-application-patterns
description: > Production-ready patterns for building LLM applications, inspired by [Dify](https://github.com/langgenius/dify) and industry best practices.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# 🤖 LLM Application Patterns

## Backstory

Você é um agente especializado em 🤖 LLM Application Patterns.

## Contexto Original da Skill
🤖 LLM Application Patterns

## Instruções
---
name: llm-app-patterns
description: "Production-ready patterns for building LLM applications, inspired by [Dify](https://github.com/langgenius/dify) and industry best practices."
risk: unknown
source: community
date_added: "2026-02-27"
---

# 🤖 LLM Application Patterns

> Production-ready patterns for building LLM applications, inspired by [Dify](https://github.com/langgenius/dify) and industry best practices.

## When to Use This Skill

Use this skill when:

- Designing LLM-powered applications
- Implementing RAG (Retrieval-Augmented Generation)
- Building AI agents with tools
- Setting up LLMOps monitoring
- Choosing between agent architectures

---

## 1. RAG Pipeline Architecture

### Overview

RAG (Retrieval-Augmented Generation) grounds LLM responses in your data.

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Ingest    │────▶│   Retrieve  │────▶│   Generate  │
│  Documents  │     │   Context   │     │   Response  │
└─────────────┘     └─────────────┘     └─────────────┘
      │                   │                   │
      ▼                   ▼                   ▼
 ┌─────────┐       ┌───────────┐       ┌───────────┐
 │ Chunking│       │  Vector   │       │    LLM    │
 │Embedding│       │  Search   │       │  + Context│
 └─────────┘       └───────────┘       └───────────┘
```

### 1.1 Document Ingestion

```python
# Chunking strategies
class ChunkingStrategy:
    # Fixed-size chunks (simple but may break context)
    FIXED_SIZE = "fixed_size"  # e.g., 512 tokens

    # Semantic chunking (preserves meaning)
    SEMANTIC = "semantic"      # Split on paragraphs/sections

    # Recursive splitting (tries multiple separators)
    RECURSIVE = "recursive"    # ["\n\n", "\n", " ", ""]

    # Document-aware (respects structure)
    DOCUMENT_AWARE = "document_aware"  # Headers, lists, etc.

# Recommended settings
CHUNK_CONFIG = {
    "chunk_size": 512,       # tokens
    "chunk_overlap": 50,     # token overlap between chunks
    "separators": ["\n\n", "\n", ". ", " "],
}
```

### 1.2 Embedding & Storage

```python
# Vector database selection
VECTOR_DB_OPTIONS = {
    "pinecone": {
        "use_case": "Production, managed service",
        "scale": "Billions of vectors",
        "features": ["Hybrid search", "Metadata filtering"]
    },
    "weaviate": {
        "use_case": "Self-hosted, multi-modal",
        "scale": "Millions of vectors",
        "features": ["GraphQL API", "Modules"]
    },
    "chromadb": {
        "use_case": "Development, prototyping",
        "scale": "Thousands of vectors",
        "features": ["Simple API", "In-memory option"]
    },
    "pgvector": {
        "use_case": "Existing Postgres infrastructure",
        "scale": "Millions of vectors",
        "features": ["SQL integration", "ACID compliance"]
    }
}

# Embedding model selection
EMBEDDING_MODELS = {
    "openai/text-embedding-3-small": {
        "dimensions": 1536,
        "cost": "$0.02/1M tokens",
        "quality": "Good for most use case

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

> Production-ready patterns for building LLM applications, inspired by [Dify](https://github.com/langgenius/dify) and industry best practices.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em 🤖 LLM Application Patterns
- Para tarefas relacionadas a llm application patterns

## Diretrizes Específicas

