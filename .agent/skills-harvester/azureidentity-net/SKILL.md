---
name: azureidentity-net
description: Authentication library for Azure SDK clients using Microsoft Entra ID (formerly Azure AD).
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.Identity (.NET)

## Backstory

Você é um agente especializado em Azure.Identity (.NET).

## Contexto Original da Skill
Azure.Identity (.NET)

## Instruções
---
name: azure-identity-dotnet
description: Azure Identity SDK for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use for DefaultAzureCredential, managed identity, service principals, and developer credentials.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.Identity (.NET)

Authentication library for Azure SDK clients using Microsoft Entra ID (formerly Azure AD).

## Installation

```bash
dotnet add package Azure.Identity

# For ASP.NET Core
dotnet add package Microsoft.Extensions.Azure

# For brokered authentication (Windows)
dotnet add package Azure.Identity.Broker
```

**Current Versions**: Stable v1.17.1, Preview v1.18.0-beta.2

## Environment Variables

### Service Principal with Secret
```bash
AZURE_CLIENT_ID=<application-client-id>
AZURE_TENANT_ID=<directory-tenant-id>
AZURE_CLIENT_SECRET=<client-secret-value>
```

### Service Principal with Certificate
```bash
AZURE_CLIENT_ID=<application-client-id>
AZURE_TENANT_ID=<directory-tenant-id>
AZURE_CLIENT_CERTIFICATE_PATH=<path-to-pfx-or-pem>
AZURE_CLIENT_CERTIFICATE_PASSWORD=<certificate-password>  # Optional
```

### Managed Identity
```bash
AZURE_CLIENT_ID=<user-assigned-managed-identity-client-id>  # Only for user-assigned
```

## DefaultAzureCredential

The recommended credential for most scenarios. Tries multiple authentication methods in order:

| Order | Credential | Enabled by Default |
|-------|------------|-------------------|
| 1 | EnvironmentCredential | Yes |
| 2 | WorkloadIdentityCredential | Yes |
| 3 | ManagedIdentityCredential | Yes |
| 4 | VisualStudioCredential | Yes |
| 5 | VisualStudioCodeCredential | Yes |
| 6 | AzureCliCredential | Yes |
| 7 | AzurePowerShellCredential | Yes |
| 8 | AzureDeveloperCliCredential | Yes |
| 9 | InteractiveBrowserCredential | **No** |

### Basic Usage

```csharp
using Azure.Identity;
using Azure.Storage.Blobs;

var credential = new DefaultAzureCredential();
var blobClient = new BlobServiceClient(
    new Uri("https://myaccount.blob.core.windows.net"),
    credential);
```

### ASP.NET Core with Dependency Injection

```csharp
using Azure.Identity;
using Microsoft.Extensions.Azure;

builder.Services.AddAzureClients(clientBuilder =>
{
    clientBuilder.AddBlobServiceClient(
        new Uri("https://myaccount.blob.core.windows.net"));
    clientBuilder.AddSecretClient(
        new Uri("https://myvault.vault.azure.net"));
    
    // Uses DefaultAzureCredential by default
    clientBuilder.UseCredential(new DefaultAzureCredential());
});
```

### Customizing DefaultAzureCredential

```csharp
var credential = new DefaultAzureCredential(
    new DefaultAzureCredentialOptions
    {
        ExcludeEnvironmentCredential = true,
        ExcludeManagedIdentityCredential = false,
        ExcludeVisualStudioCredential = false,
        ExcludeAzureCliCredential = false,
        ExcludeInteractiveBrowserCredential = false, // Enable interactive
        TenantId = "<tenant-id>",
        ManagedIdentityCli

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Authentication library for Azure SDK clients using Microsoft Entra ID (formerly Azure AD).

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.Identity (.NET)
- Para tarefas relacionadas a azureidentity net

## Diretrizes Específicas

