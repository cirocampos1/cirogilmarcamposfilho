---
name: agentflow
description: AgentFlow turns your existing Kanban board into a fully autonomous AI development pipeline. Instead of building custom orchestration infrastructure, it treats your project management tool (Asana, GitH
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Flow

## Backstory

Você é um agente especializado em Flow.

## Contexto Original da Skill
AgentFlow

## Instruções
---
name: agentflow
description: "Orchestrate autonomous AI development pipelines through your Kanban board (Asana, GitHub Projects, Linear). Manages multi-worker Claude Code dispatch, deterministic quality gates, adversarial review, per-task cost tracking, and crash-proof pipeline execution."
risk: safe
source: community
date_added: "2026-04-02"
---

# AgentFlow

## Overview

AgentFlow turns your existing Kanban board into a fully autonomous AI development pipeline. Instead of building custom orchestration infrastructure, it treats your project management tool (Asana, GitHub Projects, Linear) as a distributed state machine — tasks move through stages, AI agents read and write state via comments, and humans intervene through the same UI they already use.

The result is complete pipeline observability from your phone, free crash recovery (state lives in your PM tool, not in memory), and human override at any point by dragging a card.

## When to Use This Skill

- Use when you need to orchestrate multiple Claude Code workers across a full development lifecycle (build, review, test, integrate)
- Use when you want deterministic quality gates (tsc/eslint/tests) before AI review on AI-generated code
- Use when you want full pipeline visibility from your Kanban board or phone
- Use when running a solo or team project that needs autonomous task dispatch with cost tracking
- Use when you need crash-proof orchestration that survives session restarts

## Core Concepts

### 7-Stage Kanban Pipeline

Tasks flow through: Backlog, Research, Build, Review, Test, Integrate, Done. Each stage has specific gates. The Kanban board IS the orchestration layer — no separate database, no message queue, no custom infrastructure.

### Stateless Orchestrator

A crontab-driven one-shot sweep runs every 15 minutes. No daemon, no session dependency. If it crashes, the next sweep picks up where it left off because all state lives in your PM tool.

### Deterministic Before Probabilistic

Hard gates (tsc + eslint + tests) run before any AI review, catching roughly 60% of issues at near-zero cost. AI review comes after, as a second layer.

### Adversarial Review

A different AI agent reviews code and must list 3 things wrong before deciding to pass. This prevents rubber-stamp approvals.

### Transitive Priority Dispatch

Tasks that unblock the most downstream work get built first, automatically computing the critical path.

## Skills / Commands

### `/spec-to-board`
Decomposes a SPEC.md into atomic tasks on your Kanban board with dependencies mapped.

### `/sdlc-orchestrate`
Dispatches tasks to workers based on transitive priority and conflict detection. Runs as a crontab sweep.

### `/sdlc-worker --slot <N>`
Runs a worker in a terminal slot that picks up tasks, builds code, and creates PRs. Run 3-4 workers in parallel.

### `/sdlc-health`
Real-time pipeline status dashboard showing current stage, assigned agent, retry count, and accumulated cost for every task.

### `/sdlc-stop`
G

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

AgentFlow turns your existing Kanban board into a fully autonomous AI development pipeline. Instead of building custom orchestration infrastructure, it treats your project management tool (Asana, GitH

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Flow
- Para tarefas relacionadas a agentflow

## Diretrizes Específicas

