---
name: azureresourcemanagerbotservice-net
description: Management plane SDK for provisioning and managing Azure Bot Service resources via Azure Resource Manager.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.ResourceManager.BotService (.NET)

## Backstory

Você é um agente especializado em Azure.ResourceManager.BotService (.NET).

## Contexto Original da Skill
Azure.ResourceManager.BotService (.NET)

## Instruções
---
name: azure-mgmt-botservice-dotnet
description: Azure Resource Manager SDK for Bot Service in .NET. Management plane operations for creating and managing Azure Bot resources, channels (Teams, DirectLine, Slack), and connection settings.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.ResourceManager.BotService (.NET)

Management plane SDK for provisioning and managing Azure Bot Service resources via Azure Resource Manager.

## Installation

```bash
dotnet add package Azure.ResourceManager.BotService
dotnet add package Azure.Identity
```

**Current Versions**: Stable v1.1.1, Preview v1.1.0-beta.1

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
using Azure.ResourceManager.BotService;

// Authenticate using DefaultAzureCredential
var credential = new DefaultAzureCredential();
ArmClient armClient = new ArmClient(credential);

// Get subscription and resource group
SubscriptionResource subscription = await armClient.GetDefaultSubscriptionAsync();
ResourceGroupResource resourceGroup = await subscription.GetResourceGroups().GetAsync("myResourceGroup");

// Access bot collection
BotCollection botCollection = resourceGroup.GetBots();
```

## Resource Hierarchy

```
ArmClient
└── SubscriptionResource
    └── ResourceGroupResource
        └── BotResource
            ├── BotChannelResource (DirectLine, Teams, Slack, etc.)
            ├── BotConnectionSettingResource (OAuth connections)
            └── BotServicePrivateEndpointConnectionResource
```

## Core Workflows

### 1. Create Bot Resource

```csharp
using Azure.ResourceManager.BotService;
using Azure.ResourceManager.BotService.Models;

// Create bot data
var botData = new BotData(AzureLocation.WestUS2)
{
    Kind = BotServiceKind.Azurebot,
    Sku = new BotServiceSku(BotServiceSkuName.F0),
    Properties = new BotProperties(
        displayName: "MyBot",
        endpoint: new Uri("https://mybot.azurewebsites.net/api/messages"),
        msaAppId: "<your-msa-app-id>")
    {
        Description = "My Azure Bot",
        MsaAppType = BotMsaAppType.MultiTenant
    }
};

// Create or update the bot
ArmOperation<BotResource> operation = await botCollection.CreateOrUpdateAsync(
    WaitUntil.Completed, 
    "myBotName", 
    botData);
    
BotResource bot = operation.Value;
Console.WriteLine($"Bot created: {bot.Data.Name}");
```

### 2. Configure DirectLine Channel

```csharp
// Get the bot
BotResource bot = await resourceGroup.GetBots().GetAsync("myBotName");

// Get channel collection
BotChannelCollection channels = bot.GetBotChannels();

// Create DirectLine channel configuration
var channelData = new BotChannelData(AzureLocation.WestUS2)
{
    Properties = new DirectLineChannel()
    {
        Properties = new DirectLineChannelPropertie

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Management plane SDK for provisioning and managing Azure Bot Service resources via Azure Resource Manager.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.ResourceManager.BotService (.NET)
- Para tarefas relacionadas a azureresourcemanagerbotservice net

## Diretrizes Específicas

