---
name: practical-data-transformations
description: This skill covers the data transformations you do every day: working with arrays, reshaping objects, normalizing API responses, grouping data, and safely accessing nested values. Each section shows th
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Practical Data Transformations

## Backstory

Você é um agente especializado em Practical Data Transformations.

## Contexto Original da Skill
Practical Data Transformations

## Instruções
---
name: fp-data-transforms
description: Everyday data transformations using functional patterns - arrays, objects, grouping, aggregation, and null-safe access
risk: unknown
source: community
version: 1.0.0
author: Claude
tags:
  - functional-programming
  - typescript
  - data-transformation
  - fp-ts
  - arrays
  - objects
  - grouping
  - aggregation
  - null-safety
---

# Practical Data Transformations

This skill covers the data transformations you do every day: working with arrays, reshaping objects, normalizing API responses, grouping data, and safely accessing nested values. Each section shows the imperative approach first, then the functional equivalent, with honest assessments of when each approach shines.

## When to Use

- You need to transform arrays, objects, grouped data, or nested values in TypeScript.
- The task involves reshaping API responses, null-safe access, aggregation, or normalization.
- You want practical functional patterns for everyday data work instead of low-level loops.

---

## Table of Contents

1. [Array Operations](#1-array-operations)
2. [Object Transformations](#2-object-transformations)
3. [Data Normalization](#3-data-normalization)
4. [Grouping and Aggregation](#4-grouping-and-aggregation)
5. [Null-Safe Access](#5-null-safe-access)
6. [Real-World Examples](#6-real-world-examples)
7. [When to Use What](#7-when-to-use-what)

---

## 1. Array Operations

Array operations are the bread and butter of data transformation. Let's replace verbose loops with expressive, chainable operations.

### Map: Transform Every Element

**The Task**: Convert an array of prices from cents to dollars.

#### Imperative Approach

```typescript
const pricesInCents = [999, 1499, 2999, 4999];

function convertToDollars(prices: number[]): number[] {
  const result: number[] = [];
  for (let i = 0; i < prices.length; i++) {
    result.push(prices[i] / 100);
  }
  return result;
}

const dollars = convertToDollars(pricesInCents);
// [9.99, 14.99, 29.99, 49.99]
```

#### Functional Approach

```typescript
const pricesInCents = [999, 1499, 2999, 4999];

const toDollars = (cents: number): number => cents / 100;

const dollars = pricesInCents.map(toDollars);
// [9.99, 14.99, 29.99, 49.99]
```

**Why functional is better here**: The intent is immediately clear. `map` says "transform each element." The transformation logic (`toDollars`) is named and reusable. No index management, no manual array building.

### Filter: Keep What Matches

**The Task**: Get all active users from a list.

#### Imperative Approach

```typescript
interface User {
  id: string;
  name: string;
  isActive: boolean;
}

function getActiveUsers(users: User[]): User[] {
  const result: User[] = [];
  for (const user of users) {
    if (user.isActive) {
      result.push(user);
    }
  }
  return result;
}
```

#### Functional Approach

```typescript
const isActive = (user: User): boolean => user.isActive;

const activeUsers = users.filter(isActive);

// Or inline for simp

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

This skill covers the data transformations you do every day: working with arrays, reshaping objects, normalizing API responses, grouping data, and safely accessing nested values. Each section shows th

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Practical Data Transformations
- Para tarefas relacionadas a practical data transformations

## Diretrizes Específicas

