---
name: pydantic-models
description: Create Pydantic models following the multi-model pattern for clean API contracts.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Pydantic Models

## Backstory

Você é um agente especializado em Pydantic Models.

## Contexto Original da Skill
Pydantic Models

## Instruções
---
name: pydantic-models-py
description: "Create Pydantic models following the multi-model pattern for clean API contracts."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Pydantic Models

Create Pydantic models following the multi-model pattern for clean API contracts.

## Quick Start

Copy the template from assets/template.py and replace placeholders:
- `{{ResourceName}}` → PascalCase name (e.g., `Project`)
- `{{resource_name}}` → snake_case name (e.g., `project`)

## Multi-Model Pattern

| Model | Purpose |
|-------|---------|
| `Base` | Common fields shared across models |
| `Create` | Request body for creation (required fields) |
| `Update` | Request body for updates (all optional) |
| `Response` | API response with all fields |
| `InDB` | Database document with `doc_type` |

## camelCase Aliases

```python
class MyModel(BaseModel):
    workspace_id: str = Field(..., alias="workspaceId")
    created_at: datetime = Field(..., alias="createdAt")
    
    class Config:
        populate_by_name = True  # Accept both snake_case and camelCase
```

## Optional Update Fields

```python
class MyUpdate(BaseModel):
    """All fields optional for PATCH requests."""
    name: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None
```

## Database Document

```python
class MyInDB(MyResponse):
    """Adds doc_type for Cosmos DB queries."""
    doc_type: str = "my_resource"
```

## Integration Steps

1. Create models in `src/backend/app/models/`
2. Export from `src/backend/app/models/__init__.py`
3. Add corresponding TypeScript types

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Create Pydantic models following the multi-model pattern for clean API contracts.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Pydantic Models
- Para tarefas relacionadas a pydantic models

## Diretrizes Específicas

