---
name: azureaivoicelive-net
description: Real-time voice AI SDK for building bidirectional voice assistants with Azure AI.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.AI.VoiceLive (.NET)

## Backstory

Você é um agente especializado em Azure.AI.VoiceLive (.NET).

## Contexto Original da Skill
Azure.AI.VoiceLive (.NET)

## Instruções
---
name: azure-ai-voicelive-dotnet
description: Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communication.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.AI.VoiceLive (.NET)

Real-time voice AI SDK for building bidirectional voice assistants with Azure AI.

## Installation

```bash
dotnet add package Azure.AI.VoiceLive
dotnet add package Azure.Identity
dotnet add package NAudio                    # For audio capture/playback
```

**Current Versions**: Stable v1.0.0, Preview v1.1.0-beta.1

## Environment Variables

```bash
AZURE_VOICELIVE_ENDPOINT=https://<resource>.services.ai.azure.com/
AZURE_VOICELIVE_MODEL=gpt-4o-realtime-preview
AZURE_VOICELIVE_VOICE=en-US-AvaNeural
# Optional: API key if not using Entra ID
AZURE_VOICELIVE_API_KEY=<your-api-key>
```

## Authentication

### Microsoft Entra ID (Recommended)

```csharp
using Azure.Identity;
using Azure.AI.VoiceLive;

Uri endpoint = new Uri("https://your-resource.cognitiveservices.azure.com");
DefaultAzureCredential credential = new DefaultAzureCredential();
VoiceLiveClient client = new VoiceLiveClient(endpoint, credential);
```

**Required Role**: `Cognitive Services User` (assign in Azure Portal → Access control)

### API Key

```csharp
Uri endpoint = new Uri("https://your-resource.cognitiveservices.azure.com");
AzureKeyCredential credential = new AzureKeyCredential("your-api-key");
VoiceLiveClient client = new VoiceLiveClient(endpoint, credential);
```

## Client Hierarchy

```
VoiceLiveClient
└── VoiceLiveSession (WebSocket connection)
    ├── ConfigureSessionAsync()
    ├── GetUpdatesAsync() → SessionUpdate events
    ├── AddItemAsync() → UserMessageItem, FunctionCallOutputItem
    ├── SendAudioAsync()
    └── StartResponseAsync()
```

## Core Workflow

### 1. Start Session and Configure

```csharp
using Azure.Identity;
using Azure.AI.VoiceLive;

var endpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_VOICELIVE_ENDPOINT"));
var client = new VoiceLiveClient(endpoint, new DefaultAzureCredential());

var model = "gpt-4o-mini-realtime-preview";

// Start session
using VoiceLiveSession session = await client.StartSessionAsync(model);

// Configure session
VoiceLiveSessionOptions sessionOptions = new()
{
    Model = model,
    Instructions = "You are a helpful AI assistant. Respond naturally.",
    Voice = new AzureStandardVoice("en-US-AvaNeural"),
    TurnDetection = new AzureSemanticVadTurnDetection()
    {
        Threshold = 0.5f,
        PrefixPadding = TimeSpan.FromMilliseconds(300),
        SilenceDuration = TimeSpan.FromMilliseconds(500)
    },
    InputAudioFormat = InputAudioFormat.Pcm16,
    OutputAudioFormat = OutputAudioFormat.Pcm16
};

// Set modalities (both text and audio for voice assistants)
sessionOptions.Modalities.Clear();
sessionOptions.Modalities.Add(InteractionModality.Text);
sessionOptions.Modalities.Add(InteractionModality.Audio);

await session.ConfigureSessionAsync(sessionOptions);

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Real-time voice AI SDK for building bidirectional voice assistants with Azure AI.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.AI.VoiceLive (.NET)
- Para tarefas relacionadas a azureaivoicelive net

## Diretrizes Específicas

