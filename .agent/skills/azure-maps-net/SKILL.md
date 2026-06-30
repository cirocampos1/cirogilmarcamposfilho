---
name: azure-maps-net
description: Azure Maps SDK for .NET providing location-based services: geocoding, routing, rendering, geolocation, and weather.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Maps (.NET)

## Backstory

Você é um agente especializado em Azure Maps (.NET).

## Contexto Original da Skill
Azure Maps (.NET)

## Instruções
---
name: azure-maps-search-dotnet
description: Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and weather. Use for address search, directions, map tiles, IP geolocation, and weather data.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure Maps (.NET)

Azure Maps SDK for .NET providing location-based services: geocoding, routing, rendering, geolocation, and weather.

## Installation

```bash
# Search (geocoding, reverse geocoding)
dotnet add package Azure.Maps.Search --prerelease

# Routing (directions, route matrix)
dotnet add package Azure.Maps.Routing --prerelease

# Rendering (map tiles, static images)
dotnet add package Azure.Maps.Rendering --prerelease

# Geolocation (IP to location)
dotnet add package Azure.Maps.Geolocation --prerelease

# Weather
dotnet add package Azure.Maps.Weather --prerelease

# Resource Management (account management, SAS tokens)
dotnet add package Azure.ResourceManager.Maps --prerelease

# Required for authentication
dotnet add package Azure.Identity
```

**Current Versions**:
- `Azure.Maps.Search`: v2.0.0-beta.5
- `Azure.Maps.Routing`: v1.0.0-beta.4
- `Azure.Maps.Rendering`: v2.0.0-beta.1
- `Azure.Maps.Geolocation`: v1.0.0-beta.3
- `Azure.ResourceManager.Maps`: v1.1.0-beta.2

## Environment Variables

```bash
AZURE_MAPS_SUBSCRIPTION_KEY=<your-subscription-key>
AZURE_MAPS_CLIENT_ID=<your-client-id>  # For Entra ID auth
```

## Authentication

### Subscription Key (Shared Key)

```csharp
using Azure;
using Azure.Maps.Search;

var subscriptionKey = Environment.GetEnvironmentVariable("AZURE_MAPS_SUBSCRIPTION_KEY");
var credential = new AzureKeyCredential(subscriptionKey);

var client = new MapsSearchClient(credential);
```

### Microsoft Entra ID (Recommended for Production)

```csharp
using Azure.Identity;
using Azure.Maps.Search;

var credential = new DefaultAzureCredential();
var clientId = Environment.GetEnvironmentVariable("AZURE_MAPS_CLIENT_ID");

var client = new MapsSearchClient(credential, clientId);
```

### Shared Access Signature (SAS)

```csharp
using Azure;
using Azure.Core;
using Azure.Identity;
using Azure.ResourceManager;
using Azure.ResourceManager.Maps;
using Azure.ResourceManager.Maps.Models;
using Azure.Maps.Search;

// Authenticate with Azure Resource Manager
ArmClient armClient = new ArmClient(new DefaultAzureCredential());

// Get Maps account resource
ResourceIdentifier mapsAccountResourceId = MapsAccountResource.CreateResourceIdentifier(
    subscriptionId, resourceGroupName, accountName);
MapsAccountResource mapsAccount = armClient.GetMapsAccountResource(mapsAccountResourceId);

// Generate SAS token
MapsAccountSasContent sasContent = new MapsAccountSasContent(
    MapsSigningKey.PrimaryKey, 
    principalId, 
    maxRatePerSecond: 500, 
    start: DateTime.UtcNow.ToString("O"), 
    expiry: DateTime.UtcNow.AddDays(1).ToString("O"));

Response<MapsAccountSasToken> sas = mapsAccount.GetSas(sasContent);

// Create client

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Azure Maps SDK for .NET providing location-based services: geocoding, routing, rendering, geolocation, and weather.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Maps (.NET)
- Para tarefas relacionadas a azure maps net

## Diretrizes Específicas

