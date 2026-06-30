---
name: context-guardian
description: Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Context Guardian

## Backstory

Você é um agente especializado em Context Guardian.

## Contexto Original da Skill
Context Guardian

## Instruções
---
name: context-guardian
description: Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao.
risk: safe
source: community
date_added: '2026-03-06'
author: renat
tags:
- context
- data-integrity
- snapshots
- verification
tools:
- claude-code
- antigravity
- cursor
- gemini-cli
- codex-cli
---

# Context Guardian

## Overview

Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao.

## When to Use This Skill

- When the user mentions "compactacao contexto" or related topics
- When the user mentions "perda de contexto" or related topics
- When the user mentions "snapshot contexto" or related topics
- When the user mentions "preservar contexto" or related topics
- When the user mentions "contexto critico" or related topics
- When the user mentions "antes de compactar" or related topics

## Do Not Use This Skill When

- The task is unrelated to context guardian
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

Sistema de integridade de contexto que protege projetos tecnicoss complexos contra
perda de informacao durante compactacao automatica do Claude Code. Enquanto o
`context-agent` atua APOS as sessoes (save/load), o context-guardian atua DURANTE
a sessao, detectando quando a compactacao esta proxima e executando protocolos de
preservacao com verificacao redundante.

## Por Que Isto Existe

O Claude Code compacta automaticamente mensagens antigas quando o contexto se
aproxima do limite da janela. Essa compactacao e heuristica — ela resume mensagens
para liberar espaco, mas inevitavelmente perde detalhes. Para projetos simples,
isso funciona bem. Mas para projetos tecnicos pesados (como ecossistemas com 21+
skills, auditorias de seguranca, refatoracoes de arquitetura), a perda de um unico
detalhe pode causar regressoes, re-trabalho ou inconsistencias graves.

O context-guardian resolve isso criando uma camada de protecao PRE-compactacao:
extrai, classifica, verifica e persiste todas as informacoes criticas ANTES que a
compactacao automatica as destrua.

## Localizacao

```
C:\Users\renat\skills\context-guardian\
├── SKILL.md                          # Este arquivo
├── references/
│   ├── extraction-protocol.md        # Protocolo detalhado de extracao
│   └── verification-checklist.md     # Checklist de verificacao e redundancia
└── scripts/
    └── context_snapshot.py           # Script de snapshot automatico
```

## Integracao Com O Ecossistema

```
context-guardian (PRE-compactacao)    context-agent (POS-sessao)
         │                                    │
         ├── Detecta contexto grande          ├── Salva resumo ao final
         ├── Extrai dados criticos            ├── Atualiza ACTIVE_CONTEXT.md
         ├── Verifica integridade             ├── Sincroniza MEMORY.m

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Context Guardian
- Para tarefas relacionadas a context guardian

## Diretrizes Específicas

