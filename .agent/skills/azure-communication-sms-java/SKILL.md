---
name: azure-communication-sms-java
description: Send SMS messages to single or multiple recipients with delivery reporting.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Communication SMS (Java)

## Backstory

Você é um agente especializado em Azure Communication SMS (Java).

## Contexto Original da Skill
Azure Communication SMS (Java)

## Instruções
---
name: azure-communication-sms-java
description: "Send SMS messages with Azure Communication Services SMS Java SDK. Use when implementing SMS notifications, alerts, OTP delivery, bulk messaging, or delivery reports."
risk: safe
source: community
date_added: "2026-02-27"
---

# Azure Communication SMS (Java)

Send SMS messages to single or multiple recipients with delivery reporting.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-communication-sms</artifactId>
    <version>1.2.0</version>
</dependency>
```

## Client Creation

```java
import com.azure.communication.sms.SmsClient;
import com.azure.communication.sms.SmsClientBuilder;
import com.azure.identity.DefaultAzureCredentialBuilder;

// With DefaultAzureCredential (recommended)
SmsClient smsClient = new SmsClientBuilder()
    .endpoint("https://<resource>.communication.azure.com")
    .credential(new DefaultAzureCredentialBuilder().build())
    .buildClient();

// With connection string
SmsClient smsClient = new SmsClientBuilder()
    .connectionString("<connection-string>")
    .buildClient();

// With AzureKeyCredential
import com.azure.core.credential.AzureKeyCredential;

SmsClient smsClient = new SmsClientBuilder()
    .endpoint("https://<resource>.communication.azure.com")
    .credential(new AzureKeyCredential("<access-key>"))
    .buildClient();

// Async client
SmsAsyncClient smsAsyncClient = new SmsClientBuilder()
    .connectionString("<connection-string>")
    .buildAsyncClient();
```

## Send SMS to Single Recipient

```java
import com.azure.communication.sms.models.SmsSendResult;

// Simple send
SmsSendResult result = smsClient.send(
    "+14255550100",      // From (your ACS phone number)
    "+14255551234",      // To
    "Your verification code is 123456");

System.out.println("Message ID: " + result.getMessageId());
System.out.println("To: " + result.getTo());
System.out.println("Success: " + result.isSuccessful());

if (!result.isSuccessful()) {
    System.out.println("Error: " + result.getErrorMessage());
    System.out.println("Status: " + result.getHttpStatusCode());
}
```

## Send SMS to Multiple Recipients

```java
import com.azure.communication.sms.models.SmsSendOptions;
import java.util.Arrays;
import java.util.List;

List<String> recipients = Arrays.asList(
    "+14255551111",
    "+14255552222",
    "+14255553333"
);

// With options
SmsSendOptions options = new SmsSendOptions()
    .setDeliveryReportEnabled(true)
    .setTag("marketing-campaign-001");

Iterable<SmsSendResult> results = smsClient.sendWithResponse(
    "+14255550100",      // From
    recipients,          // To list
    "Flash sale! 50% off today only.",
    options,
    Context.NONE
).getValue();

for (SmsSendResult result : results) {
    if (result.isSuccessful()) {
        System.out.println("Sent to " + result.getTo() + ": " + result.getMessageId());
    } else {
        System.out.println("Failed to " + result.getTo() + ": " + result.getErrorMess

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Send SMS messages to single or multiple recipients with delivery reporting.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Communication SMS (Java)
- Para tarefas relacionadas a azure communication sms java

## Diretrizes Específicas

