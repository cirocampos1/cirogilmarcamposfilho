---
name: azureai-voicelive-javascripttypescript
description: Real-time voice AI SDK for building bidirectional voice assistants with Azure AI in Node.js and browser environments.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# @azure/ai-voicelive (JavaScript/TypeScript)

## Backstory

Você é um agente especializado em @azure/ai-voicelive (JavaScript/TypeScript).

## Contexto Original da Skill
@azure/ai-voicelive (JavaScript/TypeScript)

## Instruções
---
name: azure-ai-voicelive-ts
description: Azure AI Voice Live SDK for JavaScript/TypeScript. Build real-time voice AI applications with bidirectional WebSocket communication.
risk: unknown
source: community
date_added: '2026-02-27'
---

# @azure/ai-voicelive (JavaScript/TypeScript)

Real-time voice AI SDK for building bidirectional voice assistants with Azure AI in Node.js and browser environments.

## Installation

```bash
npm install @azure/ai-voicelive @azure/identity
# TypeScript users
npm install @types/node
```

**Current Version**: 1.0.0-beta.3

**Supported Environments**:
- Node.js LTS versions (20+)
- Modern browsers (Chrome, Firefox, Safari, Edge)

## Environment Variables

```bash
AZURE_VOICELIVE_ENDPOINT=https://<resource>.cognitiveservices.azure.com
# Optional: API key if not using Entra ID
AZURE_VOICELIVE_API_KEY=<your-api-key>
# Optional: Logging
AZURE_LOG_LEVEL=info
```

## Authentication

### Microsoft Entra ID (Recommended)

```typescript
import { DefaultAzureCredential } from "@azure/identity";
import { VoiceLiveClient } from "@azure/ai-voicelive";

const credential = new DefaultAzureCredential();
const endpoint = "https://your-resource.cognitiveservices.azure.com";

const client = new VoiceLiveClient(endpoint, credential);
```

### API Key

```typescript
import { AzureKeyCredential } from "@azure/core-auth";
import { VoiceLiveClient } from "@azure/ai-voicelive";

const endpoint = "https://your-resource.cognitiveservices.azure.com";
const credential = new AzureKeyCredential("your-api-key");

const client = new VoiceLiveClient(endpoint, credential);
```

## Client Hierarchy

```
VoiceLiveClient
└── VoiceLiveSession (WebSocket connection)
    ├── updateSession()      → Configure session options
    ├── subscribe()          → Event handlers (Azure SDK pattern)
    ├── sendAudio()          → Stream audio input
    ├── addConversationItem() → Add messages/function outputs
    └── sendEvent()          → Send raw protocol events
```

## Quick Start

```typescript
import { DefaultAzureCredential } from "@azure/identity";
import { VoiceLiveClient } from "@azure/ai-voicelive";

const credential = new DefaultAzureCredential();
const endpoint = process.env.AZURE_VOICELIVE_ENDPOINT!;

// Create client and start session
const client = new VoiceLiveClient(endpoint, credential);
const session = await client.startSession("gpt-4o-mini-realtime-preview");

// Configure session
await session.updateSession({
  modalities: ["text", "audio"],
  instructions: "You are a helpful AI assistant. Respond naturally.",
  voice: {
    type: "azure-standard",
    name: "en-US-AvaNeural",
  },
  turnDetection: {
    type: "server_vad",
    threshold: 0.5,
    prefixPaddingMs: 300,
    silenceDurationMs: 500,
  },
  inputAudioFormat: "pcm16",
  outputAudioFormat: "pcm16",
});

// Subscribe to events
const subscription = session.subscribe({
  onResponseAudioDelta: async (event, context) => {
    // Handle streaming audio output
    const audioData = event.delt

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Real-time voice AI SDK for building bidirectional voice assistants with Azure AI in Node.js and browser environments.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em @azure/ai-voicelive (JavaScript/TypeScript)
- Para tarefas relacionadas a azureai voicelive javascripttypescript

## Diretrizes Específicas

