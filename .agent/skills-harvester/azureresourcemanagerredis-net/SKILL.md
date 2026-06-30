---
name: azureresourcemanagerredis-net
description: Management plane SDK for provisioning and managing Azure Cache for Redis resources via Azure Resource Manager.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.ResourceManager.Redis (.NET)

## Backstory

Você é um agente especializado em Azure.ResourceManager.Redis (.NET).

## Contexto Original da Skill
Azure.ResourceManager.Redis (.NET)

## Instruções
---
name: azure-resource-manager-redis-dotnet
description: Azure Resource Manager SDK for Redis in .NET.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.ResourceManager.Redis (.NET)

Management plane SDK for provisioning and managing Azure Cache for Redis resources via Azure Resource Manager.

> **⚠️ Management vs Data Plane**
> - **This SDK (Azure.ResourceManager.Redis)**: Create caches, configure firewall rules, manage access keys, set up geo-replication
> - **Data Plane SDK (StackExchange.Redis)**: Get/set keys, pub/sub, streams, Lua scripts

## Installation

```bash
dotnet add package Azure.ResourceManager.Redis
dotnet add package Azure.Identity
```

**Current Version**: 1.5.1 (Stable)  
**API Version**: 2024-11-01  
**Target Frameworks**: .NET 8.0, .NET Standard 2.0

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
using Azure.ResourceManager.Redis;

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
        └── RedisResource
            ├── RedisFirewallRuleResource
            ├── RedisPatchScheduleResource
            ├── RedisLinkedServerWithPropertyResource
            ├── RedisPrivateEndpointConnectionResource
            └── RedisCacheAccessPolicyResource
```

## Core Workflows

### 1. Create Redis Cache

```csharp
using Azure.ResourceManager.Redis;
using Azure.ResourceManager.Redis.Models;

// Get resource group
var resourceGroup = await subscription
    .GetResourceGroupAsync("my-resource-group");

// Define cache configuration
var cacheData = new RedisCreateOrUpdateContent(
    location: AzureLocation.EastUS,
    sku: new RedisSku(RedisSkuName.Standard, RedisSkuFamily.BasicOrStandard, 1))
{
    EnableNonSslPort = false,
    MinimumTlsVersion = RedisTlsVersion.Tls1_2,
    RedisConfiguration = new RedisCommonConfiguration
    {
        MaxMemoryPolicy = "volatile-lru"
    },
    Tags =
    {
        ["environment"] = "production"
    }
};

// Create cache (long-running operation)
var cacheCollection = resourceGroup.Value.GetAllRedis();
var operation = await cacheCollection.CreateOrUpdateAsync(
    WaitUntil.Completed,
    "my-redis-cache",
    cacheData);

RedisResource cache = operation.Value;
Console.WriteLine($"Cache created: {cache.Data.HostName}");
```

### 2. Get Redis Cache

```csharp
// Get existing cache
var cache = await resourceGroup.Value
    .GetRedisAsync("my-redis-cac

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Management plane SDK for provisioning and managing Azure Cache for Redis resources via Azure Resource Manager.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.ResourceManager.Redis (.NET)
- Para tarefas relacionadas a azureresourcemanagerredis net

## Diretrizes Específicas

