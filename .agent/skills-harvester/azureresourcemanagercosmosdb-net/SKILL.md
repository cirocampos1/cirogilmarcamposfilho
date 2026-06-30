---
name: azureresourcemanagercosmosdb-net
description: Management plane SDK for provisioning and managing Azure Cosmos DB resources via Azure Resource Manager.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.ResourceManager.CosmosDB (.NET)

## Backstory

Você é um agente especializado em Azure.ResourceManager.CosmosDB (.NET).

## Contexto Original da Skill
Azure.ResourceManager.CosmosDB (.NET)

## Instruções
---
name: azure-resource-manager-cosmosdb-dotnet
description: Azure Resource Manager SDK for Cosmos DB in .NET.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.ResourceManager.CosmosDB (.NET)

Management plane SDK for provisioning and managing Azure Cosmos DB resources via Azure Resource Manager.

> **⚠️ Management vs Data Plane**
> - **This SDK (Azure.ResourceManager.CosmosDB)**: Create accounts, databases, containers, configure throughput, manage RBAC
> - **Data Plane SDK (Microsoft.Azure.Cosmos)**: CRUD operations on documents, queries, stored procedures execution

## Installation

```bash
dotnet add package Azure.ResourceManager.CosmosDB
dotnet add package Azure.Identity
```

**Current Versions**: Stable v1.4.0, Preview v1.4.0-beta.13

## Environment Variables

```bash
AZURE_SUBSCRIPTION_ID=<your-subscription-id>
# For service principal auth (optional)
AZURE_TENANT_ID=<tenant-id>
AZURE_CLIENT_ID=<client-id>
AZURE_CLIENT_SECRET=<client-secret>
```

## Authentication

```csharp
using Azure.Identity;
using Azure.ResourceManager;
using Azure.ResourceManager.CosmosDB;

// Always use DefaultAzureCredential
var credential = new DefaultAzureCredential();
var armClient = new ArmClient(credential);

// Get subscription
var subscriptionId = Environment.GetEnvironmentVariable("AZURE_SUBSCRIPTION_ID");
var subscription = armClient.GetSubscriptionResource(
    new ResourceIdentifier($"/subscriptions/{subscriptionId}"));
```

## Resource Hierarchy

```
ArmClient
└── SubscriptionResource
    └── ResourceGroupResource
        └── CosmosDBAccountResource
            ├── CosmosDBSqlDatabaseResource
            │   └── CosmosDBSqlContainerResource
            │       ├── CosmosDBSqlStoredProcedureResource
            │       ├── CosmosDBSqlTriggerResource
            │       └── CosmosDBSqlUserDefinedFunctionResource
            ├── CassandraKeyspaceResource
            ├── GremlinDatabaseResource
            ├── MongoDBDatabaseResource
            └── CosmosDBTableResource
```

## Core Workflow

### 1. Create Cosmos DB Account

```csharp
using Azure.ResourceManager.CosmosDB;
using Azure.ResourceManager.CosmosDB.Models;

// Get resource group
var resourceGroup = await subscription
    .GetResourceGroupAsync("my-resource-group");

// Define account
var accountData = new CosmosDBAccountCreateOrUpdateContent(
    location: AzureLocation.EastUS,
    locations: new[]
    {
        new CosmosDBAccountLocation
        {
            LocationName = AzureLocation.EastUS,
            FailoverPriority = 0,
            IsZoneRedundant = false
        }
    })
{
    Kind = CosmosDBAccountKind.GlobalDocumentDB,
    ConsistencyPolicy = new ConsistencyPolicy(DefaultConsistencyLevel.Session),
    EnableAutomaticFailover = true
};

// Create account (long-running operation)
var accountCollection = resourceGroup.Value.GetCosmosDBAccounts();
var operation = await accountCollection.CreateOrUpdateAsync(
    WaitUntil.Completed,
    "my-cosmos-account",
    accoun

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Management plane SDK for provisioning and managing Azure Cosmos DB resources via Azure Resource Manager.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.ResourceManager.CosmosDB (.NET)
- Para tarefas relacionadas a azureresourcemanagercosmosdb net

## Diretrizes Específicas

