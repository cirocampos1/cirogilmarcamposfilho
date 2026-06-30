---
name: practical-async-patterns-with-fp-ts
description: Stop writing nested try/catch blocks. Stop losing error context. Start building clean async pipelines that handle errors properly.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Practical Async Patterns with fp-ts

## Backstory

Você é um agente especializado em Practical Async Patterns with fp-ts.

## Contexto Original da Skill
Practical Async Patterns with fp-ts

## Instruções
---
name: fp-async
description: Practical async patterns using TaskEither - clean pipelines instead of try/catch hell, with real API examples
risk: unknown
source: community
version: 1.0.0
author: kadu
tags:
  - fp-ts
  - typescript
  - async
  - error-handling
  - practical
  - promises
  - api
  - fetch
---

# Practical Async Patterns with fp-ts

Stop writing nested try/catch blocks. Stop losing error context. Start building clean async pipelines that handle errors properly.

**TaskEither is simply an async operation that tracks success or failure.** That's it. No fancy terminology needed.

## When to Use

- You need async error handling in TypeScript with `TaskEither`.
- The task involves wrapping Promises, composing API calls, or replacing nested `try/catch` flows.
- You want practical fp-ts async patterns instead of academic explanations.

```typescript
// TaskEither<Error, User> means:
// "An async operation that either fails with Error or succeeds with User"
```

---

## 1. Wrapping Promises Safely

### The Problem: Try/Catch Everywhere

```typescript
// BEFORE: Try/catch hell
async function getUserData(userId: string) {
  try {
    const response = await fetch(`/api/users/${userId}`)
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`)
    }
    const user = await response.json()

    try {
      const posts = await fetch(`/api/users/${userId}/posts`)
      if (!posts.ok) {
        throw new Error(`HTTP ${posts.status}`)
      }
      const postsData = await posts.json()
      return { user, posts: postsData }
    } catch (postsError) {
      // Now what? Return partial data? Rethrow? Log?
      console.error('Failed to fetch posts:', postsError)
      return { user, posts: [] }
    }
  } catch (error) {
    // Lost all context about what failed
    console.error('Something failed:', error)
    throw error
  }
}
```

### The Solution: Wrap Once, Handle Cleanly

```typescript
import * as TE from 'fp-ts/TaskEither'
import * as E from 'fp-ts/Either'
import { pipe } from 'fp-ts/function'

// One wrapper function - reuse everywhere
const fetchJson = <T>(url: string): TE.TaskEither<Error, T> =>
  TE.tryCatch(
    async () => {
      const response = await fetch(url)
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }
      return response.json()
    },
    (error) => error instanceof Error ? error : new Error(String(error))
  )

// AFTER: Clean and composable
const getUser = (userId: string) => fetchJson<User>(`/api/users/${userId}`)
const getPosts = (userId: string) => fetchJson<Post[]>(`/api/users/${userId}/posts`)
```

### tryCatch Explained

`TE.tryCatch` takes two things:
1. An async function that might throw
2. A function to convert the thrown value into your error type

```typescript
TE.tryCatch(
  () => somePromise,           // The async work
  (thrown) => toError(thrown)  // Convert failures to your error type
)
```

### Creating Success and Failure Values

`

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Stop writing nested try/catch blocks. Stop losing error context. Start building clean async pipelines that handle errors properly.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Practical Async Patterns with fp-ts
- Para tarefas relacionadas a practical async patterns with fp ts

## Diretrizes Específicas

