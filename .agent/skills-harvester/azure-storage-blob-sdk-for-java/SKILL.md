---
name: azure-storage-blob-sdk-for-java
description: Build blob storage applications using the Azure Storage Blob SDK for Java.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Storage Blob SDK for Java

## Backstory

Você é um agente especializado em Azure Storage Blob SDK for Java.

## Contexto Original da Skill
Azure Storage Blob SDK for Java

## Instruções
---
name: azure-storage-blob-java
description: "Build blob storage applications using the Azure Storage Blob SDK for Java."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure Storage Blob SDK for Java

Build blob storage applications using the Azure Storage Blob SDK for Java.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-storage-blob</artifactId>
    <version>12.33.0</version>
</dependency>
```

## Client Creation

### BlobServiceClient

```java
import com.azure.storage.blob.BlobServiceClient;
import com.azure.storage.blob.BlobServiceClientBuilder;

// With SAS token
BlobServiceClient serviceClient = new BlobServiceClientBuilder()
    .endpoint("<storage-account-url>")
    .sasToken("<sas-token>")
    .buildClient();

// With connection string
BlobServiceClient serviceClient = new BlobServiceClientBuilder()
    .connectionString("<connection-string>")
    .buildClient();
```

### With DefaultAzureCredential

```java
import com.azure.identity.DefaultAzureCredentialBuilder;

BlobServiceClient serviceClient = new BlobServiceClientBuilder()
    .endpoint("<storage-account-url>")
    .credential(new DefaultAzureCredentialBuilder().build())
    .buildClient();
```

### BlobContainerClient

```java
import com.azure.storage.blob.BlobContainerClient;

// From service client
BlobContainerClient containerClient = serviceClient.getBlobContainerClient("mycontainer");

// Direct construction
BlobContainerClient containerClient = new BlobContainerClientBuilder()
    .connectionString("<connection-string>")
    .containerName("mycontainer")
    .buildClient();
```

### BlobClient

```java
import com.azure.storage.blob.BlobClient;

// From container client
BlobClient blobClient = containerClient.getBlobClient("myblob.txt");

// With directory structure
BlobClient blobClient = containerClient.getBlobClient("folder/subfolder/myblob.txt");

// Direct construction
BlobClient blobClient = new BlobClientBuilder()
    .connectionString("<connection-string>")
    .containerName("mycontainer")
    .blobName("myblob.txt")
    .buildClient();
```

## Core Patterns

### Create Container

```java
// Create container
serviceClient.createBlobContainer("mycontainer");

// Create if not exists
BlobContainerClient container = serviceClient.createBlobContainerIfNotExists("mycontainer");

// From container client
containerClient.create();
containerClient.createIfNotExists();
```

### Upload Data

```java
import com.azure.core.util.BinaryData;

// Upload string
String data = "Hello, Azure Blob Storage!";
blobClient.upload(BinaryData.fromString(data));

// Upload with overwrite
blobClient.upload(BinaryData.fromString(data), true);
```

### Upload from File

```java
blobClient.uploadFromFile("local-file.txt");

// With overwrite
blobClient.uploadFromFile("local-file.txt", true);
```

### Upload from Stream

```java
import com.azure.storage.blob.specialized.BlockBlobClient;

BlockBlobClient blockBlobClient = blobClient.ge

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Build blob storage applications using the Azure Storage Blob SDK for Java.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Storage Blob SDK for Java
- Para tarefas relacionadas a azure storage blob sdk for java

## Diretrizes Específicas

