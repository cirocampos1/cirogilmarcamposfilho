---
name: robius-app-architecture-skill
description: Best practices for structuring Makepad applications based on the Robrix and Moly codebases - production applications built with Makepad and Robius framework.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Robius App Architecture Skill

## Backstory

Você é um agente especializado em Robius App Architecture Skill.

## Contexto Original da Skill
Robius App Architecture Skill

## Instruções
---
name: robius-app-architecture
description: |
  CRITICAL: Use for Robius app architecture patterns. Triggers on:
  Tokio, async, submit_async_request, 异步, 架构,
  SignalToUI, Cx::post_action, worker task,
  app structure, MatchEvent, handle_startup
risk: unknown
source: community
---

# Robius App Architecture Skill

Best practices for structuring Makepad applications based on the Robrix and Moly codebases - production applications built with Makepad and Robius framework.

**Source codebases:**
- **Robrix**: Matrix chat client - complex sync/async with background subscriptions
- **Moly**: AI chat application - cross-platform (native + WASM) with streaming APIs

## When to Use

Use this skill when:
- Building a Makepad application with async backend integration
- Designing sync/async communication patterns in Makepad
- Structuring a Robius-style application
- Keywords: robrix, robius, makepad app structure, async makepad, tokio makepad

## Production Patterns

For production-ready async patterns, see the `_base/` directory:

| Pattern | Description |
|---------|-------------|
| 08-async-loading | Async data loading with loading states |
| 09-streaming-results | Incremental results with SignalToUI |
| 13-tokio-integration | Full tokio runtime integration |

## Core Architecture Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                     UI Thread (Makepad)                     │
│  ┌─────────┐     ┌──────────┐     ┌──────────────────────┐ │
│  │   App   │────▶│ WidgetRef │────▶│ Widget Tree (View)  │ │
│  │ State   │     │    ui     │     │ Scope::with_data()  │ │
│  └────┬────┘     └──────────┘     └──────────────────────┘ │
│       │                                                     │
│       │ submit_async_request()                              │
│       ▼                                                     │
│  ┌─────────────────┐          ┌─────────────────────────┐  │
│  │ REQUEST_SENDER  │─────────▶│  Crossbeam SegQueue     │  │
│  │ (MPSC Channel)  │          │  (Lock-free Updates)    │  │
│  └─────────────────┘          └─────────────────────────┘  │
└───────────────────────────────────┬─────────────────────────┘
                                    │
                    SignalToUI::set_ui_signal()
                                    │
┌───────────────────────────────────┴─────────────────────────┐
│                   Tokio Runtime (Async)                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           worker_task (Request Handler)               │   │
│  │  - Receives Request from UI                           │   │
│  │  - Spawns async tasks per request                     │   │
│  │  - Posts actions back via Cx::post_action()           │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         Per-Item Subscriber Tasks                     │   │
│  │  - Listens to external dat

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Best practices for structuring Makepad applications based on the Robrix and Moly codebases - production applications built with Makepad and Robius framework.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Robius App Architecture Skill
- Para tarefas relacionadas a robius app architecture skill

## Diretrizes Específicas

