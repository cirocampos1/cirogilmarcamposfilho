---
name: azureresourcemanagerapplicationinsights-net
description: Azure Resource Manager SDK for managing Application Insights resources for application performance monitoring.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.ResourceManager.ApplicationInsights (.NET)

## Backstory

Você é um agente especializado em Azure.ResourceManager.ApplicationInsights (.NET).

## Contexto Original da Skill
Azure.ResourceManager.ApplicationInsights (.NET)

## Instruções
---
name: azure-mgmt-applicationinsights-dotnet
description: Azure Application Insights SDK for .NET. Application performance monitoring and observability resource management.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.ResourceManager.ApplicationInsights (.NET)

Azure Resource Manager SDK for managing Application Insights resources for application performance monitoring.

## Installation

```bash
dotnet add package Azure.ResourceManager.ApplicationInsights
dotnet add package Azure.Identity
```

**Current Version**: v1.0.0 (GA)  
**API Version**: 2022-06-15

## Environment Variables

```bash
AZURE_SUBSCRIPTION_ID=<your-subscription-id>
AZURE_RESOURCE_GROUP=<your-resource-group>
AZURE_APPINSIGHTS_NAME=<your-appinsights-component>
```

## Authentication

```csharp
using Azure.Identity;
using Azure.ResourceManager;
using Azure.ResourceManager.ApplicationInsights;

ArmClient client = new ArmClient(new DefaultAzureCredential());
```

## Resource Hierarchy

```
Subscription
└── ResourceGroup
    └── ApplicationInsightsComponent          # App Insights resource
        ├── ApplicationInsightsComponentApiKey  # API keys for programmatic access
        ├── ComponentLinkedStorageAccount      # Linked storage for data export
        └── (via component ID)
            ├── WebTest                        # Availability tests
            ├── Workbook                       # Workbooks for analysis
            ├── WorkbookTemplate               # Workbook templates
            └── MyWorkbook                     # Private workbooks
```

## Core Workflows

### 1. Create Application Insights Component (Workspace-based)

```csharp
using Azure.ResourceManager.ApplicationInsights;
using Azure.ResourceManager.ApplicationInsights.Models;

ResourceGroupResource resourceGroup = await client
    .GetDefaultSubscriptionAsync()
    .Result
    .GetResourceGroupAsync("my-resource-group");

ApplicationInsightsComponentCollection components = resourceGroup.GetApplicationInsightsComponents();

// Workspace-based Application Insights (recommended)
ApplicationInsightsComponentData data = new ApplicationInsightsComponentData(
    AzureLocation.EastUS,
    ApplicationInsightsApplicationType.Web)
{
    Kind = "web",
    WorkspaceResourceId = new ResourceIdentifier(
        "/subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.OperationalInsights/workspaces/<workspace-name>"),
    IngestionMode = IngestionMode.LogAnalytics,
    PublicNetworkAccessForIngestion = PublicNetworkAccessType.Enabled,
    PublicNetworkAccessForQuery = PublicNetworkAccessType.Enabled,
    RetentionInDays = 90,
    SamplingPercentage = 100,
    DisableIPMasking = false,
    ImmediatePurgeDataOn30Days = false,
    Tags =
    {
        { "environment", "production" },
        { "application", "mywebapp" }
    }
};

ArmOperation<ApplicationInsightsComponentResource> operation = await components
    .CreateOrUpdateAsync(WaitUntil.Completed, "my-appinsights", data);

ApplicationIn

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Azure Resource Manager SDK for managing Application Insights resources for application performance monitoring.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.ResourceManager.ApplicationInsights (.NET)
- Para tarefas relacionadas a azureresourcemanagerapplicationinsights net

## Diretrizes Específicas

