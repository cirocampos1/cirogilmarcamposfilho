---
name: context-agent
description: Agente de contexto para continuidade entre sessoes. Salva resumos, decisoes, tarefas pendentes e carrega briefing automatico na sessao seguinte.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Context Agent

## Backstory

Você é um agente especializado em Context Agent.

## Contexto Original da Skill
Context Agent

## Instruções
---
name: context-agent
description: Agente de contexto para continuidade entre sessoes. Salva resumos, decisoes, tarefas pendentes e carrega briefing automatico na sessao seguinte.
risk: safe
source: community
date_added: '2026-03-06'
author: renat
tags:
- context
- session-management
- continuity
- memory
tools:
- claude-code
- antigravity
- cursor
- gemini-cli
- codex-cli
---

# Context Agent

## Overview

Agente de contexto para continuidade entre sessoes. Salva resumos, decisoes, tarefas pendentes e carrega briefing automatico na sessao seguinte.

## When to Use This Skill

- When the user mentions "salvar contexto" or related topics
- When the user mentions "salva o contexto" or related topics
- When the user mentions "proxima sessao" or related topics
- When the user mentions "briefing sessao" or related topics
- When the user mentions "resumo sessao" or related topics
- When the user mentions "continuidade sessao" or related topics

## Do Not Use This Skill When

- The task is unrelated to context agent
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

Continuidade perfeita entre sessões do Claude Code. Captura, comprime e
restaura contexto automaticamente — tópicos, decisões, tarefas, erros,
arquivos modificados e descobertas técnicas.

## Localização

```
C:\Users\renat\skills\context-agent\
├── SKILL.md
├── scripts/
│   ├── config.py               # Paths e constantes
│   ├── models.py               # Dataclasses
│   ├── session_parser.py       # Parser JSONL do Claude Code
│   ├── session_summary.py      # Gerador de resumos
│   ├── active_context.py       # Gerencia ACTIVE_CONTEXT.md
│   ├── project_registry.py     # Registro de projetos
│   ├── compressor.py           # Compressão e arquivamento
│   ├── search.py               # Busca FTS5
│   ├── context_loader.py       # Carrega contexto
│   └── context_manager.py      # CLI entry point
├── references/
│   ├── context-format.md       # Especificação de formatos
│   └── compression-rules.md    # Regras de compressão
└── data/
    ├── sessions/               # session-001.md, session-002.md, ...
    ├── archive/                # Sessões arquivadas
    ├── ACTIVE_CONTEXT.md       # Contexto consolidado (max 150 linhas)
    ├── PROJECT_REGISTRY.md     # Status de todos os projetos
    └── context.db              # SQLite FTS5 para busca
```

## Inicialização (Primeira Vez)

```bash
python C:\Users\renat\skills\context-agent\scripts\context_manager.py init
```

## Salvar Contexto Da Sessão Atual

Quando a sessão está terminando ou antes de uma tarefa longa, salvar o contexto:

```bash
python C:\Users\renat\skills\context-agent\scripts\context_manager.py save
```

O que faz:
1. Encontra o arquivo JSONL mais recente da sessão
2. Analisa todas as mensagens, tool calls e resultados
3. Gera resumo estruturado (session-NNN.md)
4. Atualiza ACTIVE_CONTEXT.md com novas informações
5. Sincroniza com MEMOR

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Agente de contexto para continuidade entre sessoes. Salva resumos, decisoes, tarefas pendentes e carrega briefing automatico na sessao seguinte.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Context Agent
- Para tarefas relacionadas a context agent

## Diretrizes Específicas

