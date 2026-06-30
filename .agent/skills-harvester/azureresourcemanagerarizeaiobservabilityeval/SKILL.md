---
name: azureresourcemanagerarizeaiobservabilityeval
description: .NET SDK for managing Arize AI Observability and Evaluation resources on Azure.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.ResourceManager.ArizeAIObservabilityEval

## Backstory

Você é um agente especializado em Azure.ResourceManager.ArizeAIObservabilityEval.

## Contexto Original da Skill
Azure.ResourceManager.ArizeAIObservabilityEval

## Instruções
---
name: azure-mgmt-arizeaiobservabilityeval-dotnet
description: Azure Resource Manager SDK for Arize AI Observability and Evaluation (.NET).
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.ResourceManager.ArizeAIObservabilityEval

.NET SDK for managing Arize AI Observability and Evaluation resources on Azure.

## Installation

```bash
dotnet add package Azure.ResourceManager.ArizeAIObservabilityEval --version 1.0.0
```

## Package Info

| Property | Value |
|----------|-------|
| Package | `Azure.ResourceManager.ArizeAIObservabilityEval` |
| Version | `1.0.0` (GA) |
| API Version | `2024-10-01` |
| ARM Type | `ArizeAi.ObservabilityEval/organizations` |
| Dependencies | `Azure.Core` >= 1.46.2, `Azure.ResourceManager` >= 1.13.1 |

## Environment Variables

```bash
AZURE_SUBSCRIPTION_ID=<your-subscription-id>
AZURE_TENANT_ID=<your-tenant-id>
AZURE_CLIENT_ID=<your-client-id>
AZURE_CLIENT_SECRET=<your-client-secret>
```

## Authentication

```csharp
using Azure.Identity;
using Azure.ResourceManager;
using Azure.ResourceManager.ArizeAIObservabilityEval;

// Always use DefaultAzureCredential
var credential = new DefaultAzureCredential();
var armClient = new ArmClient(credential);
```

## Core Workflow

### Create an Arize AI Organization

```csharp
using Azure.Core;
using Azure.ResourceManager.Resources;
using Azure.ResourceManager.ArizeAIObservabilityEval;
using Azure.ResourceManager.ArizeAIObservabilityEval.Models;

// Get subscription and resource group
var subscriptionId = Environment.GetEnvironmentVariable("AZURE_SUBSCRIPTION_ID");
var subscription = await armClient.GetSubscriptionResource(
    SubscriptionResource.CreateResourceIdentifier(subscriptionId)).GetAsync();
var resourceGroup = await subscription.Value.GetResourceGroupAsync("my-resource-group");

// Get the organization collection
var collection = resourceGroup.Value.GetArizeAIObservabilityEvalOrganizations();

// Create organization data
var data = new ArizeAIObservabilityEvalOrganizationData(AzureLocation.EastUS)
{
    Properties = new ArizeAIObservabilityEvalOrganizationProperties
    {
        Marketplace = new ArizeAIObservabilityEvalMarketplaceDetails
        {
            SubscriptionId = "marketplace-subscription-id",
            OfferDetails = new ArizeAIObservabilityEvalOfferDetails
            {
                PublisherId = "arikimlabs1649082416596",
                OfferId = "arize-liftr-1",
                PlanId = "arize-liftr-1-plan",
                PlanName = "Arize AI Plan",
                TermUnit = "P1M",
                TermId = "term-id"
            }
        },
        User = new ArizeAIObservabilityEvalUserDetails
        {
            FirstName = "John",
            LastName = "Doe",
            EmailAddress = "john.doe@example.com"
        }
    },
    Tags = { ["environment"] = "production" }
};

// Create (long-running operation)
var operation = await collection.CreateOrUpdateAsync(
    WaitUntil.Completed,
    "my-arize-org",
    data

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

.NET SDK for managing Arize AI Observability and Evaluation resources on Azure.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.ResourceManager.ArizeAIObservabilityEval
- Para tarefas relacionadas a azureresourcemanagerarizeaiobservabilityeval

## Diretrizes Específicas

