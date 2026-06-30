---
name: nextjs-supabase-auth
description: Expert integration of Supabase Auth with Next.js App Router
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Next.js + Supabase Auth

## Backstory

Você é um agente especializado em Next.js + Supabase Auth.

## Contexto Original da Skill
Next.js + Supabase Auth

## Instruções
---
name: nextjs-supabase-auth
description: Expert integration of Supabase Auth with Next.js App Router
risk: none
source: vibeship-spawner-skills (Apache 2.0)
date_added: 2026-02-27
---

# Next.js + Supabase Auth

Expert integration of Supabase Auth with Next.js App Router

## Capabilities

- nextjs-auth
- supabase-auth-nextjs
- auth-middleware
- auth-callback

## Prerequisites

- Required skills: nextjs-app-router, supabase-backend

## Patterns

### Supabase Client Setup

Create properly configured Supabase clients for different contexts

**When to use**: Setting up auth in a Next.js project

// lib/supabase/client.ts (Browser client)
'use client'
import { createBrowserClient } from '@supabase/ssr'

export function createClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  )
}

// lib/supabase/server.ts (Server client)
import { createServerClient } from '@supabase/ssr'
import { cookies } from 'next/headers'

export async function createClient() {
  const cookieStore = await cookies()
  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return cookieStore.getAll()
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value, options }) => {
            cookieStore.set(name, value, options)
          })
        },
      },
    }
  )
}

### Auth Middleware

Protect routes and refresh sessions in middleware

**When to use**: You need route protection or session refresh

// middleware.ts
import { createServerClient } from '@supabase/ssr'
import { NextResponse, type NextRequest } from 'next/server'

export async function middleware(request: NextRequest) {
  let response = NextResponse.next({ request })

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return request.cookies.getAll()
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value, options }) => {
            response.cookies.set(name, value, options)
          })
        },
      },
    }
  )

  // Refresh session if expired
  const { data: { user } } = await supabase.auth.getUser()

  // Protect dashboard routes
  if (request.nextUrl.pathname.startsWith('/dashboard') && !user) {
    return NextResponse.redirect(new URL('/login', request.url))
  }

  return response
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
}

### Auth Callback Route

Handle OAuth callback and exchange code for session

**When to use**: Using OAuth providers (Google, GitHub, etc.)

// app/auth/callback/route.ts
import { createClient } from '@/lib/supabase/server'
import { NextResponse } from 'next/server'

export async function GET(request: Request) {
  const { searchParams, origin } = new URL(re

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Expert integration of Supabase Auth with Next.js App Router

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Next.js + Supabase Auth
- Para tarefas relacionadas a nextjs supabase auth

## Diretrizes Específicas

