---
name: azure-app-configuration-sdk-for-java
description: Client library for Azure App Configuration, a managed service for centralizing application configurations.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure App Configuration SDK for Java

## Backstory

Você é um agente especializado em Azure App Configuration SDK for Java.

## Contexto Original da Skill
Azure App Configuration SDK for Java

## Instruções
---
name: azure-appconfiguration-java
description: Azure App Configuration SDK for Java. Centralized application configuration management with key-value settings, feature flags, and snapshots.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure App Configuration SDK for Java

Client library for Azure App Configuration, a managed service for centralizing application configurations.

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-data-appconfiguration</artifactId>
    <version>1.8.0</version>
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
        <artifactId>azure-data-appconfiguration</artifactId>
    </dependency>
</dependencies>
```

## Prerequisites

- Azure App Configuration store
- Connection string or Entra ID credentials

## Environment Variables

```bash
AZURE_APPCONFIG_CONNECTION_STRING=Endpoint=https://<store>.azconfig.io;Id=<id>;Secret=<secret>
AZURE_APPCONFIG_ENDPOINT=https://<store>.azconfig.io
```

## Client Creation

### With Connection String

```java
import com.azure.data.appconfiguration.ConfigurationClient;
import com.azure.data.appconfiguration.ConfigurationClientBuilder;

ConfigurationClient configClient = new ConfigurationClientBuilder()
    .connectionString(System.getenv("AZURE_APPCONFIG_CONNECTION_STRING"))
    .buildClient();
```

### Async Client

```java
import com.azure.data.appconfiguration.ConfigurationAsyncClient;

ConfigurationAsyncClient asyncClient = new ConfigurationClientBuilder()
    .connectionString(connectionString)
    .buildAsyncClient();
```

### With Entra ID (Recommended)

```java
import com.azure.identity.DefaultAzureCredentialBuilder;

ConfigurationClient configClient = new ConfigurationClientBuilder()
    .credential(new DefaultAzureCredentialBuilder().build())
    .endpoint(System.getenv("AZURE_APPCONFIG_ENDPOINT"))
    .buildClient();
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| Configuration Setting | Key-value pair with optional label |
| Label | Dimension for separating settings (e.g., environments) |
| Feature Flag | Special setting for feature management |
| Secret Reference | Setting pointing to Key Vault secret |
| Snapshot | Point-in-time immutable view of settings |

## Configuration Setting Operations

### Create Setting (Add)

Creates only if setting doesn't exist:

```java
import com.azure.data.appconfiguration.models.ConfigurationSetting;

ConfigurationSetting setting = configClient.addConfigurationSetting(
    "app/database/connection", 
    "Production", 
    "Server=prod.db.com;Database=myapp"
);

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Client library for Azure App Configuration, a managed service for centralizing application configurations.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure App Configuration SDK for Java
- Para tarefas relacionadas a azure app configuration sdk for java

## Diretrizes Específicas

