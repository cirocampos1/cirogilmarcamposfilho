---
name: project-guidelines-skill-example
description: This is an example of a project-specific skill. Use this as a template for your own projects.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# ject Guidelines Skill (Example)

## Backstory

Você é um agente especializado em ject Guidelines Skill (Example).

## Contexto Original da Skill
Project Guidelines Skill (Example)

## Instruções
---
name: cc-skill-project-guidelines-example
description: "Project Guidelines Skill (Example)"
risk: unknown
source: community
date_added: "2026-02-27"
---

# Project Guidelines Skill (Example)

This is an example of a project-specific skill. Use this as a template for your own projects.

Based on a real production application: [Zenith](https://zenith.chat) - AI-powered customer discovery platform.

---

## When to Use
Reference this skill when working on the specific project it's designed for. Project skills contain:
- Architecture overview
- File structure
- Code patterns
- Testing requirements
- Deployment workflow

---

## Architecture Overview

**Tech Stack:**
- **Frontend**: Next.js 15 (App Router), TypeScript, React
- **Backend**: FastAPI (Python), Pydantic models
- **Database**: Supabase (PostgreSQL)
- **AI**: Claude API with tool calling and structured output
- **Deployment**: Google Cloud Run
- **Testing**: Playwright (E2E), pytest (backend), React Testing Library

**Services:**
```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend                            │
│  Next.js 15 + TypeScript + TailwindCSS                     │
│  Deployed: Vercel / Cloud Run                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                         Backend                             │
│  FastAPI + Python 3.11 + Pydantic                          │
│  Deployed: Cloud Run                                       │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │ Supabase │   │  Claude  │   │  Redis   │
        │ Database │   │   API    │   │  Cache   │
        └──────────┘   └──────────┘   └──────────┘
```

---

## File Structure

```
project/
├── frontend/
│   └── src/
│       ├── app/              # Next.js app router pages
│       │   ├── api/          # API routes
│       │   ├── (auth)/       # Auth-protected routes
│       │   └── workspace/    # Main app workspace
│       ├── components/       # React components
│       │   ├── ui/           # Base UI components
│       │   ├── forms/        # Form components
│       │   └── layouts/      # Layout components
│       ├── hooks/            # Custom React hooks
│       ├── lib/              # Utilities
│       ├── types/            # TypeScript definitions
│       └── config/           # Configuration
│
├── backend/
│   ├── routers/              # FastAPI route handlers
│   ├── models.py             # Pydantic models
│   ├── main.py               # FastAPI app entry
│   ├── auth_system.py        # Authentication
│   ├── database.py           # Database operations
│   ├── services/         

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

This is an example of a project-specific skill. Use this as a template for your own projects.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em ject Guidelines Skill (Example)
- Para tarefas relacionadas a project guidelines skill example

## Diretrizes Específicas

