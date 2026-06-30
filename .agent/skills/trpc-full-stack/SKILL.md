---
name: trpc-full-stack
description: tRPC lets you build fully type-safe APIs without writing a schema or code-generation step. Your TypeScript types flow from the server router directly to the client — so every API call is autocompleted
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# tRPC Full-Stack

## Backstory

Você é um agente especializado em tRPC Full-Stack.

## Contexto Original da Skill
tRPC Full-Stack

## Instruções
---
name: trpc-fullstack
description: "Build end-to-end type-safe APIs with tRPC — routers, procedures, middleware, subscriptions, and Next.js/React integration patterns."
category: framework
risk: none
source: community
date_added: "2026-03-17"
author: suhaibjanjua
tags: [typescript, trpc, api, fullstack, nextjs, react, type-safety]
tools: [claude, cursor, gemini]
---

# tRPC Full-Stack

## Overview

tRPC lets you build fully type-safe APIs without writing a schema or code-generation step. Your TypeScript types flow from the server router directly to the client — so every API call is autocompleted, validated at compile time, and refactoring-safe. Use this skill when building TypeScript monorepos, Next.js apps, or any project where the server and client share a codebase.

## When to Use This Skill

- Use when building a TypeScript full-stack app (Next.js, Remix, Express + React) where the client and server share a single repo
- Use when you want end-to-end type safety on API calls without REST/GraphQL schema overhead
- Use when adding real-time features (subscriptions) to an existing tRPC setup
- Use when designing multi-step middleware (auth, rate limiting, tenant scoping) on tRPC procedures
- Use when migrating an existing REST/GraphQL API to tRPC incrementally

## Core Concepts

### Routers and Procedures

A **router** groups related **procedures** (think: endpoints). Procedures are typed functions — `query` for reads, `mutation` for writes, `subscription` for real-time streams.

### Input Validation with Zod

All procedure inputs are validated with Zod schemas. The validated, typed input is available in the procedure handler — no manual parsing.

### Context

`context` is shared state passed to every procedure — auth session, database client, request headers, etc. It is built once per request in a context factory. **Important:** Next.js App Router and Pages Router require separate context factories because App Router handlers receive a fetch `Request`, not a Node.js `NextApiRequest`.

### Middleware

Middleware chains run before a procedure. Use them for authentication, logging, and request enrichment. They can extend the context for downstream procedures.

---

## How It Works

### Step 1: Install and Initialize

```bash
npm install @trpc/server @trpc/client @trpc/react-query @tanstack/react-query zod
```

Create the tRPC instance and reusable builders:

```typescript
// src/server/trpc.ts
import { initTRPC, TRPCError } from '@trpc/server';
import { type Context } from './context';
import { ZodError } from 'zod';

const t = initTRPC.context<Context>().create({
  errorFormatter({ shape, error }) {
    return {
      ...shape,
      data: {
        ...shape.data,
        zodError:
          error.cause instanceof ZodError ? error.cause.flatten() : null,
      },
    };
  },
});

export const router = t.router;
export const publicProcedure = t.procedure;
export const middleware = t.middleware;
```

### Step 2: Define Two Context Factories

Next

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

tRPC lets you build fully type-safe APIs without writing a schema or code-generation step. Your TypeScript types flow from the server router directly to the client — so every API call is autocompleted

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em tRPC Full-Stack
- Para tarefas relacionadas a trpc full stack

## Diretrizes Específicas

