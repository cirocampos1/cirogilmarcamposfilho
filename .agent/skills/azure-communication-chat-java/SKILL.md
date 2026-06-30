---
name: azure-communication-chat-java
description: Build real-time chat applications with thread management, messaging, participants, and read receipts.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Communication Chat (Java)

## Backstory

Você é um agente especializado em Azure Communication Chat (Java).

## Contexto Original da Skill
Azure Communication Chat (Java)

## Instruções
---
name: azure-communication-chat-java
description: "Build real-time chat applications with thread management, messaging, participants, and read receipts."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure Communication Chat (Java)

Build real-time chat applications with thread management, messaging, participants, and read receipts.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-communication-chat</artifactId>
    <version>1.6.0</version>
</dependency>
```

## Client Creation

```java
import com.azure.communication.chat.ChatClient;
import com.azure.communication.chat.ChatClientBuilder;
import com.azure.communication.chat.ChatThreadClient;
import com.azure.communication.common.CommunicationTokenCredential;

// ChatClient requires a CommunicationTokenCredential (user access token)
String endpoint = "https://<resource>.communication.azure.com";
String userAccessToken = "<user-access-token>";

CommunicationTokenCredential credential = new CommunicationTokenCredential(userAccessToken);

ChatClient chatClient = new ChatClientBuilder()
    .endpoint(endpoint)
    .credential(credential)
    .buildClient();

// Async client
ChatAsyncClient chatAsyncClient = new ChatClientBuilder()
    .endpoint(endpoint)
    .credential(credential)
    .buildAsyncClient();
```

## Key Concepts

| Class | Purpose |
|-------|---------|
| `ChatClient` | Create/delete chat threads, get thread clients |
| `ChatThreadClient` | Operations within a thread (messages, participants, receipts) |
| `ChatParticipant` | User in a chat thread with display name |
| `ChatMessage` | Message content, type, sender info, timestamps |
| `ChatMessageReadReceipt` | Read receipt tracking per participant |

## Create Chat Thread

```java
import com.azure.communication.chat.models.*;
import com.azure.communication.common.CommunicationUserIdentifier;
import java.util.ArrayList;
import java.util.List;

// Define participants
List<ChatParticipant> participants = new ArrayList<>();

ChatParticipant participant1 = new ChatParticipant()
    .setCommunicationIdentifier(new CommunicationUserIdentifier("<user-id-1>"))
    .setDisplayName("Alice");

ChatParticipant participant2 = new ChatParticipant()
    .setCommunicationIdentifier(new CommunicationUserIdentifier("<user-id-2>"))
    .setDisplayName("Bob");

participants.add(participant1);
participants.add(participant2);

// Create thread
CreateChatThreadOptions options = new CreateChatThreadOptions("Project Discussion")
    .setParticipants(participants);

CreateChatThreadResult result = chatClient.createChatThread(options);
String threadId = result.getChatThread().getId();

// Get thread client for operations
ChatThreadClient threadClient = chatClient.getChatThreadClient(threadId);
```

## Send Messages

```java
// Send text message
SendChatMessageOptions messageOptions = new SendChatMessageOptions()
    .setContent("Hello, team!")
    .setSenderDisplayName("Alice")
    .setType(ChatMessage

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Build real-time chat applications with thread management, messaging, participants, and read receipts.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Communication Chat (Java)
- Para tarefas relacionadas a azure communication chat java

## Diretrizes Específicas

