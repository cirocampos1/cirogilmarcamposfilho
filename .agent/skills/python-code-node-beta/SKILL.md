---
name: python-code-node-beta
description: Expert guidance for writing Python code in n8n Code nodes.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Python Code Node (Beta)

## Backstory

Você é um agente especializado em Python Code Node (Beta).

## Contexto Original da Skill
Python Code Node (Beta)

## Instruções
---
name: n8n-code-python
description: Write Python code in n8n Code nodes. Use when writing Python in n8n, using _input/_json/_node syntax, working with standard library, or need to understand Python limitations in n8n Code nodes.
risk: unknown
source: community
---

# Python Code Node (Beta)

Expert guidance for writing Python code in n8n Code nodes.

---

## ⚠️ Important: JavaScript First

**Recommendation**: Use **JavaScript for 95% of use cases**. Only use Python when:
- You need specific Python standard library functions
- You're significantly more comfortable with Python syntax
- You're doing data transformations better suited to Python

**Why JavaScript is preferred:**
- Full n8n helper functions ($helpers.httpRequest, etc.)
- Luxon DateTime library for advanced date/time operations
- No external library limitations
- Better n8n documentation and community support

---

## Quick Start

```python
# Basic template for Python Code nodes
items = _input.all()

# Process data
processed = []
for item in items:
    processed.append({
        "json": {
            **item["json"],
            "processed": True,
            "timestamp": datetime.now().isoformat()
        }
    })

return processed
```

### Essential Rules

1. **Consider JavaScript first** - Use Python only when necessary
2. **Access data**: `_input.all()`, `_input.first()`, or `_input.item`
3. **CRITICAL**: Must return `[{"json": {...}}]` format
4. **CRITICAL**: Webhook data is under `_json["body"]` (not `_json` directly)
5. **CRITICAL LIMITATION**: **No external libraries** (no requests, pandas, numpy)
6. **Standard library only**: json, datetime, re, base64, hashlib, urllib.parse, math, random, statistics

---

## Mode Selection Guide

Same as JavaScript - choose based on your use case:

### Run Once for All Items (Recommended - Default)

**Use this mode for:** 95% of use cases

- **How it works**: Code executes **once** regardless of input count
- **Data access**: `_input.all()` or `_items` array (Native mode)
- **Best for**: Aggregation, filtering, batch processing, transformations
- **Performance**: Faster for multiple items (single execution)

```python
# Example: Calculate total from all items
all_items = _input.all()
total = sum(item["json"].get("amount", 0) for item in all_items)

return [{
    "json": {
        "total": total,
        "count": len(all_items),
        "average": total / len(all_items) if all_items else 0
    }
}]
```

### Run Once for Each Item

**Use this mode for:** Specialized cases only

- **How it works**: Code executes **separately** for each input item
- **Data access**: `_input.item` or `_item` (Native mode)
- **Best for**: Item-specific logic, independent operations, per-item validation
- **Performance**: Slower for large datasets (multiple executions)

```python
# Example: Add processing timestamp to each item
item = _input.item

return [{
    "json": {
        **item["json"],
        "processed": True,
        "processed_at": datetime.now().isofo

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Expert guidance for writing Python code in n8n Code nodes.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Python Code Node (Beta)
- Para tarefas relacionadas a python code node beta

## Diretrizes Específicas

