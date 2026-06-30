---
name: azure-ai-voicelive-sdk-for-java
description: Real-time, bidirectional voice conversations with AI assistants using WebSocket technology.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure AI VoiceLive SDK for Java

## Backstory

Você é um agente especializado em Azure AI VoiceLive SDK for Java.

## Contexto Original da Skill
Azure AI VoiceLive SDK for Java

## Instruções
---
name: azure-ai-voicelive-java
description: Azure AI VoiceLive SDK for Java. Real-time bidirectional voice conversations with AI assistants using WebSocket.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure AI VoiceLive SDK for Java

Real-time, bidirectional voice conversations with AI assistants using WebSocket technology.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-ai-voicelive</artifactId>
    <version>1.0.0-beta.2</version>
</dependency>
```

## Environment Variables

```bash
AZURE_VOICELIVE_ENDPOINT=https://<resource>.openai.azure.com/
AZURE_VOICELIVE_API_KEY=<your-api-key>
```

## Authentication

### API Key

```java
import com.azure.ai.voicelive.VoiceLiveAsyncClient;
import com.azure.ai.voicelive.VoiceLiveClientBuilder;
import com.azure.core.credential.AzureKeyCredential;

VoiceLiveAsyncClient client = new VoiceLiveClientBuilder()
    .endpoint(System.getenv("AZURE_VOICELIVE_ENDPOINT"))
    .credential(new AzureKeyCredential(System.getenv("AZURE_VOICELIVE_API_KEY")))
    .buildAsyncClient();
```

### DefaultAzureCredential (Recommended)

```java
import com.azure.identity.DefaultAzureCredentialBuilder;

VoiceLiveAsyncClient client = new VoiceLiveClientBuilder()
    .endpoint(System.getenv("AZURE_VOICELIVE_ENDPOINT"))
    .credential(new DefaultAzureCredentialBuilder().build())
    .buildAsyncClient();
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| `VoiceLiveAsyncClient` | Main entry point for voice sessions |
| `VoiceLiveSessionAsyncClient` | Active WebSocket connection for streaming |
| `VoiceLiveSessionOptions` | Configuration for session behavior |

### Audio Requirements

- **Sample Rate**: 24kHz (24000 Hz)
- **Bit Depth**: 16-bit PCM
- **Channels**: Mono (1 channel)
- **Format**: Signed PCM, little-endian

## Core Workflow

### 1. Start Session

```java
import reactor.core.publisher.Mono;

client.startSession("gpt-4o-realtime-preview")
    .flatMap(session -> {
        System.out.println("Session started");
        
        // Subscribe to events
        session.receiveEvents()
            .subscribe(
                event -> System.out.println("Event: " + event.getType()),
                error -> System.err.println("Error: " + error.getMessage())
            );
        
        return Mono.just(session);
    })
    .block();
```

### 2. Configure Session Options

```java
import com.azure.ai.voicelive.models.*;
import java.util.Arrays;

ServerVadTurnDetection turnDetection = new ServerVadTurnDetection()
    .setThreshold(0.5)                    // Sensitivity (0.0-1.0)
    .setPrefixPaddingMs(300)              // Audio before speech
    .setSilenceDurationMs(500)            // Silence to end turn
    .setInterruptResponse(true)           // Allow interruptions
    .setAutoTruncate(true)
    .setCreateResponse(true);

AudioInputTranscriptionOptions transcription = new AudioInputTranscriptionOptions(
    AudioInputTranscriptionOptionsMod

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Real-time, bidirectional voice conversations with AI assistants using WebSocket technology.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure AI VoiceLive SDK for Java
- Para tarefas relacionadas a azure ai voicelive sdk for java

## Diretrizes Específicas

