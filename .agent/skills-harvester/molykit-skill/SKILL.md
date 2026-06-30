---
name: molykit-skill
description: Best practices for building AI chat interfaces with Makepad using MolyKit - a toolkit for cross-platform AI chat applications.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# MolyKit Skill

## Backstory

Você é um agente especializado em MolyKit Skill.

## Contexto Original da Skill
MolyKit Skill

## Instruções
---
name: molykit
description: |
  CRITICAL: Use for MolyKit AI chat toolkit. Triggers on:
  BotClient, OpenAI, SSE streaming, AI chat, molykit,
  PlatformSend, spawn(), ThreadToken, cross-platform async,
  Chat widget, Messages, PromptInput, Avatar, LLM
risk: unknown
source: community
---

# MolyKit Skill

Best practices for building AI chat interfaces with Makepad using MolyKit - a toolkit for cross-platform AI chat applications.

**Source codebase**: `/Users/zhangalex/Work/Projects/FW/robius/moly/moly-kit`

## When to Use

Use this skill when:
- Building AI chat interfaces with Makepad
- Integrating OpenAI or other LLM APIs
- Implementing cross-platform async for native and WASM
- Creating chat widgets (messages, prompts, avatars)
- Handling SSE streaming responses
- Keywords: molykit, moly-kit, ai chat, bot client, openai makepad, chat widget, sse streaming

## Overview

MolyKit provides:
- Cross-platform async utilities (PlatformSend, spawn(), ThreadToken)
- Ready-to-use chat widgets (Chat, Messages, PromptInput, Avatar)
- BotClient trait for AI provider integration
- OpenAI-compatible client with SSE streaming
- Protocol types for messages, bots, and tool calls
- MCP (Model Context Protocol) support

## Cross-Platform Async Patterns

### PlatformSend - Send Only on Native

```rust
/// Implies Send only on native platforms, not on WASM
/// - On native: implemented by types that implement Send
/// - On WASM: implemented by ALL types
pub trait PlatformSend: PlatformSendInner {}

/// Boxed future type for cross-platform use
pub type BoxPlatformSendFuture<'a, T> = Pin<Box<dyn PlatformSendFuture<Output = T> + 'a>>;

/// Boxed stream type for cross-platform use
pub type BoxPlatformSendStream<'a, T> = Pin<Box<dyn PlatformSendStream<Item = T> + 'a>>;
```

### Platform-Agnostic Spawning

```rust
/// Runs a future independently
/// - Uses tokio on native (requires Send)
/// - Uses wasm-bindgen-futures on WASM (no Send required)
pub fn spawn(fut: impl PlatformSendFuture<Output = ()> + 'static);

// Usage
spawn(async move {
    let result = fetch_data().await;
    Cx::post_action(DataReady(result));
    SignalToUI::set_ui_signal();
});
```

### Task Cancellation with AbortOnDropHandle

```rust
/// Handle that aborts its future when dropped
pub struct AbortOnDropHandle(AbortHandle);

// Usage - task cancelled when widget dropped
#[rust]
task_handle: Option<AbortOnDropHandle>,

fn start_task(&mut self) {
    let (future, handle) = abort_on_drop(async move {
        // async work...
    });
    self.task_handle = Some(handle);
    spawn(async move { let _ = future.await; });
}
```

### ThreadToken for Non-Send Types on WASM

```rust
/// Store non-Send value in thread-local, access via token
pub struct ThreadToken<T: 'static>;

impl<T> ThreadToken<T> {
    pub fn new(value: T) -> Self;
    pub fn peek<R>(&self, f: impl FnOnce(&T) -> R) -> R;
    pub fn peek_mut<R>(&self, f: impl FnOnce(&mut T) -> R) -> R;
}

// Usage - wrap non-Send type for use across Send

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Best practices for building AI chat interfaces with Makepad using MolyKit - a toolkit for cross-platform AI chat applications.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em MolyKit Skill
- Para tarefas relacionadas a molykit skill

## Diretrizes Específicas

