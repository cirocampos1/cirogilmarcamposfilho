---
name: functional-programming-in-react
description: Practical patterns for React apps. No jargon, just code that works.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Functional Programming in React

## Backstory

Você é um agente especializado em Functional Programming in React.

## Contexto Original da Skill
Functional Programming in React

## Instruções
---
name: fp-react
description: Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. Works with React 18/19, Next.js 14/15.
risk: unknown
source: community
version: 2.0.0
author: fp-ts-skills
tags: [fp-ts, react, typescript, hooks, state-management, forms, data-fetching, remote-data, react-19, next-js]
---

# Functional Programming in React

Practical patterns for React apps. No jargon, just code that works.

---

## Quick Reference

| Pattern | Use When |
|---------|----------|
| `Option` | Value might be missing (user not loaded yet) |
| `Either` | Operation might fail (form validation) |
| `TaskEither` | Async operation might fail (API calls) |
| `RemoteData` | Need to show loading/error/success states |
| `pipe` | Chaining multiple transformations |

---

## 1. State with Option (Maybe It's There, Maybe Not)

Use `Option` instead of `null | undefined` for clearer intent.

### Basic Pattern

```typescript
import { useState } from 'react'
import * as O from 'fp-ts/Option'
import { pipe } from 'fp-ts/function'

interface User {
  id: string
  name: string
  email: string
}

function UserProfile() {
  // Option says "this might not exist yet"
  const [user, setUser] = useState<O.Option<User>>(O.none)

  const handleLogin = (userData: User) => {
    setUser(O.some(userData))
  }

  const handleLogout = () => {
    setUser(O.none)
  }

  return pipe(
    user,
    O.match(
      // When there's no user
      () => <button onClick={() => handleLogin({ id: '1', name: 'Alice', email: 'alice@example.com' })}>
        Log In
      </button>,
      // When there's a user
      (u) => (
        <div>
          <p>Welcome, {u.name}!</p>
          <button onClick={handleLogout}>Log Out</button>
        </div>
      )
    )
  )
}
```

### Chaining Optional Values

```typescript
import * as O from 'fp-ts/Option'
import { pipe } from 'fp-ts/function'

interface Profile {
  user: O.Option<{
    name: string
    settings: O.Option<{
      theme: string
    }>
  }>
}

function getTheme(profile: Profile): string {
  return pipe(
    profile.user,
    O.flatMap(u => u.settings),
    O.map(s => s.theme),
    O.getOrElse(() => 'light') // default
  )
}
```

---

## 2. Form Validation with Either

Either is perfect for validation: `Left` = errors, `Right` = valid data.

### Simple Form Validation

```typescript
import * as E from 'fp-ts/Either'
import * as A from 'fp-ts/Array'
import { pipe } from 'fp-ts/function'

// Validation functions return Either<ErrorMessage, ValidValue>
const validateEmail = (email: string): E.Either<string, string> =>
  email.includes('@')
    ? E.right(email)
    : E.left('Invalid email address')

const validatePassword = (password: string): E.Either<string, string> =>
  password.length >= 8
    ? E.right(password)
    : E.left('Password must be at least 8 characters')

const validateName = (name: string): E.Either<string, string> =>
  name.trim().length > 0
    ? E.right(name.trim())
    : E.left('Name is requ

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Practical patterns for React apps. No jargon, just code that works.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Functional Programming in React
- Para tarefas relacionadas a functional programming in react

## Diretrizes Específicas

