---
name: practical-error-handling-with-fp-ts
description: This skill teaches you how to handle errors without try/catch spaghetti. No academic jargon - just practical patterns for real problems.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Practical Error Handling with fp-ts

## Backstory

Você é um agente especializado em Practical Error Handling with fp-ts.

## Contexto Original da Skill
Practical Error Handling with fp-ts

## Instruções
---
name: fp-ts-errors
description: "Handle errors as values using fp-ts Either and TaskEither for cleaner, more predictable TypeScript code. Use when implementing error handling patterns with fp-ts."
risk: safe
source: "https://github.com/whatiskadudoing/fp-ts-skills"
date_added: "2026-02-27"
---

# Practical Error Handling with fp-ts

This skill teaches you how to handle errors without try/catch spaghetti. No academic jargon - just practical patterns for real problems.

## When to Use This Skill

- When you want type-safe error handling in TypeScript
- When replacing try/catch with Either and TaskEither patterns
- When building APIs or services that need explicit error types
- When accumulating multiple validation errors

The core idea: **Errors are just data**. Instead of throwing them into the void and hoping someone catches them, return them as values that TypeScript can track.

---

## 1. Stop Throwing Everywhere

### The Problem with Exceptions

Exceptions are invisible in your types. They break the contract between functions.

```typescript
// What this function signature promises:
function getUser(id: string): User

// What it actually does:
function getUser(id: string): User {
  if (!id) throw new Error('ID required')
  const user = db.find(id)
  if (!user) throw new Error('User not found')
  return user
}

// The caller has no idea this can fail
const user = getUser(id) // Might explode!
```

You end up with code like this:

```typescript
// MESSY: try/catch everywhere
function processOrder(orderId: string) {
  let order
  try {
    order = getOrder(orderId)
  } catch (e) {
    console.error('Failed to get order')
    return null
  }

  let user
  try {
    user = getUser(order.userId)
  } catch (e) {
    console.error('Failed to get user')
    return null
  }

  let payment
  try {
    payment = chargeCard(user.cardId, order.total)
  } catch (e) {
    console.error('Payment failed')
    return null
  }

  return { order, user, payment }
}
```

### The Solution: Return Errors as Values

```typescript
import * as E from 'fp-ts/Either'
import { pipe } from 'fp-ts/function'

// Now TypeScript KNOWS this can fail
function getUser(id: string): E.Either<string, User> {
  if (!id) return E.left('ID required')
  const user = db.find(id)
  if (!user) return E.left('User not found')
  return E.right(user)
}

// The caller is forced to handle both cases
const result = getUser(id)
// result is Either<string, User> - error OR success, never both
```

---

## 2. The Result Pattern (Either)

`Either<E, A>` is simple: it holds either an error (`E`) or a value (`A`).

- `Left` = error case
- `Right` = success case (think "right" as in "correct")

```typescript
import * as E from 'fp-ts/Either'

// Creating values
const success = E.right(42)           // Right(42)
const failure = E.left('Oops')        // Left('Oops')

// Checking what you have
if (E.isRight(result)) {
  console.log(result.right) // The success value
} else {
  console.log(result.left)  

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

This skill teaches you how to handle errors without try/catch spaghetti. No academic jargon - just practical patterns for real problems.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Practical Error Handling with fp-ts
- Para tarefas relacionadas a practical error handling with fp ts

## Diretrizes Específicas

