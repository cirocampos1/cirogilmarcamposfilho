---
name: azureresourcemanagerpostgresql-net
description: Azure Resource Manager SDK for managing PostgreSQL Flexible Server deployments.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.ResourceManager.PostgreSql (.NET)

## Backstory

Você é um agente especializado em Azure.ResourceManager.PostgreSql (.NET).

## Contexto Original da Skill
Azure.ResourceManager.PostgreSql (.NET)

## Instruções
---
name: azure-resource-manager-postgresql-dotnet
description: Azure PostgreSQL Flexible Server SDK for .NET. Database management for PostgreSQL Flexible Server deployments.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.ResourceManager.PostgreSql (.NET)

Azure Resource Manager SDK for managing PostgreSQL Flexible Server deployments.

## Installation

```bash
dotnet add package Azure.ResourceManager.PostgreSql
dotnet add package Azure.Identity
```

**Current Version**: v1.2.0 (GA)  
**API Version**: 2023-12-01-preview

> **Note**: This skill focuses on PostgreSQL Flexible Server. Single Server is deprecated and scheduled for retirement.

## Environment Variables

```bash
AZURE_SUBSCRIPTION_ID=<your-subscription-id>
AZURE_RESOURCE_GROUP=<your-resource-group>
AZURE_POSTGRESQL_SERVER_NAME=<your-postgresql-server>
```

## Authentication

```csharp
using Azure.Identity;
using Azure.ResourceManager;
using Azure.ResourceManager.PostgreSql;
using Azure.ResourceManager.PostgreSql.FlexibleServers;

ArmClient client = new ArmClient(new DefaultAzureCredential());
```

## Resource Hierarchy

```
Subscription
└── ResourceGroup
    └── PostgreSqlFlexibleServer              # PostgreSQL Flexible Server instance
        ├── PostgreSqlFlexibleServerDatabase  # Database within the server
        ├── PostgreSqlFlexibleServerFirewallRule # IP firewall rules
        ├── PostgreSqlFlexibleServerConfiguration # Server parameters
        ├── PostgreSqlFlexibleServerBackup    # Backup information
        ├── PostgreSqlFlexibleServerActiveDirectoryAdministrator # Entra ID admin
        └── PostgreSqlFlexibleServerVirtualEndpoint # Read replica endpoints
```

## Core Workflows

### 1. Create PostgreSQL Flexible Server

```csharp
using Azure.ResourceManager.PostgreSql.FlexibleServers;
using Azure.ResourceManager.PostgreSql.FlexibleServers.Models;

ResourceGroupResource resourceGroup = await client
    .GetDefaultSubscriptionAsync()
    .Result
    .GetResourceGroupAsync("my-resource-group");

PostgreSqlFlexibleServerCollection servers = resourceGroup.GetPostgreSqlFlexibleServers();

PostgreSqlFlexibleServerData data = new PostgreSqlFlexibleServerData(AzureLocation.EastUS)
{
    Sku = new PostgreSqlFlexibleServerSku("Standard_D2ds_v4", PostgreSqlFlexibleServerSkuTier.GeneralPurpose),
    AdministratorLogin = "pgadmin",
    AdministratorLoginPassword = "YourSecurePassword123!",
    Version = PostgreSqlFlexibleServerVersion.Ver16,
    Storage = new PostgreSqlFlexibleServerStorage
    {
        StorageSizeInGB = 128,
        AutoGrow = StorageAutoGrow.Enabled,
        Tier = PostgreSqlStorageTierName.P30
    },
    Backup = new PostgreSqlFlexibleServerBackupProperties
    {
        BackupRetentionDays = 7,
        GeoRedundantBackup = PostgreSqlFlexibleServerGeoRedundantBackupEnum.Disabled
    },
    HighAvailability = new PostgreSqlFlexibleServerHighAvailability
    {
        Mode = PostgreSqlFlexibleServerHighAvailabilityMode.ZoneRedundant,
        Stan

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Azure Resource Manager SDK for managing PostgreSQL Flexible Server deployments.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.ResourceManager.PostgreSql (.NET)
- Para tarefas relacionadas a azureresourcemanagerpostgresql net

## Diretrizes Específicas

