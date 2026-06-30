---
name: azure-communication-call-automation-java
description: Build server-side call automation workflows including IVR systems, call routing, recording, and AI-powered interactions.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Communication Call Automation (Java)

## Backstory

Você é um agente especializado em Azure Communication Call Automation (Java).

## Contexto Original da Skill
Azure Communication Call Automation (Java)

## Instruções
---
name: azure-communication-callautomation-java
description: "Build server-side call automation workflows including IVR systems, call routing, recording, and AI-powered interactions."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure Communication Call Automation (Java)

Build server-side call automation workflows including IVR systems, call routing, recording, and AI-powered interactions.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-communication-callautomation</artifactId>
    <version>1.6.0</version>
</dependency>
```

## Client Creation

```java
import com.azure.communication.callautomation.CallAutomationClient;
import com.azure.communication.callautomation.CallAutomationClientBuilder;
import com.azure.identity.DefaultAzureCredentialBuilder;

// With DefaultAzureCredential
CallAutomationClient client = new CallAutomationClientBuilder()
    .endpoint("https://<resource>.communication.azure.com")
    .credential(new DefaultAzureCredentialBuilder().build())
    .buildClient();

// With connection string
CallAutomationClient client = new CallAutomationClientBuilder()
    .connectionString("<connection-string>")
    .buildClient();
```

## Key Concepts

| Class | Purpose |
|-------|---------|
| `CallAutomationClient` | Make calls, answer/reject incoming calls, redirect calls |
| `CallConnection` | Actions in established calls (add participants, terminate) |
| `CallMedia` | Media operations (play audio, recognize DTMF/speech) |
| `CallRecording` | Start/stop/pause recording |
| `CallAutomationEventParser` | Parse webhook events from ACS |

## Create Outbound Call

```java
import com.azure.communication.callautomation.models.*;
import com.azure.communication.common.CommunicationUserIdentifier;
import com.azure.communication.common.PhoneNumberIdentifier;

// Call to PSTN number
PhoneNumberIdentifier target = new PhoneNumberIdentifier("+14255551234");
PhoneNumberIdentifier caller = new PhoneNumberIdentifier("+14255550100");

CreateCallOptions options = new CreateCallOptions(
    new CommunicationUserIdentifier("<user-id>"),  // Source
    List.of(target))                                // Targets
    .setSourceCallerId(caller)
    .setCallbackUrl("https://your-app.com/api/callbacks");

CreateCallResult result = client.createCall(options);
String callConnectionId = result.getCallConnectionProperties().getCallConnectionId();
```

## Answer Incoming Call

```java
// From Event Grid webhook - IncomingCall event
String incomingCallContext = "<incoming-call-context-from-event>";

AnswerCallOptions options = new AnswerCallOptions(
    incomingCallContext,
    "https://your-app.com/api/callbacks");

AnswerCallResult result = client.answerCall(options);
CallConnection callConnection = result.getCallConnection();
```

## Play Audio (Text-to-Speech)

```java
CallConnection callConnection = client.getCallConnection(callConnectionId);
CallMedia callMedia = callConnection.getCallMedia();

// Play

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Build server-side call automation workflows including IVR systems, call routing, recording, and AI-powered interactions.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Communication Call Automation (Java)
- Para tarefas relacionadas a azure communication call automation java

## Diretrizes Específicas

