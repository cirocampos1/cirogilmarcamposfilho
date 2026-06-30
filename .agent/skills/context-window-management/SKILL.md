---
name: context-window-management
description: Strategies for managing LLM context windows including summarization, trimming, routing, and avoiding context rot
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Context Window Management

## Backstory

Você é um agente especializado em Context Window Management.

## Contexto Original da Skill
Context Window Management

## Instruções
---
name: context-window-management
description: Strategies for managing LLM context windows including
  summarization, trimming, routing, and avoiding context rot
risk: unknown
source: vibeship-spawner-skills (Apache 2.0)
date_added: 2026-02-27
---

# Context Window Management

Strategies for managing LLM context windows including summarization, trimming, routing, and avoiding context rot

## Capabilities

- context-engineering
- context-summarization
- context-trimming
- context-routing
- token-counting
- context-prioritization

## Prerequisites

- Knowledge: LLM fundamentals, Tokenization basics, Prompt engineering
- Skills_recommended: prompt-engineering

## Scope

- Does_not_cover: RAG implementation details, Model fine-tuning, Embedding models
- Boundaries: Focus is context optimization, Covers strategies not specific implementations

## Ecosystem

### Primary_tools

- tiktoken - OpenAI's tokenizer for counting tokens
- LangChain - Framework with context management utilities
- Claude API - 200K+ context with caching support

## Patterns

### Tiered Context Strategy

Different strategies based on context size

**When to use**: Building any multi-turn conversation system

interface ContextTier {
    maxTokens: number;
    strategy: 'full' | 'summarize' | 'rag';
    model: string;
}

const TIERS: ContextTier[] = [
    { maxTokens: 8000, strategy: 'full', model: 'claude-3-haiku' },
    { maxTokens: 32000, strategy: 'full', model: 'claude-3-5-sonnet' },
    { maxTokens: 100000, strategy: 'summarize', model: 'claude-3-5-sonnet' },
    { maxTokens: Infinity, strategy: 'rag', model: 'claude-3-5-sonnet' }
];

async function selectStrategy(messages: Message[]): ContextTier {
    const tokens = await countTokens(messages);

    for (const tier of TIERS) {
        if (tokens <= tier.maxTokens) {
            return tier;
        }
    }
    return TIERS[TIERS.length - 1];
}

async function prepareContext(messages: Message[]): PreparedContext {
    const tier = await selectStrategy(messages);

    switch (tier.strategy) {
        case 'full':
            return { messages, model: tier.model };

        case 'summarize':
            const summary = await summarizeOldMessages(messages);
            return { messages: [summary, ...recentMessages(messages)], model: tier.model };

        case 'rag':
            const relevant = await retrieveRelevant(messages);
            return { messages: [...relevant, ...recentMessages(messages)], model: tier.model };
    }
}

### Serial Position Optimization

Place important content at start and end

**When to use**: Constructing prompts with significant context

// LLMs weight beginning and end more heavily
// Structure prompts to leverage this

function buildOptimalPrompt(components: {
    systemPrompt: string;
    criticalContext: string;
    conversationHistory: Message[];
    currentQuery: string;
}): string {
    // START: System instructions (always first)
    const parts = [components.systemPrompt];

    // CRIT

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Strategies for managing LLM context windows including summarization, trimming, routing, and avoiding context rot

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Context Window Management
- Para tarefas relacionadas a context window management

## Diretrizes Específicas

