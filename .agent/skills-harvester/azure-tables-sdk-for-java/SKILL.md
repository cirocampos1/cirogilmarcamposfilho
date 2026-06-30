---
name: azure-tables-sdk-for-java
description: Build table storage applications using the Azure Tables SDK for Java. Works with both Azure Table Storage and Cosmos DB Table API.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Tables SDK for Java

## Backstory

Você é um agente especializado em Azure Tables SDK for Java.

## Contexto Original da Skill
Azure Tables SDK for Java

## Instruções
---
name: azure-data-tables-java
description: "Build table storage applications using the Azure Tables SDK for Java. Works with both Azure Table Storage and Cosmos DB Table API."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure Tables SDK for Java

Build table storage applications using the Azure Tables SDK for Java. Works with both Azure Table Storage and Cosmos DB Table API.

## Installation

```xml
<dependency>
  <groupId>com.azure</groupId>
  <artifactId>azure-data-tables</artifactId>
  <version>12.6.0-beta.1</version>
</dependency>
```

## Client Creation

### With Connection String

```java
import com.azure.data.tables.TableServiceClient;
import com.azure.data.tables.TableServiceClientBuilder;
import com.azure.data.tables.TableClient;

TableServiceClient serviceClient = new TableServiceClientBuilder()
    .connectionString("<your-connection-string>")
    .buildClient();
```

### With Shared Key

```java
import com.azure.core.credential.AzureNamedKeyCredential;

AzureNamedKeyCredential credential = new AzureNamedKeyCredential(
    "<account-name>",
    "<account-key>");

TableServiceClient serviceClient = new TableServiceClientBuilder()
    .endpoint("<your-table-account-url>")
    .credential(credential)
    .buildClient();
```

### With SAS Token

```java
TableServiceClient serviceClient = new TableServiceClientBuilder()
    .endpoint("<your-table-account-url>")
    .sasToken("<sas-token>")
    .buildClient();
```

### With DefaultAzureCredential (Storage only)

```java
import com.azure.identity.DefaultAzureCredentialBuilder;

TableServiceClient serviceClient = new TableServiceClientBuilder()
    .endpoint("<your-table-account-url>")
    .credential(new DefaultAzureCredentialBuilder().build())
    .buildClient();
```

## Key Concepts

- **TableServiceClient**: Manage tables (create, list, delete)
- **TableClient**: Manage entities within a table (CRUD)
- **Partition Key**: Groups entities for efficient queries
- **Row Key**: Unique identifier within a partition
- **Entity**: A row with up to 252 properties (1MB Storage, 2MB Cosmos)

## Core Patterns

### Create Table

```java
// Create table (throws if exists)
TableClient tableClient = serviceClient.createTable("mytable");

// Create if not exists (no exception)
TableClient tableClient = serviceClient.createTableIfNotExists("mytable");
```

### Get Table Client

```java
// From service client
TableClient tableClient = serviceClient.getTableClient("mytable");

// Direct construction
TableClient tableClient = new TableClientBuilder()
    .connectionString("<connection-string>")
    .tableName("mytable")
    .buildClient();
```

### Create Entity

```java
import com.azure.data.tables.models.TableEntity;

TableEntity entity = new TableEntity("partitionKey", "rowKey")
    .addProperty("Name", "Product A")
    .addProperty("Price", 29.99)
    .addProperty("Quantity", 100)
    .addProperty("IsAvailable", true);

tableClient.createEntity(entity);
```

### Get Entity

```java
T

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Build table storage applications using the Azure Tables SDK for Java. Works with both Azure Table Storage and Cosmos DB Table API.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Tables SDK for Java
- Para tarefas relacionadas a azure tables sdk for java

## Diretrizes Específicas

