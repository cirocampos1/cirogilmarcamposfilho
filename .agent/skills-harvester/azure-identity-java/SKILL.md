---
name: azure-identity-java
description: Authenticate Java applications with Azure services using Microsoft Entra ID (Azure AD).
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Identity (Java)

## Backstory

Você é um agente especializado em Azure Identity (Java).

## Contexto Original da Skill
Azure Identity (Java)

## Instruções
---
name: azure-identity-java
description: "Authenticate Java applications with Azure services using Microsoft Entra ID (Azure AD)."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure Identity (Java)

Authenticate Java applications with Azure services using Microsoft Entra ID (Azure AD).

## Installation

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-identity</artifactId>
    <version>1.15.0</version>
</dependency>
```

## Key Concepts

| Credential | Use Case |
|------------|----------|
| `DefaultAzureCredential` | **Recommended** - Works in dev and production |
| `ManagedIdentityCredential` | Azure-hosted apps (App Service, Functions, VMs) |
| `EnvironmentCredential` | CI/CD pipelines with env vars |
| `ClientSecretCredential` | Service principals with secret |
| `ClientCertificateCredential` | Service principals with certificate |
| `AzureCliCredential` | Local dev using `az login` |
| `InteractiveBrowserCredential` | Interactive login flow |
| `DeviceCodeCredential` | Headless device authentication |

## DefaultAzureCredential (Recommended)

The `DefaultAzureCredential` tries multiple authentication methods in order:

1. Environment variables
2. Workload Identity
3. Managed Identity
4. Azure CLI
5. Azure PowerShell
6. Azure Developer CLI

```java
import com.azure.identity.DefaultAzureCredential;
import com.azure.identity.DefaultAzureCredentialBuilder;

// Simple usage
DefaultAzureCredential credential = new DefaultAzureCredentialBuilder().build();

// Use with any Azure client
BlobServiceClient blobClient = new BlobServiceClientBuilder()
    .endpoint("https://<storage-account>.blob.core.windows.net")
    .credential(credential)
    .buildClient();

KeyClient keyClient = new KeyClientBuilder()
    .vaultUrl("https://<vault-name>.vault.azure.net")
    .credential(credential)
    .buildClient();
```

### Configure DefaultAzureCredential

```java
DefaultAzureCredential credential = new DefaultAzureCredentialBuilder()
    .managedIdentityClientId("<user-assigned-identity-client-id>")  // For user-assigned MI
    .tenantId("<tenant-id>")                                        // Limit to specific tenant
    .excludeEnvironmentCredential()                                 // Skip env vars
    .excludeAzureCliCredential()                                    // Skip Azure CLI
    .build();
```

## Managed Identity

For Azure-hosted applications (App Service, Functions, AKS, VMs).

```java
import com.azure.identity.ManagedIdentityCredential;
import com.azure.identity.ManagedIdentityCredentialBuilder;

// System-assigned managed identity
ManagedIdentityCredential credential = new ManagedIdentityCredentialBuilder()
    .build();

// User-assigned managed identity (by client ID)
ManagedIdentityCredential credential = new ManagedIdentityCredentialBuilder()
    .clientId("<user-assigned-client-id>")
    .build();

// User-assigned managed identity (by resource ID)
ManagedIdentityCredential credential = new Mana

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Authenticate Java applications with Azure services using Microsoft Entra ID (Azure AD).

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Identity (Java)
- Para tarefas relacionadas a azure identity java

## Diretrizes Específicas

