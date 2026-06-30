---
name: azure-functions
description: "Expert patterns for Azure Functions development including isolated worker model, Durable Functions orchestration, cold start optimization, and production patterns. Covers .NET, Python, and Node.js programming models. Use when: azure function, azure functions, durable functions, azure serverless, function app."
source: vibeship-spawner-skills (Apache 2.0)
version: 3.0
architecture_focus: "Option B"
last_updated: 2026-03-28
verification_script: "scripts/verify.py"
---

# Azure Functions

## Patterns

### Isolated Worker Model (.NET)

Modern .NET execution model with process isolation

### Node.js v4 Programming Model

Modern code-centric approach for TypeScript/JavaScript

### Python v2 Programming Model

Decorator-based approach for Python functions

## Anti-Patterns

### ❌ Blocking Async Calls

### ❌ New HttpClient Per Request

### ❌ In-Process Model for New Projects

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | high | ## Use async pattern with Durable Functions |
| Issue | high | ## Use IHttpClientFactory (Recommended) |
| Issue | high | ## Always use async/await |
| Issue | medium | ## Configure maximum timeout (Consumption) |
| Issue | high | ## Use isolated worker for new projects |
| Issue | medium | ## Configure Application Insights properly |
| Issue | medium | ## Check extension bundle (most common) |
| Issue | medium | ## Add warmup trigger to initialize your code |


## 🚀 Option B: Efficiency Guidelines (MANDATORY)

1. **Direct Action**: Never explain what you are going to do. Just do it.
2. **Token Economy**: Minimize chatter. Use the most concise tool calls possible.
3. **Verification First**: Run validation scripts immediately after any change.
4. **GPU Acceleration**: Use local GPU/Ollama for heavy analysis tasks when possible.
