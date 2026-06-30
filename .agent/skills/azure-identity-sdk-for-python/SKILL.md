---
name: azure-identity-sdk-for-python
description: Authentication library for Azure SDK clients using Microsoft Entra ID (formerly Azure AD).
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Identity SDK for Python

## Backstory

Você é um agente especializado em Azure Identity SDK for Python.

## Contexto Original da Skill
Azure Identity SDK for Python

## Instruções
---
name: azure-identity-py
description: Azure Identity SDK for Python authentication. Use for DefaultAzureCredential, managed identity, service principals, and token caching.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure Identity SDK for Python

Authentication library for Azure SDK clients using Microsoft Entra ID (formerly Azure AD).

## Installation

```bash
pip install azure-identity
```

## Environment Variables

```bash
# Service Principal (for production/CI)
AZURE_TENANT_ID=<your-tenant-id>
AZURE_CLIENT_ID=<your-client-id>
AZURE_CLIENT_SECRET=<your-client-secret>

# User-assigned Managed Identity (optional)
AZURE_CLIENT_ID=<managed-identity-client-id>
```

## DefaultAzureCredential

The recommended credential for most scenarios. Tries multiple authentication methods in order:

```python
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Works in local dev AND production without code changes
credential = DefaultAzureCredential()

client = BlobServiceClient(
    account_url="https://<account>.blob.core.windows.net",
    credential=credential
)
```

### Credential Chain Order

| Order | Credential | Environment |
|-------|-----------|-------------|
| 1 | EnvironmentCredential | CI/CD, containers |
| 2 | WorkloadIdentityCredential | Kubernetes |
| 3 | ManagedIdentityCredential | Azure VMs, App Service, Functions |
| 4 | SharedTokenCacheCredential | Windows only |
| 5 | VisualStudioCodeCredential | VS Code with Azure extension |
| 6 | AzureCliCredential | `az login` |
| 7 | AzurePowerShellCredential | `Connect-AzAccount` |
| 8 | AzureDeveloperCliCredential | `azd auth login` |

### Customizing DefaultAzureCredential

```python
# Exclude credentials you don't need
credential = DefaultAzureCredential(
    exclude_environment_credential=True,
    exclude_shared_token_cache_credential=True,
    managed_identity_client_id="<user-assigned-mi-client-id>"  # For user-assigned MI
)

# Enable interactive browser (disabled by default)
credential = DefaultAzureCredential(
    exclude_interactive_browser_credential=False
)
```

## Specific Credential Types

### ManagedIdentityCredential

For Azure-hosted resources (VMs, App Service, Functions, AKS):

```python
from azure.identity import ManagedIdentityCredential

# System-assigned managed identity
credential = ManagedIdentityCredential()

# User-assigned managed identity
credential = ManagedIdentityCredential(
    client_id="<user-assigned-mi-client-id>"
)
```

### ClientSecretCredential

For service principal with secret:

```python
from azure.identity import ClientSecretCredential

credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"]
)
```

### AzureCliCredential

Uses the account from `az login`:

```python
from azure.identity import AzureCliCredential

credential = AzureCliCredential()
```

### ChainedToke

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Authentication library for Azure SDK clients using Microsoft Entra ID (formerly Azure AD).

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Identity SDK for Python
- Para tarefas relacionadas a azure identity sdk for python

## Diretrizes Específicas

