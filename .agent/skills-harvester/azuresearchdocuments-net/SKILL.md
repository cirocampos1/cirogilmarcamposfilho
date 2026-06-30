---
name: azuresearchdocuments-net
description: Build search applications with full-text, vector, semantic, and hybrid search capabilities.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.Search.Documents (.NET)

## Backstory

Você é um agente especializado em Azure.Search.Documents (.NET).

## Contexto Original da Skill
Azure.Search.Documents (.NET)

## Instruções
---
name: azure-search-documents-dotnet
description: Azure AI Search SDK for .NET (Azure.Search.Documents). Use for building search applications with full-text, vector, semantic, and hybrid search.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.Search.Documents (.NET)

Build search applications with full-text, vector, semantic, and hybrid search capabilities.

## Installation

```bash
dotnet add package Azure.Search.Documents
dotnet add package Azure.Identity
```

**Current Versions**: Stable v11.7.0, Preview v11.8.0-beta.1

## Environment Variables

```bash
SEARCH_ENDPOINT=https://<search-service>.search.windows.net
SEARCH_INDEX_NAME=<index-name>
# For API key auth (not recommended for production)
SEARCH_API_KEY=<api-key>
```

## Authentication

**DefaultAzureCredential (preferred)**:
```csharp
using Azure.Identity;
using Azure.Search.Documents;

var credential = new DefaultAzureCredential();
var client = new SearchClient(
    new Uri(Environment.GetEnvironmentVariable("SEARCH_ENDPOINT")),
    Environment.GetEnvironmentVariable("SEARCH_INDEX_NAME"),
    credential);
```

**API Key**:
```csharp
using Azure;
using Azure.Search.Documents;

var credential = new AzureKeyCredential(
    Environment.GetEnvironmentVariable("SEARCH_API_KEY"));
var client = new SearchClient(
    new Uri(Environment.GetEnvironmentVariable("SEARCH_ENDPOINT")),
    Environment.GetEnvironmentVariable("SEARCH_INDEX_NAME"),
    credential);
```

## Client Selection

| Client | Purpose |
|--------|---------|
| `SearchClient` | Query indexes, upload/update/delete documents |
| `SearchIndexClient` | Create/manage indexes, synonym maps |
| `SearchIndexerClient` | Manage indexers, skillsets, data sources |

## Index Creation

### Using FieldBuilder (Recommended)

```csharp
using Azure.Search.Documents.Indexes;
using Azure.Search.Documents.Indexes.Models;

// Define model with attributes
public class Hotel
{
    [SimpleField(IsKey = true, IsFilterable = true)]
    public string HotelId { get; set; }

    [SearchableField(IsSortable = true)]
    public string HotelName { get; set; }

    [SearchableField(AnalyzerName = LexicalAnalyzerName.EnLucene)]
    public string Description { get; set; }

    [SimpleField(IsFilterable = true, IsSortable = true, IsFacetable = true)]
    public double? Rating { get; set; }

    [VectorSearchField(VectorSearchDimensions = 1536, VectorSearchProfileName = "vector-profile")]
    public ReadOnlyMemory<float>? DescriptionVector { get; set; }
}

// Create index
var indexClient = new SearchIndexClient(endpoint, credential);
var fieldBuilder = new FieldBuilder();
var fields = fieldBuilder.Build(typeof(Hotel));

var index = new SearchIndex("hotels")
{
    Fields = fields,
    VectorSearch = new VectorSearch
    {
        Profiles = { new VectorSearchProfile("vector-profile", "hnsw-algo") },
        Algorithms = { new HnswAlgorithmConfiguration("hnsw-algo") }
    }
};

await indexClient.CreateOrUpdateIndexAsync(index);
```

### Manual F

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Build search applications with full-text, vector, semantic, and hybrid search capabilities.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.Search.Documents (.NET)
- Para tarefas relacionadas a azuresearchdocuments net

## Diretrizes Específicas

