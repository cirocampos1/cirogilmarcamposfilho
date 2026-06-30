---
name: azureresourcemanagerfabric-net
description: Management plane SDK for provisioning and managing Microsoft Fabric capacity resources via Azure Resource Manager.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.ResourceManager.Fabric (.NET)

## Backstory

Você é um agente especializado em Azure.ResourceManager.Fabric (.NET).

## Contexto Original da Skill
Azure.ResourceManager.Fabric (.NET)

## Instruções
---
name: azure-mgmt-fabric-dotnet
description: Azure Resource Manager SDK for Fabric in .NET.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.ResourceManager.Fabric (.NET)

Management plane SDK for provisioning and managing Microsoft Fabric capacity resources via Azure Resource Manager.

> **Management Plane Only**
> This SDK manages Fabric *capacities* (compute resources). For working with Fabric workspaces, lakehouses, warehouses, and data items, use the Microsoft Fabric REST API or data plane SDKs.

## Installation

```bash
dotnet add package Azure.ResourceManager.Fabric
dotnet add package Azure.Identity
```

**Current Version**: 1.0.0 (GA - September 2025)  
**API Version**: 2023-11-01  
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
using Azure.ResourceManager.Fabric;

// Always use DefaultAzureCredential
var credential = new DefaultAzureCredential();
var armClient = new ArmClient(credential);

// Get subscription
var subscription = await armClient.GetDefaultSubscriptionAsync();
```

## Resource Hierarchy

```
ArmClient
└── SubscriptionResource
    └── ResourceGroupResource
        └── FabricCapacityResource
```

## Core Workflows

### 1. Create Fabric Capacity

```csharp
using Azure.ResourceManager.Fabric;
using Azure.ResourceManager.Fabric.Models;
using Azure.Core;

// Get resource group
var resourceGroup = await subscription.GetResourceGroupAsync("my-resource-group");

// Define capacity configuration
var administration = new FabricCapacityAdministration(
    new[] { "admin@contoso.com" }  // Capacity administrators (UPNs or object IDs)
);

var properties = new FabricCapacityProperties(administration);

var sku = new FabricSku("F64", FabricSkuTier.Fabric);

var capacityData = new FabricCapacityData(
    AzureLocation.WestUS2,
    properties,
    sku)
{
    Tags = { ["Environment"] = "Production" }
};

// Create capacity (long-running operation)
var capacityCollection = resourceGroup.Value.GetFabricCapacities();
var operation = await capacityCollection.CreateOrUpdateAsync(
    WaitUntil.Completed,
    "my-fabric-capacity",
    capacityData);

FabricCapacityResource capacity = operation.Value;
Console.WriteLine($"Created capacity: {capacity.Data.Name}");
Console.WriteLine($"State: {capacity.Data.Properties.State}");
```

### 2. Get Fabric Capacity

```csharp
// Get existing capacity
var capacity = await resourceGroup.Value
    .GetFabricCapacityAsync("my-fabric-capacity");

Console.WriteLine($"Name: {capacity.Value.Data.Name}");
Console.WriteLine($"Location: {capacity.Value.Data.Location}");
Console.WriteLine($"SKU: {capacity.Value.Data.Sku.Name}");
Console.WriteLine($"State: {capacity.Value.Data.Properties.State}");
Conso

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Management plane SDK for provisioning and managing Microsoft Fabric capacity resources via Azure Resource Manager.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.ResourceManager.Fabric (.NET)
- Para tarefas relacionadas a azureresourcemanagerfabric net

## Diretrizes Específicas

