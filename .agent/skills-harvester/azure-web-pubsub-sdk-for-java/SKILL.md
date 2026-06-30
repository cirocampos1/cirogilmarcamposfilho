---
name: azure-web-pubsub-sdk-for-java
description: Build real-time web applications using the Azure Web PubSub SDK for Java.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Web PubSub SDK for Java

## Backstory

Você é um agente especializado em Azure Web PubSub SDK for Java.

## Contexto Original da Skill
Azure Web PubSub SDK for Java

## Instruções
---
name: azure-messaging-webpubsub-java
description: "Build real-time web applications with Azure Web PubSub SDK for Java. Use when implementing WebSocket-based messaging, live updates, chat applications, or server-to-client push notifications."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure Web PubSub SDK for Java

Build real-time web applications using the Azure Web PubSub SDK for Java.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-messaging-webpubsub</artifactId>
    <version>1.5.0</version>
</dependency>
```

## Client Creation

### With Connection String

```java
import com.azure.messaging.webpubsub.WebPubSubServiceClient;
import com.azure.messaging.webpubsub.WebPubSubServiceClientBuilder;

WebPubSubServiceClient client = new WebPubSubServiceClientBuilder()
    .connectionString("<connection-string>")
    .hub("chat")
    .buildClient();
```

### With Access Key

```java
import com.azure.core.credential.AzureKeyCredential;

WebPubSubServiceClient client = new WebPubSubServiceClientBuilder()
    .credential(new AzureKeyCredential("<access-key>"))
    .endpoint("<endpoint>")
    .hub("chat")
    .buildClient();
```

### With DefaultAzureCredential

```java
import com.azure.identity.DefaultAzureCredentialBuilder;

WebPubSubServiceClient client = new WebPubSubServiceClientBuilder()
    .credential(new DefaultAzureCredentialBuilder().build())
    .endpoint("<endpoint>")
    .hub("chat")
    .buildClient();
```

### Async Client

```java
import com.azure.messaging.webpubsub.WebPubSubServiceAsyncClient;

WebPubSubServiceAsyncClient asyncClient = new WebPubSubServiceClientBuilder()
    .connectionString("<connection-string>")
    .hub("chat")
    .buildAsyncClient();
```

## Key Concepts

- **Hub**: Logical isolation unit for connections
- **Group**: Subset of connections within a hub
- **Connection**: Individual WebSocket client connection
- **User**: Entity that can have multiple connections

## Core Patterns

### Send to All Connections

```java
import com.azure.messaging.webpubsub.models.WebPubSubContentType;

// Send text message
client.sendToAll("Hello everyone!", WebPubSubContentType.TEXT_PLAIN);

// Send JSON
String jsonMessage = "{\"type\": \"notification\", \"message\": \"New update!\"}";
client.sendToAll(jsonMessage, WebPubSubContentType.APPLICATION_JSON);
```

### Send to All with Filter

```java
import com.azure.core.http.rest.RequestOptions;
import com.azure.core.util.BinaryData;

BinaryData message = BinaryData.fromString("Hello filtered users!");

// Filter by userId
client.sendToAllWithResponse(
    message,
    WebPubSubContentType.TEXT_PLAIN,
    message.getLength(),
    new RequestOptions().addQueryParam("filter", "userId ne 'user1'"));

// Filter by groups
client.sendToAllWithResponse(
    message,
    WebPubSubContentType.TEXT_PLAIN,
    message.getLength(),
    new RequestOptions().addQueryParam("filter", "'GroupA' in groups and not('GroupB' in groups)"));


## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Build real-time web applications using the Azure Web PubSub SDK for Java.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Web PubSub SDK for Java
- Para tarefas relacionadas a azure web pubsub sdk for java

## Diretrizes Específicas

