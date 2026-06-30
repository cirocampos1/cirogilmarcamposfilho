---
name: context-engineering-fundamentals
description: Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, tool definitions, retrieve
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Context Engineering Fundamentals

## Backstory

Você é um agente especializado em Context Engineering Fundamentals.

## Contexto Original da Skill
Context Engineering Fundamentals

## Instruções
---
name: context-fundamentals
description: "Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, tool definitions, retrieved documents, message history, and tool outputs."
risk: unknown
source: community
---

# Context Engineering Fundamentals

Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, tool definitions, retrieved documents, message history, and tool outputs. Understanding context fundamentals is prerequisite to effective context engineering.

## When to Use
Activate this skill when:
- Designing new agent systems or modifying existing architectures
- Debugging unexpected agent behavior that may relate to context
- Optimizing context usage to reduce token costs or improve performance
- Onboarding new team members to context engineering concepts
- Reviewing context-related design decisions

## Core Concepts

Context comprises several distinct components, each with different characteristics and constraints. The attention mechanism creates a finite budget that constrains effective context usage. Progressive disclosure manages this constraint by loading information only as needed. The engineering discipline is curating the smallest high-signal token set that achieves desired outcomes.

## Detailed Topics

### The Anatomy of Context

**System Prompts**
System prompts establish the agent's core identity, constraints, and behavioral guidelines. They are loaded once at session start and typically persist throughout the conversation. System prompts should be extremely clear and use simple, direct language at the right altitude for the agent.

The right altitude balances two failure modes. At one extreme, engineers hardcode complex brittle logic that creates fragility and maintenance burden. At the other extreme, engineers provide vague high-level guidance that fails to give concrete signals for desired outputs or falsely assumes shared context. The optimal altitude strikes a balance: specific enough to guide behavior effectively, yet flexible enough to provide strong heuristics.

Organize prompts into distinct sections using XML tagging or Markdown headers to delineate background information, instructions, tool guidance, and output description. The exact formatting matters less as models become more capable, but structural clarity remains valuable.

**Tool Definitions**
Tool definitions specify the actions an agent can take. Each tool includes a name, description, parameters, and return format. Tool definitions live near the front of context after serialization, typically before or after the system prompt.

Tool descriptions collectively steer agent behavior. Poor descriptions force agents to guess; optimized descriptions include usage context, examples, and defaults. The consolidation principle states that 

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, tool definitions, retrieve

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Context Engineering Fundamentals
- Para tarefas relacionadas a context engineering fundamentals

## Diretrizes Específicas

