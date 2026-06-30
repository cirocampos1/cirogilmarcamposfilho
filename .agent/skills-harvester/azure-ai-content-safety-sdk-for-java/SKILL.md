---
name: azure-ai-content-safety-sdk-for-java
description: Build content moderation applications using the Azure AI Content Safety SDK for Java.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure AI Content Safety SDK for Java

## Backstory

Você é um agente especializado em Azure AI Content Safety SDK for Java.

## Contexto Original da Skill
Azure AI Content Safety SDK for Java

## Instruções
---
name: azure-ai-contentsafety-java
description: "Build content moderation applications using the Azure AI Content Safety SDK for Java."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure AI Content Safety SDK for Java

Build content moderation applications using the Azure AI Content Safety SDK for Java.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-ai-contentsafety</artifactId>
    <version>1.1.0-beta.1</version>
</dependency>
```

## Client Creation

### With API Key

```java
import com.azure.ai.contentsafety.ContentSafetyClient;
import com.azure.ai.contentsafety.ContentSafetyClientBuilder;
import com.azure.ai.contentsafety.BlocklistClient;
import com.azure.ai.contentsafety.BlocklistClientBuilder;
import com.azure.core.credential.KeyCredential;

String endpoint = System.getenv("CONTENT_SAFETY_ENDPOINT");
String key = System.getenv("CONTENT_SAFETY_KEY");

ContentSafetyClient contentSafetyClient = new ContentSafetyClientBuilder()
    .credential(new KeyCredential(key))
    .endpoint(endpoint)
    .buildClient();

BlocklistClient blocklistClient = new BlocklistClientBuilder()
    .credential(new KeyCredential(key))
    .endpoint(endpoint)
    .buildClient();
```

### With DefaultAzureCredential

```java
import com.azure.identity.DefaultAzureCredentialBuilder;

ContentSafetyClient client = new ContentSafetyClientBuilder()
    .credential(new DefaultAzureCredentialBuilder().build())
    .endpoint(endpoint)
    .buildClient();
```

## Key Concepts

### Harm Categories
| Category | Description |
|----------|-------------|
| Hate | Discriminatory language based on identity groups |
| Sexual | Sexual content, relationships, acts |
| Violence | Physical harm, weapons, injury |
| Self-harm | Self-injury, suicide-related content |

### Severity Levels
- Text: 0-7 scale (default outputs 0, 2, 4, 6)
- Image: 0, 2, 4, 6 (trimmed scale)

## Core Patterns

### Analyze Text

```java
import com.azure.ai.contentsafety.models.*;

AnalyzeTextResult result = contentSafetyClient.analyzeText(
    new AnalyzeTextOptions("This is text to analyze"));

for (TextCategoriesAnalysis category : result.getCategoriesAnalysis()) {
    System.out.printf("Category: %s, Severity: %d%n",
        category.getCategory(),
        category.getSeverity());
}
```

### Analyze Text with Options

```java
AnalyzeTextOptions options = new AnalyzeTextOptions("Text to analyze")
    .setCategories(Arrays.asList(
        TextCategory.HATE,
        TextCategory.VIOLENCE))
    .setOutputType(AnalyzeTextOutputType.EIGHT_SEVERITY_LEVELS);

AnalyzeTextResult result = contentSafetyClient.analyzeText(options);
```

### Analyze Text with Blocklist

```java
AnalyzeTextOptions options = new AnalyzeTextOptions("I h*te you and want to k*ll you")
    .setBlocklistNames(Arrays.asList("my-blocklist"))
    .setHaltOnBlocklistHit(true);

AnalyzeTextResult result = contentSafetyClient.analyzeText(options);

if (result.getBlocklistsMatch() != null) 

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Build content moderation applications using the Azure AI Content Safety SDK for Java.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure AI Content Safety SDK for Java
- Para tarefas relacionadas a azure ai content safety sdk for java

## Diretrizes Específicas

