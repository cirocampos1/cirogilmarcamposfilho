---
name: azure-monitor-query-sdk-for-java
description: > **DEPRECATION NOTICE**: This package is deprecated in favor of: > - `azure-monitor-query-logs` — For Log Analytics queries > - `azure-monitor-query-metrics` — For metrics queries > > See migration g
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Monitor Query SDK for Java

## Backstory

Você é um agente especializado em Azure Monitor Query SDK for Java.

## Contexto Original da Skill
Azure Monitor Query SDK for Java

## Instruções
---
name: azure-monitor-query-java
description: Azure Monitor Query SDK for Java. Execute Kusto queries against Log Analytics workspaces and query metrics from Azure resources.
risk: safe
source: community
date_added: '2026-02-27'
---

# Azure Monitor Query SDK for Java

> **DEPRECATION NOTICE**: This package is deprecated in favor of:
> - `azure-monitor-query-logs` — For Log Analytics queries
> - `azure-monitor-query-metrics` — For metrics queries
>
> See migration guides: [Logs Migration](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/monitor/azure-monitor-query-logs/migration-guide.md) | [Metrics Migration](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/monitor/azure-monitor-query-metrics/migration-guide.md)

Client library for querying Azure Monitor Logs and Metrics.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-monitor-query</artifactId>
    <version>1.5.9</version>
</dependency>
```

Or use Azure SDK BOM:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.azure</groupId>
            <artifactId>azure-sdk-bom</artifactId>
            <version>{bom_version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <dependency>
        <groupId>com.azure</groupId>
        <artifactId>azure-monitor-query</artifactId>
    </dependency>
</dependencies>
```

## Prerequisites

- Log Analytics workspace (for logs queries)
- Azure resource (for metrics queries)
- TokenCredential with appropriate permissions

## Environment Variables

```bash
LOG_ANALYTICS_WORKSPACE_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_RESOURCE_ID=/subscriptions/{sub}/resourceGroups/{rg}/providers/{provider}/{resource}
```

## Client Creation

### LogsQueryClient (Sync)

```java
import com.azure.identity.DefaultAzureCredentialBuilder;
import com.azure.monitor.query.LogsQueryClient;
import com.azure.monitor.query.LogsQueryClientBuilder;

LogsQueryClient logsClient = new LogsQueryClientBuilder()
    .credential(new DefaultAzureCredentialBuilder().build())
    .buildClient();
```

### LogsQueryAsyncClient

```java
import com.azure.monitor.query.LogsQueryAsyncClient;

LogsQueryAsyncClient logsAsyncClient = new LogsQueryClientBuilder()
    .credential(new DefaultAzureCredentialBuilder().build())
    .buildAsyncClient();
```

### MetricsQueryClient (Sync)

```java
import com.azure.monitor.query.MetricsQueryClient;
import com.azure.monitor.query.MetricsQueryClientBuilder;

MetricsQueryClient metricsClient = new MetricsQueryClientBuilder()
    .credential(new DefaultAzureCredentialBuilder().build())
    .buildClient();
```

### MetricsQueryAsyncClient

```java
import com.azure.monitor.query.MetricsQueryAsyncClient;

MetricsQueryAsyncClient metricsAsyncClient = new MetricsQueryClientBuilder()
    .credential(new DefaultAzureCredentialBuilder().build())
    .buildAsyncClient

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

> **DEPRECATION NOTICE**: This package is deprecated in favor of: > - `azure-monitor-query-logs` — For Log Analytics queries > - `azure-monitor-query-metrics` — For metrics queries > > See migration g

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Monitor Query SDK for Java
- Para tarefas relacionadas a azure monitor query sdk for java

## Diretrizes Específicas

