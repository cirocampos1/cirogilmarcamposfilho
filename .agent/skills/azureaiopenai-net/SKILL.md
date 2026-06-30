---
name: azureaiopenai-net
description: Client library for Azure OpenAI Service providing access to OpenAI models including GPT-4, GPT-4o, embeddings, DALL-E, and Whisper.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.AI.OpenAI (.NET)

## Backstory

Você é um agente especializado em Azure.AI.OpenAI (.NET).

## Contexto Original da Skill
Azure.AI.OpenAI (.NET)

## Instruções
---
name: azure-ai-openai-dotnet
description: Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embeddings, image generation, audio transcription, and assistants.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.AI.OpenAI (.NET)

Client library for Azure OpenAI Service providing access to OpenAI models including GPT-4, GPT-4o, embeddings, DALL-E, and Whisper.

## Installation

```bash
dotnet add package Azure.AI.OpenAI

# For OpenAI (non-Azure) compatibility
dotnet add package OpenAI
```

**Current Version**: 2.1.0 (stable)

## Environment Variables

```bash
AZURE_OPENAI_ENDPOINT=https://<resource-name>.openai.azure.com
AZURE_OPENAI_API_KEY=<api-key>                    # For key-based auth
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini          # Your deployment name
```

## Client Hierarchy

```
AzureOpenAIClient (top-level)
├── GetChatClient(deploymentName)      → ChatClient
├── GetEmbeddingClient(deploymentName) → EmbeddingClient
├── GetImageClient(deploymentName)     → ImageClient
├── GetAudioClient(deploymentName)     → AudioClient
└── GetAssistantClient()               → AssistantClient
```

## Authentication

### API Key Authentication

```csharp
using Azure;
using Azure.AI.OpenAI;

AzureOpenAIClient client = new(
    new Uri(Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")!),
    new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY")!));
```

### Microsoft Entra ID (Recommended for Production)

```csharp
using Azure.Identity;
using Azure.AI.OpenAI;

AzureOpenAIClient client = new(
    new Uri(Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")!),
    new DefaultAzureCredential());
```

### Using OpenAI SDK Directly with Azure

```csharp
using Azure.Identity;
using OpenAI;
using OpenAI.Chat;
using System.ClientModel.Primitives;

#pragma warning disable OPENAI001

BearerTokenPolicy tokenPolicy = new(
    new DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default");

ChatClient client = new(
    model: "gpt-4o-mini",
    authenticationPolicy: tokenPolicy,
    options: new OpenAIClientOptions()
    {
        Endpoint = new Uri("https://YOUR-RESOURCE.openai.azure.com/openai/v1")
    });
```

## Chat Completions

### Basic Chat

```csharp
using Azure.AI.OpenAI;
using OpenAI.Chat;

AzureOpenAIClient azureClient = new(
    new Uri(endpoint),
    new DefaultAzureCredential());

ChatClient chatClient = azureClient.GetChatClient("gpt-4o-mini");

ChatCompletion completion = chatClient.CompleteChat(
[
    new SystemChatMessage("You are a helpful assistant."),
    new UserChatMessage("What is Azure OpenAI?")
]);

Console.WriteLine(completion.Content[0].Text);
```

### Async Chat

```csharp
ChatCompletion completion = await chatClient.CompleteChatAsync(
[
    new SystemChatMessage("You are a helpful assistant."),
    new UserChatMessage("Explain cloud computing in simple terms.")
]);

Console.WriteLine($"Response: {co

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Client library for Azure OpenAI Service providing access to OpenAI models including GPT-4, GPT-4o, embeddings, DALL-E, and Whisper.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.AI.OpenAI (.NET)
- Para tarefas relacionadas a azureaiopenai net

## Diretrizes Específicas

