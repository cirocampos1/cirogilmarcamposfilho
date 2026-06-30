---
name: crypto-bd-agent-autonomous-business-development-fo
description: > Production-tested patterns for building AI agents that autonomously discover, > evaluate, and acquire token listings for cryptocurrency exchanges.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Crypto BD Agent — Autonomous Business Development for Exchanges

## Backstory

Você é um agente especializado em Crypto BD Agent — Autonomous Business Development for Exchanges.

## Contexto Original da Skill
Crypto BD Agent — Autonomous Business Development for Exchanges

## Instruções
---
name: crypto-bd-agent
description: "Production-tested patterns for building AI agents that autonomously discover, > evaluate, and acquire token listings for cryptocurrency exchanges."
risk: safe
source: community
tags: null
date_added: '2026-02-27'
---

# Crypto BD Agent — Autonomous Business Development for Exchanges

> Production-tested patterns for building AI agents that autonomously discover,
> evaluate, and acquire token listings for cryptocurrency exchanges.

## Overview

This skill teaches AI agents systematic crypto business development: discover
promising tokens across chains, score them with a 100-point weighted system,
verify safety through wallet forensics, and manage outreach pipelines with
human-in-the-loop oversight.

Built from production experience running Buzz BD Agent by SolCex Exchange —
an autonomous agent on decentralized infrastructure with 13 intelligence
sources, x402 micropayments, and dual-chain ERC-8004 registration.

Reference implementation: https://github.com/buzzbysolcex/buzz-bd-agent

## When to Use This Skill

- Building an AI agent for crypto/DeFi business development
- Creating token evaluation and scoring systems
- Implementing multi-chain scanning pipelines
- Setting up autonomous payment workflows (x402)
- Designing wallet forensics for deployer analysis
- Managing BD pipelines with human-in-the-loop
- Registering agents on-chain via ERC-8004
- Implementing cost-efficient LLM cascades

## Do Not Use When

- Building trading bots (this is BD, not trading)
- Creating DeFi protocols or smart contracts
- Non-crypto business development

---

## Architecture
```text
Intelligence Sources (Free + Paid via x402)
        |
        v
  Scoring Engine (100-point weighted)
        |
        v
  Wallet Forensics (deployer verification)
        |
        v
  Pipeline Manager (10-stage tracked)
        |
        v
  Outreach Drafts → Human Approval → Send
```

### LLM Cascade Pattern

Route tasks to the cheapest model that handles them correctly:
```text
Fast/cheap model (routine: tweets, forum posts, pipeline updates)
    ↓ fallback on quality issues
Free API models (scanning, initial scoring, system tasks)
    ↓ fallback
Mid-tier model (outreach drafts, deeper analysis)
    ↓ fallback
Premium model (strategy, wallet forensics, final outreach)
```

Run a quality gate (10+ test cases) before promoting any new model.

---

## 1. Intelligence Gathering

### Free-First Principle
Always exhaust free data before paying. Target: $0/day for 90% of intelligence.

### Recommended Source Categories

| Category | What to Track | Example Sources |
|----------|--------------|-----------------|
| DEX Data | Prices, liquidity, pairs, chain coverage | DexScreener, GeckoTerminal |
| AI Momentum | Trending tokens, catalysts | AIXBT or similar trackers |
| Smart Money | VC follows, KOL accumulation | leak.me, Nansen free, Arkham |
| Contract Safety | Rug scores, LP lock, authorities | RugCheck |
| Wallet Forensics | Deployer analysis, f

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

> Production-tested patterns for building AI agents that autonomously discover, > evaluate, and acquire token listings for cryptocurrency exchanges.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Crypto BD Agent — Autonomous Business Development for Exchanges
- Para tarefas relacionadas a crypto bd agent autonomous business development fo

## Diretrizes Específicas

