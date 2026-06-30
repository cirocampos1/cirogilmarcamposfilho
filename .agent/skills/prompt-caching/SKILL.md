---
name: prompt-caching
description: Caching strategies for LLM prompts including Anthropic prompt caching, response caching, and CAG (Cache Augmented Generation)
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# mpt Caching

## Backstory

Você é um agente especializado em mpt Caching.

## Contexto Original da Skill
Prompt Caching

## Instruções
---
name: prompt-caching
description: Caching strategies for LLM prompts including Anthropic prompt
  caching, response caching, and CAG (Cache Augmented Generation)
risk: none
source: vibeship-spawner-skills (Apache 2.0)
date_added: 2026-02-27
---

# Prompt Caching

Caching strategies for LLM prompts including Anthropic prompt caching, response caching, and CAG (Cache Augmented Generation)

## Capabilities

- prompt-cache
- response-cache
- kv-cache
- cag-patterns
- cache-invalidation

## Prerequisites

- Knowledge: Caching fundamentals, LLM API usage, Hash functions
- Skills_recommended: context-window-management

## Scope

- Does_not_cover: CDN caching, Database query caching, Static asset caching
- Boundaries: Focus is LLM-specific caching, Covers prompt and response caching

## Ecosystem

### Primary_tools

- Anthropic Prompt Caching - Native prompt caching in Claude API
- Redis - In-memory cache for responses
- OpenAI Caching - Automatic caching in OpenAI API

## Patterns

### Anthropic Prompt Caching

Use Claude's native prompt caching for repeated prefixes

**When to use**: Using Claude API with stable system prompts or context

import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic();

// Cache the stable parts of your prompt
async function queryWithCaching(userQuery: string) {
    const response = await client.messages.create({
        model: "claude-sonnet-4-20250514",
        max_tokens: 1024,
        system: [
            {
                type: "text",
                text: LONG_SYSTEM_PROMPT,  // Your detailed instructions
                cache_control: { type: "ephemeral" }  // Cache this!
            },
            {
                type: "text",
                text: KNOWLEDGE_BASE,  // Large static context
                cache_control: { type: "ephemeral" }
            }
        ],
        messages: [
            { role: "user", content: userQuery }  // Dynamic part
        ]
    });

    // Check cache usage
    console.log(`Cache read: ${response.usage.cache_read_input_tokens}`);
    console.log(`Cache write: ${response.usage.cache_creation_input_tokens}`);

    return response;
}

// Cost savings: 90% reduction on cached tokens
// Latency savings: Up to 2x faster

### Response Caching

Cache full LLM responses for identical or similar queries

**When to use**: Same queries asked repeatedly

import { createHash } from 'crypto';
import Redis from 'ioredis';

const redis = new Redis(process.env.REDIS_URL);

class ResponseCache {
    private ttl = 3600;  // 1 hour default

    // Exact match caching
    async getCached(prompt: string): Promise<string | null> {
        const key = this.hashPrompt(prompt);
        return await redis.get(`response:${key}`);
    }

    async setCached(prompt: string, response: string): Promise<void> {
        const key = this.hashPrompt(prompt);
        await redis.set(`response:${key}`, response, 'EX', this.ttl);
    }

    private hashPrompt(prompt: string): string {
        ret

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Caching strategies for LLM prompts including Anthropic prompt caching, response caching, and CAG (Cache Augmented Generation)

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em mpt Caching
- Para tarefas relacionadas a prompt caching

## Diretrizes Específicas

