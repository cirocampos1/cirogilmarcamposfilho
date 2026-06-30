---
name: pragmatic-functional-programming
description: **Read this first.** This guide cuts through the academic jargon and shows you what actually matters. No category theory. No abstract nonsense. Just patterns that make your code better.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Pragmatic Functional Programming

## Backstory

Você é um agente especializado em Pragmatic Functional Programming.

## Contexto Original da Skill
Pragmatic Functional Programming

## Instruções
---
name: fp-pragmatic
description: A practical, jargon-free guide to functional programming - the 80/20 approach that gets results without the academic overhead
risk: unknown
source: community
version: 1.0.0
author: kadu
tags:
  - fp-ts
  - functional-programming
  - typescript
  - pragmatic
  - beginner-friendly
  - best-practices
---

# Pragmatic Functional Programming

**Read this first.** This guide cuts through the academic jargon and shows you what actually matters. No category theory. No abstract nonsense. Just patterns that make your code better.

## When to Use

- You want a pragmatic starting point for fp-ts or functional programming in TypeScript.
- The task is exploratory or educational and needs an 80/20 view of what is actually worth adopting.
- You need guidance on when FP helps and when it is better to keep code simple.

## The Golden Rule

> **If functional programming makes your code harder to read, don't use it.**

FP is a tool, not a religion. Use it when it helps. Skip it when it doesn't.

---

## The 80/20 of FP

These five patterns give you most of the benefits. Master these before exploring anything else.

### 1. Pipe: Chain Operations Clearly

Instead of nesting function calls or creating intermediate variables, chain operations in reading order.

```typescript
import { pipe } from 'fp-ts/function'

// Before: Hard to read (inside-out)
const result = format(validate(parse(input)))

// Before: Too many variables
const parsed = parse(input)
const validated = validate(parsed)
const result = format(validated)

// After: Clear, linear flow
const result = pipe(
  input,
  parse,
  validate,
  format
)
```

**When to use pipe:**
- 3+ transformations on the same data
- You find yourself naming throwaway variables
- Logic reads better top-to-bottom

**When to skip pipe:**
- Just 1-2 operations (direct call is fine)
- The operations don't naturally chain

### 2. Option: Handle Missing Values Without null Checks

Stop writing `if (x !== null && x !== undefined)` everywhere.

```typescript
import * as O from 'fp-ts/Option'
import { pipe } from 'fp-ts/function'

// Before: Defensive null checking
function getUserCity(user: User | null): string {
  if (user === null) return 'Unknown'
  if (user.address === null) return 'Unknown'
  if (user.address.city === null) return 'Unknown'
  return user.address.city
}

// After: Chain through potential missing values
const getUserCity = (user: User | null): string =>
  pipe(
    O.fromNullable(user),
    O.flatMap(u => O.fromNullable(u.address)),
    O.flatMap(a => O.fromNullable(a.city)),
    O.getOrElse(() => 'Unknown')
  )
```

**Plain language translation:**
- `O.fromNullable(x)` = "wrap this value, treating null/undefined as 'nothing'"
- `O.flatMap(fn)` = "if we have something, apply this function"
- `O.getOrElse(() => default)` = "unwrap, or use this default if nothing"

### 3. Either: Make Errors Explicit

Stop throwing exceptions for expected failures. Return errors as values.

```typesc

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

**Read this first.** This guide cuts through the academic jargon and shows you what actually matters. No category theory. No abstract nonsense. Just patterns that make your code better.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Pragmatic Functional Programming
- Para tarefas relacionadas a pragmatic functional programming

## Diretrizes Específicas

