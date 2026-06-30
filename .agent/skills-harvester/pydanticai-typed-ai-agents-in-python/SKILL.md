---
name: pydanticai-typed-ai-agents-in-python
description: PydanticAI is a Python agent framework from the Pydantic team that brings the same type-safety and validation guarantees as Pydantic to LLM-based applications. It supports structured outputs (validate
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# PydanticAI — Typed AI Agents in Python

## Backstory

Você é um agente especializado em PydanticAI — Typed AI Agents in Python.

## Contexto Original da Skill
PydanticAI — Typed AI Agents in Python

## Instruções
---
name: pydantic-ai
description: "Build production-ready AI agents with PydanticAI — type-safe tool use, structured outputs, dependency injection, and multi-model support."
category: ai-agents
risk: safe
source: community
date_added: "2026-03-18"
author: suhaibjanjua
tags: [pydantic-ai, ai-agents, llm, openai, anthropic, gemini, tool-use, structured-output, python]
tools: [claude, cursor, gemini]
---

# PydanticAI — Typed AI Agents in Python

## Overview

PydanticAI is a Python agent framework from the Pydantic team that brings the same type-safety and validation guarantees as Pydantic to LLM-based applications. It supports structured outputs (validated with Pydantic models), dependency injection for testability, streamed responses, multi-turn conversations, and tool use — across OpenAI, Anthropic, Google Gemini, Groq, Mistral, and Ollama. Use this skill when building production AI agents, chatbots, or LLM pipelines where correctness and testability matter.

## When to Use This Skill

- Use when building Python AI agents that call tools and return structured data
- Use when you need validated, typed LLM outputs (not raw strings)
- Use when you want to write unit tests for agent logic without hitting a real LLM
- Use when switching between LLM providers without rewriting agent code
- Use when the user asks about `Agent`, `@agent.tool`, `RunContext`, `ModelRetry`, or `result_type`

## How It Works

### Step 1: Installation

```bash
pip install pydantic-ai

# Install extras for specific providers
pip install 'pydantic-ai[openai]'       # OpenAI / Azure OpenAI
pip install 'pydantic-ai[anthropic]'    # Anthropic Claude
pip install 'pydantic-ai[gemini]'       # Google Gemini
pip install 'pydantic-ai[groq]'         # Groq
pip install 'pydantic-ai[vertexai]'     # Google Vertex AI
```

### Step 2: A Minimal Agent

```python
from pydantic_ai import Agent

# Simple agent — returns a plain string
agent = Agent(
    'anthropic:claude-sonnet-4-6',
    system_prompt='You are a helpful assistant. Be concise.',
)

result = agent.run_sync('What is the capital of Japan?')
print(result.data)  # "Tokyo"
print(result.usage())  # Usage(requests=1, request_tokens=..., response_tokens=...)
```

### Step 3: Structured Output with Pydantic Models

```python
from pydantic import BaseModel
from pydantic_ai import Agent

class MovieReview(BaseModel):
    title: str
    year: int
    rating: float  # 0.0 to 10.0
    summary: str
    recommended: bool

agent = Agent(
    'openai:gpt-4o',
    result_type=MovieReview,
    system_prompt='You are a film critic. Return structured reviews.',
)

result = agent.run_sync('Review Inception (2010)')
review = result.data  # Fully typed MovieReview instance
print(f"{review.title} ({review.year}): {review.rating}/10")
print(f"Recommended: {review.recommended}")
```

### Step 4: Tool Use

Register tools with `@agent.tool` — the LLM can call them during a run:

```python
from pydantic_ai import Agent, RunContext
from pydantic import BaseMod

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

PydanticAI is a Python agent framework from the Pydantic team that brings the same type-safety and validation guarantees as Pydantic to LLM-based applications. It supports structured outputs (validate

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em PydanticAI — Typed AI Agents in Python
- Para tarefas relacionadas a pydanticai typed ai agents in python

## Diretrizes Específicas

