---
name: azure-container-registry-sdk-for-python
description: Manage container images, artifacts, and repositories in Azure Container Registry.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Container Registry SDK for Python

## Backstory

Você é um agente especializado em Azure Container Registry SDK for Python.

## Contexto Original da Skill
Azure Container Registry SDK for Python

## Instruções
---
name: azure-containerregistry-py
description: Azure Container Registry SDK for Python. Use for managing container images, artifacts, and repositories.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure Container Registry SDK for Python

Manage container images, artifacts, and repositories in Azure Container Registry.

## Installation

```bash
pip install azure-containerregistry
```

## Environment Variables

```bash
AZURE_CONTAINERREGISTRY_ENDPOINT=https://<registry-name>.azurecr.io
```

## Authentication

### Entra ID (Recommended)

```python
from azure.containerregistry import ContainerRegistryClient
from azure.identity import DefaultAzureCredential

client = ContainerRegistryClient(
    endpoint=os.environ["AZURE_CONTAINERREGISTRY_ENDPOINT"],
    credential=DefaultAzureCredential()
)
```

### Anonymous Access (Public Registry)

```python
from azure.containerregistry import ContainerRegistryClient

client = ContainerRegistryClient(
    endpoint="https://mcr.microsoft.com",
    credential=None,
    audience="https://mcr.microsoft.com"
)
```

## List Repositories

```python
client = ContainerRegistryClient(endpoint, DefaultAzureCredential())

for repository in client.list_repository_names():
    print(repository)
```

## Repository Operations

### Get Repository Properties

```python
properties = client.get_repository_properties("my-image")
print(f"Created: {properties.created_on}")
print(f"Modified: {properties.last_updated_on}")
print(f"Manifests: {properties.manifest_count}")
print(f"Tags: {properties.tag_count}")
```

### Update Repository Properties

```python
from azure.containerregistry import RepositoryProperties

client.update_repository_properties(
    "my-image",
    properties=RepositoryProperties(
        can_delete=False,
        can_write=False
    )
)
```

### Delete Repository

```python
client.delete_repository("my-image")
```

## List Tags

```python
for tag in client.list_tag_properties("my-image"):
    print(f"{tag.name}: {tag.created_on}")
```

### Filter by Order

```python
from azure.containerregistry import ArtifactTagOrder

# Most recent first
for tag in client.list_tag_properties(
    "my-image",
    order_by=ArtifactTagOrder.LAST_UPDATED_ON_DESCENDING
):
    print(f"{tag.name}: {tag.last_updated_on}")
```

## Manifest Operations

### List Manifests

```python
from azure.containerregistry import ArtifactManifestOrder

for manifest in client.list_manifest_properties(
    "my-image",
    order_by=ArtifactManifestOrder.LAST_UPDATED_ON_DESCENDING
):
    print(f"Digest: {manifest.digest}")
    print(f"Tags: {manifest.tags}")
    print(f"Size: {manifest.size_in_bytes}")
```

### Get Manifest Properties

```python
manifest = client.get_manifest_properties("my-image", "latest")
print(f"Digest: {manifest.digest}")
print(f"Architecture: {manifest.architecture}")
print(f"OS: {manifest.operating_system}")
```

### Update Manifest Properties

```python
from azure.containerregistry import ArtifactManifestProper

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Manage container images, artifacts, and repositories in Azure Container Registry.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Container Registry SDK for Python
- Para tarefas relacionadas a azure container registry sdk for python

## Diretrizes Específicas

