---
name: azure-ai-voice-live-sdk
description: Build real-time voice AI applications with bidirectional WebSocket communication.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure AI Voice Live SDK

## Backstory

Você é um agente especializado em Azure AI Voice Live SDK.

## Contexto Original da Skill
Azure AI Voice Live SDK

## Instruções
---
name: azure-ai-voicelive-py
description: "Build real-time voice AI applications with bidirectional WebSocket communication."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure AI Voice Live SDK

Build real-time voice AI applications with bidirectional WebSocket communication.

## Installation

```bash
pip install azure-ai-voicelive aiohttp azure-identity
```

## Environment Variables

```bash
AZURE_COGNITIVE_SERVICES_ENDPOINT=https://<region>.api.cognitive.microsoft.com
# For API key auth (not recommended for production)
AZURE_COGNITIVE_SERVICES_KEY=<api-key>
```

## Authentication

**DefaultAzureCredential (preferred)**:
```python
from azure.ai.voicelive.aio import connect
from azure.identity.aio import DefaultAzureCredential

async with connect(
    endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
    credential=DefaultAzureCredential(),
    model="gpt-4o-realtime-preview",
    credential_scopes=["https://cognitiveservices.azure.com/.default"]
) as conn:
    ...
```

**API Key**:
```python
from azure.ai.voicelive.aio import connect
from azure.core.credentials import AzureKeyCredential

async with connect(
    endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["AZURE_COGNITIVE_SERVICES_KEY"]),
    model="gpt-4o-realtime-preview"
) as conn:
    ...
```

## Quick Start

```python
import asyncio
import os
from azure.ai.voicelive.aio import connect
from azure.identity.aio import DefaultAzureCredential

async def main():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=DefaultAzureCredential(),
        model="gpt-4o-realtime-preview",
        credential_scopes=["https://cognitiveservices.azure.com/.default"]
    ) as conn:
        # Update session with instructions
        await conn.session.update(session={
            "instructions": "You are a helpful assistant.",
            "modalities": ["text", "audio"],
            "voice": "alloy"
        })
        
        # Listen for events
        async for event in conn:
            print(f"Event: {event.type}")
            if event.type == "response.audio_transcript.done":
                print(f"Transcript: {event.transcript}")
            elif event.type == "response.done":
                break

asyncio.run(main())
```

## Core Architecture

### Connection Resources

The `VoiceLiveConnection` exposes these resources:

| Resource | Purpose | Key Methods |
|----------|---------|-------------|
| `conn.session` | Session configuration | `update(session=...)` |
| `conn.response` | Model responses | `create()`, `cancel()` |
| `conn.input_audio_buffer` | Audio input | `append()`, `commit()`, `clear()` |
| `conn.output_audio_buffer` | Audio output | `clear()` |
| `conn.conversation` | Conversation state | `item.create()`, `item.delete()`, `item.truncate()` |
| `conn.transcription_session` | Transcription config | `update(session=...)` |

## Session Configuration

`

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Build real-time voice AI applications with bidirectional WebSocket communication.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure AI Voice Live SDK
- Para tarefas relacionadas a azure ai voice live sdk

## Diretrizes Específicas

