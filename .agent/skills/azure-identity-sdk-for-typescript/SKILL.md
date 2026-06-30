---
name: azure-identity-sdk-for-typescript
description: Authenticate to Azure services with various credential types.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Identity SDK for TypeScript

## Backstory

Você é um agente especializado em Azure Identity SDK for TypeScript.

## Contexto Original da Skill
Azure Identity SDK for TypeScript

## Instruções
---
name: azure-identity-ts
description: "Authenticate to Azure services with various credential types."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure Identity SDK for TypeScript

Authenticate to Azure services with various credential types.

## Installation

```bash
npm install @azure/identity
```

## Environment Variables

### Service Principal (Secret)

```bash
AZURE_TENANT_ID=<tenant-id>
AZURE_CLIENT_ID=<client-id>
AZURE_CLIENT_SECRET=<client-secret>
```

### Service Principal (Certificate)

```bash
AZURE_TENANT_ID=<tenant-id>
AZURE_CLIENT_ID=<client-id>
AZURE_CLIENT_CERTIFICATE_PATH=/path/to/cert.pem
AZURE_CLIENT_CERTIFICATE_PASSWORD=<optional-password>
```

### Workload Identity (Kubernetes)

```bash
AZURE_TENANT_ID=<tenant-id>
AZURE_CLIENT_ID=<client-id>
AZURE_FEDERATED_TOKEN_FILE=/var/run/secrets/tokens/azure-identity
```

## DefaultAzureCredential (Recommended)

```typescript
import { DefaultAzureCredential } from "@azure/identity";

const credential = new DefaultAzureCredential();

// Use with any Azure SDK client
import { BlobServiceClient } from "@azure/storage-blob";
const blobClient = new BlobServiceClient(
  "https://<account>.blob.core.windows.net",
  credential
);
```

**Credential Chain Order:**
1. EnvironmentCredential
2. WorkloadIdentityCredential
3. ManagedIdentityCredential
4. VisualStudioCodeCredential
5. AzureCliCredential
6. AzurePowerShellCredential
7. AzureDeveloperCliCredential

## Managed Identity

### System-Assigned

```typescript
import { ManagedIdentityCredential } from "@azure/identity";

const credential = new ManagedIdentityCredential();
```

### User-Assigned (by Client ID)

```typescript
const credential = new ManagedIdentityCredential({
  clientId: "<user-assigned-client-id>"
});
```

### User-Assigned (by Resource ID)

```typescript
const credential = new ManagedIdentityCredential({
  resourceId: "/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<name>"
});
```

## Service Principal

### Client Secret

```typescript
import { ClientSecretCredential } from "@azure/identity";

const credential = new ClientSecretCredential(
  "<tenant-id>",
  "<client-id>",
  "<client-secret>"
);
```

### Client Certificate

```typescript
import { ClientCertificateCredential } from "@azure/identity";

const credential = new ClientCertificateCredential(
  "<tenant-id>",
  "<client-id>",
  { certificatePath: "/path/to/cert.pem" }
);

// With password
const credentialWithPwd = new ClientCertificateCredential(
  "<tenant-id>",
  "<client-id>",
  { 
    certificatePath: "/path/to/cert.pem",
    certificatePassword: "<password>"
  }
);
```

## Interactive Authentication

### Browser-Based Login

```typescript
import { InteractiveBrowserCredential } from "@azure/identity";

const credential = new InteractiveBrowserCredential({
  clientId: "<client-id>",
  tenantId: "<tenant-id>",
  loginHint: "user@example.com"
});
```

### Device Code Flow

```typescript
impor

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Authenticate to Azure services with various credential types.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Identity SDK for TypeScript
- Para tarefas relacionadas a azure identity sdk for typescript

## Diretrizes Específicas

