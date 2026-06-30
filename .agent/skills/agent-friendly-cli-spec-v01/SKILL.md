---
name: agent-friendly-cli-spec-v01
description: When building or modifying CLI tools, follow these rules to make them safe and reliable for AI agents to use.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Friendly CLI Spec v0.1

## Backstory

Você é um agente especializado em Friendly CLI Spec v0.1.

## Contexto Original da Skill
Agent-Friendly CLI Spec v0.1

## Instruções
---
name: ai-native-cli
description: "Design spec with 98 rules for building CLI tools that AI agents can safely use. Covers structured JSON output, error handling, input contracts, safety guardrails, exit codes, and agent self-description."
risk: safe
source: https://github.com/ChaosRealmsAI/agent-cli-spec
date_added: "2026-03-15"
---

# Agent-Friendly CLI Spec v0.1

When building or modifying CLI tools, follow these rules to make them safe and
reliable for AI agents to use.

## Overview

A comprehensive design specification for building AI-native CLI tools. It defines
98 rules across three certification levels (Agent-Friendly, Agent-Ready, Agent-Native)
with prioritized requirements (P0/P1/P2). The spec covers structured JSON output,
error handling, input contracts, safety guardrails, exit codes, self-description,
and a feedback loop via a built-in issue system.

## When to Use This Skill

- Use when building a new CLI tool that AI agents will invoke
- Use when retrofitting an existing CLI to be agent-friendly
- Use when designing command-line interfaces for automation pipelines
- Use when auditing a CLI tool's compliance with agent-safety standards

## Core Philosophy

1. **Agent-first** -- default output is JSON; human-friendly is opt-in via `--human`
2. **Agent is untrusted** -- validate all input at the same level as a public API
3. **Fail-Closed** -- when validation logic itself errors, deny by default
4. **Verifiable** -- every rule is written so it can be automatically checked

## Layer Model

This spec uses two orthogonal axes:

- **Layer** answers rollout scope: `core`, `recommended`, `ecosystem`
- **Priority** answers severity: `P0`, `P1`, `P2`

Use layers for migration and certification:

- **core** -- execution contract: JSON, errors, exit codes, stdout/stderr, safety
- **recommended** -- better machine UX: self-description, explicit modes, richer schemas
- **ecosystem** -- agent-native integration: `agent/`, `skills`, `issue`, inline context

Certification maps to layers:

- **Agent-Friendly** -- all `core` rules pass
- **Agent-Ready** -- all `core` + `recommended` rules pass
- **Agent-Native** -- all layers pass

## How It Works

### Step 1: Output Mode

Default is agent mode (JSON). Explicit flags to switch:

```bash
$ mycli list              # default = JSON output (agent mode)
$ mycli list --human      # human-friendly: colored, tables, formatted
$ mycli list --agent      # explicit agent mode (override config if needed)
```

- **Default (no flag)** -- JSON to stdout. Agent never needs to add a flag.
- **--human** -- human-friendly format (colors, tables, progress bars)
- **--agent** -- explicit JSON mode (useful when env/config overrides default)

### Step 2: agent/ Directory Convention

Every CLI tool MUST have an `agent/` directory at its project root. This is the
tool's identity and behavior contract for AI agents.

```
agent/
  brief.md          # One paragraph: who am I, what can I do
  rules/            # Behavior constr

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

When building or modifying CLI tools, follow these rules to make them safe and reliable for AI agents to use.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Friendly CLI Spec v0.1
- Para tarefas relacionadas a agent friendly cli spec v01

## Diretrizes Específicas

