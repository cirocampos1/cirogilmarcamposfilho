---
name: jq-json-querying-and-transformation
description: `jq` is the standard CLI tool for querying and reshaping JSON. This skill covers practical, expert-level usage: filtering deeply nested data, transforming structures, aggregating values, and composing
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# jq — JSON Querying and Transformation

## Backstory

Você é um agente especializado em jq — JSON Querying and Transformation.

## Contexto Original da Skill
jq — JSON Querying and Transformation

## Instruções
---
name: jq
description: "Expert jq usage for JSON querying, filtering, transformation, and pipeline integration. Practical patterns for real shell workflows."
category: development
risk: safe
source: community
date_added: "2026-03-28"
author: kostakost2
tags: [jq, json, shell, cli, data-transformation, bash]
tools: [claude, cursor, gemini]
---

# jq — JSON Querying and Transformation

## Overview

`jq` is the standard CLI tool for querying and reshaping JSON. This skill covers practical, expert-level usage: filtering deeply nested data, transforming structures, aggregating values, and composing `jq` into shell pipelines. Every example is copy-paste ready for real workflows.

## When to Use This Skill

- Use when parsing JSON output from APIs, CLI tools (AWS, GitHub, kubectl, docker), or log files
- Use when transforming JSON structure (rename keys, flatten arrays, group records)
- Use when the user needs `jq` inside a bash script or one-liner
- Use when explaining what a complex `jq` expression does

## How It Works

`jq` takes a filter expression and applies it to JSON input. Filters compose with pipes (`|`), and `jq` handles arrays, objects, strings, numbers, booleans, and `null` natively.

### Basic Selection

```bash
# Extract a field
echo '{"name":"alice","age":30}' | jq '.name'
# "alice"

# Nested access
echo '{"user":{"email":"a@b.com"}}' | jq '.user.email'

# Array index
echo '[10, 20, 30]' | jq '.[1]'
# 20

# Array slice
echo '[1,2,3,4,5]' | jq '.[2:4]'
# [3, 4]

# All array elements
echo '[{"id":1},{"id":2}]' | jq '.[]'
```

### Filtering with `select`

```bash
# Keep only matching elements
echo '[{"role":"admin"},{"role":"user"},{"role":"admin"}]' \
  | jq '[.[] | select(.role == "admin")]'

# Numeric comparison
curl -s https://api.github.com/repos/owner/repo/issues \
  | jq '[.[] | select(.comments > 5)]'

# Test a field exists and is non-null
jq '[.[] | select(.email != null)]'

# Combine conditions
jq '[.[] | select(.active == true and .score >= 80)]'
```

### Mapping and Transformation

```bash
# Extract a field from every array element
echo '[{"name":"alice","age":30},{"name":"bob","age":25}]' \
  | jq '[.[] | .name]'
# ["alice", "bob"]

# Shorthand: map()
jq 'map(.name)'

# Build a new object per element
jq '[.[] | {user: .name, years: .age}]'

# Add a computed field
jq '[.[] | . + {senior: (.age > 28)}]'

# Rename keys
jq '[.[] | {username: .name, email_address: .email}]'
```

### Aggregation and Reduce

```bash
# Sum all values
echo '[1, 2, 3, 4, 5]' | jq 'add'
# 15

# Sum a field across objects
jq '[.[].price] | add'

# Count elements
jq 'length'

# Max / min
jq 'max_by(.score)'
jq 'min_by(.created_at)'

# reduce: custom accumulator
echo '[1,2,3,4,5]' | jq 'reduce .[] as $x (0; . + $x)'
# 15

# Group by field
jq 'group_by(.department)'

# Count per group
jq 'group_by(.status) | map({status: .[0].status, count: length})'
```

### String Interpolation and Formatting

```bash
# String interpolation
jq -r '.[] | "\(.name) is \(.

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

`jq` is the standard CLI tool for querying and reshaping JSON. This skill covers practical, expert-level usage: filtering deeply nested data, transforming structures, aggregating values, and composing

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em jq — JSON Querying and Transformation
- Para tarefas relacionadas a jq json querying and transformation

## Diretrizes Específicas

