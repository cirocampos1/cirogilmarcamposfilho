---
name: azure-ai-projects-sdk-for-java
description: High-level SDK for Azure AI Foundry project management with access to connections, datasets, indexes, and evaluations.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure AI Projects SDK for Java

## Backstory

Você é um agente especializado em Azure AI Projects SDK for Java.

## Contexto Original da Skill
Azure AI Projects SDK for Java

## Instruções
---
name: azure-ai-projects-java
description: Azure AI Projects SDK for Java. High-level SDK for Azure AI Foundry project management including connections, datasets, indexes, and evaluations.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure AI Projects SDK for Java

High-level SDK for Azure AI Foundry project management with access to connections, datasets, indexes, and evaluations.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-ai-projects</artifactId>
    <version>1.0.0-beta.1</version>
</dependency>
```

## Environment Variables

```bash
PROJECT_ENDPOINT=https://<resource>.services.ai.azure.com/api/projects/<project>
```

## Authentication

```java
import com.azure.ai.projects.AIProjectClientBuilder;
import com.azure.identity.DefaultAzureCredentialBuilder;

AIProjectClientBuilder builder = new AIProjectClientBuilder()
    .endpoint(System.getenv("PROJECT_ENDPOINT"))
    .credential(new DefaultAzureCredentialBuilder().build());
```

## Client Hierarchy

The SDK provides multiple sub-clients for different operations:

| Client | Purpose |
|--------|---------|
| `ConnectionsClient` | Enumerate connected Azure resources |
| `DatasetsClient` | Upload documents and manage datasets |
| `DeploymentsClient` | Enumerate AI model deployments |
| `IndexesClient` | Create and manage search indexes |
| `EvaluationsClient` | Run AI model evaluations |
| `EvaluatorsClient` | Manage evaluator configurations |
| `SchedulesClient` | Manage scheduled operations |

```java
// Build sub-clients from builder
ConnectionsClient connectionsClient = builder.buildConnectionsClient();
DatasetsClient datasetsClient = builder.buildDatasetsClient();
DeploymentsClient deploymentsClient = builder.buildDeploymentsClient();
IndexesClient indexesClient = builder.buildIndexesClient();
EvaluationsClient evaluationsClient = builder.buildEvaluationsClient();
```

## Core Operations

### List Connections

```java
import com.azure.ai.projects.models.Connection;
import com.azure.core.http.rest.PagedIterable;

PagedIterable<Connection> connections = connectionsClient.listConnections();
for (Connection connection : connections) {
    System.out.println("Name: " + connection.getName());
    System.out.println("Type: " + connection.getType());
    System.out.println("Credential Type: " + connection.getCredentials().getType());
}
```

### List Indexes

```java
indexesClient.listLatest().forEach(index -> {
    System.out.println("Index name: " + index.getName());
    System.out.println("Version: " + index.getVersion());
    System.out.println("Description: " + index.getDescription());
});
```

### Create or Update Index

```java
import com.azure.ai.projects.models.AzureAISearchIndex;
import com.azure.ai.projects.models.Index;

String indexName = "my-index";
String indexVersion = "1.0";
String searchConnectionName = System.getenv("AI_SEARCH_CONNECTION_NAME");
String searchIndexName = System.getenv("AI_SEARCH_INDEX_NAME");

Inde

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

High-level SDK for Azure AI Foundry project management with access to connections, datasets, indexes, and evaluations.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure AI Projects SDK for Java
- Para tarefas relacionadas a azure ai projects sdk for java

## Diretrizes Específicas

