---
name: azure-ai-search-sdk-for-python
description: Full-text, vector, and hybrid search with AI enrichment capabilities.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure AI Search SDK for Python

## Backstory

Você é um agente especializado em Azure AI Search SDK for Python.

## Contexto Original da Skill
Azure AI Search SDK for Python

## Instruções
---
name: azure-search-documents-py
description: Azure AI Search SDK for Python. Use for vector search, hybrid search, semantic ranking, indexing, and skillsets.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure AI Search SDK for Python

Full-text, vector, and hybrid search with AI enrichment capabilities.

## Installation

```bash
pip install azure-search-documents
```

## Environment Variables

```bash
AZURE_SEARCH_ENDPOINT=https://<service-name>.search.windows.net
AZURE_SEARCH_API_KEY=<your-api-key>
AZURE_SEARCH_INDEX_NAME=<your-index-name>
```

## Authentication

### API Key

```python
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

client = SearchClient(
    endpoint=os.environ["AZURE_SEARCH_ENDPOINT"],
    index_name=os.environ["AZURE_SEARCH_INDEX_NAME"],
    credential=AzureKeyCredential(os.environ["AZURE_SEARCH_API_KEY"])
)
```

### Entra ID (Recommended)

```python
from azure.search.documents import SearchClient
from azure.identity import DefaultAzureCredential

client = SearchClient(
    endpoint=os.environ["AZURE_SEARCH_ENDPOINT"],
    index_name=os.environ["AZURE_SEARCH_INDEX_NAME"],
    credential=DefaultAzureCredential()
)
```

## Client Types

| Client | Purpose |
|--------|---------|
| `SearchClient` | Search and document operations |
| `SearchIndexClient` | Index management, synonym maps |
| `SearchIndexerClient` | Indexers, data sources, skillsets |

## Create Index with Vector Field

```python
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
    SearchableField,
    SimpleField
)

index_client = SearchIndexClient(endpoint, AzureKeyCredential(key))

fields = [
    SimpleField(name="id", type=SearchFieldDataType.String, key=True),
    SearchableField(name="title", type=SearchFieldDataType.String),
    SearchableField(name="content", type=SearchFieldDataType.String),
    SearchField(
        name="content_vector",
        type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
        searchable=True,
        vector_search_dimensions=1536,
        vector_search_profile_name="my-vector-profile"
    )
]

vector_search = VectorSearch(
    algorithms=[
        HnswAlgorithmConfiguration(name="my-hnsw")
    ],
    profiles=[
        VectorSearchProfile(
            name="my-vector-profile",
            algorithm_configuration_name="my-hnsw"
        )
    ]
)

index = SearchIndex(
    name="my-index",
    fields=fields,
    vector_search=vector_search
)

index_client.create_or_update_index(index)
```

## Upload Documents

```python
from azure.search.documents import SearchClient

client = SearchClient(endpoint, "my-index", AzureKeyCredential(key))

documents = [
    {
        "id": "1",
        "title": "Azure AI Search",
        "content": "Full-text and vect

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Full-text, vector, and hybrid search with AI enrichment capabilities.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure AI Search SDK for Python
- Para tarefas relacionadas a azure ai search sdk for python

## Diretrizes Específicas

