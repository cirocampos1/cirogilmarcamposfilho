---
name: azure-batch-sdk-for-java
description: Client library for running large-scale parallel and high-performance computing (HPC) batch jobs in Azure.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Batch SDK for Java

## Backstory

Você é um agente especializado em Azure Batch SDK for Java.

## Contexto Original da Skill
Azure Batch SDK for Java

## Instruções
---
name: azure-compute-batch-java
description: Azure Batch SDK for Java. Run large-scale parallel and HPC batch jobs with pools, jobs, tasks, and compute nodes.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure Batch SDK for Java

Client library for running large-scale parallel and high-performance computing (HPC) batch jobs in Azure.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-compute-batch</artifactId>
    <version>1.0.0-beta.5</version>
</dependency>
```

## Prerequisites

- Azure Batch account
- Pool configured with compute nodes
- Azure subscription

## Environment Variables

```bash
AZURE_BATCH_ENDPOINT=https://<account>.<region>.batch.azure.com
AZURE_BATCH_ACCOUNT=<account-name>
AZURE_BATCH_ACCESS_KEY=<account-key>
```

## Client Creation

### With Microsoft Entra ID (Recommended)

```java
import com.azure.compute.batch.BatchClient;
import com.azure.compute.batch.BatchClientBuilder;
import com.azure.identity.DefaultAzureCredentialBuilder;

BatchClient batchClient = new BatchClientBuilder()
    .credential(new DefaultAzureCredentialBuilder().build())
    .endpoint(System.getenv("AZURE_BATCH_ENDPOINT"))
    .buildClient();
```

### Async Client

```java
import com.azure.compute.batch.BatchAsyncClient;

BatchAsyncClient batchAsyncClient = new BatchClientBuilder()
    .credential(new DefaultAzureCredentialBuilder().build())
    .endpoint(System.getenv("AZURE_BATCH_ENDPOINT"))
    .buildAsyncClient();
```

### With Shared Key Credentials

```java
import com.azure.core.credential.AzureNamedKeyCredential;

String accountName = System.getenv("AZURE_BATCH_ACCOUNT");
String accountKey = System.getenv("AZURE_BATCH_ACCESS_KEY");
AzureNamedKeyCredential sharedKeyCreds = new AzureNamedKeyCredential(accountName, accountKey);

BatchClient batchClient = new BatchClientBuilder()
    .credential(sharedKeyCreds)
    .endpoint(System.getenv("AZURE_BATCH_ENDPOINT"))
    .buildClient();
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| Pool | Collection of compute nodes that run tasks |
| Job | Logical grouping of tasks |
| Task | Unit of computation (command/script) |
| Node | VM that executes tasks |
| Job Schedule | Recurring job creation |

## Pool Operations

### Create Pool

```java
import com.azure.compute.batch.models.*;

batchClient.createPool(new BatchPoolCreateParameters("myPoolId", "STANDARD_DC2s_V2")
    .setVirtualMachineConfiguration(
        new VirtualMachineConfiguration(
            new BatchVmImageReference()
                .setPublisher("Canonical")
                .setOffer("UbuntuServer")
                .setSku("22_04-lts")
                .setVersion("latest"),
            "batch.node.ubuntu 22.04"))
    .setTargetDedicatedNodes(2)
    .setTargetLowPriorityNodes(0), null);
```

### Get Pool

```java
BatchPool pool = batchClient.getPool("myPoolId");
System.out.println("Pool state: " + pool.getState());
System.out.println("Current dedicated nod

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Client library for running large-scale parallel and high-performance computing (HPC) batch jobs in Azure.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Batch SDK for Java
- Para tarefas relacionadas a azure batch sdk for java

## Diretrizes Específicas

