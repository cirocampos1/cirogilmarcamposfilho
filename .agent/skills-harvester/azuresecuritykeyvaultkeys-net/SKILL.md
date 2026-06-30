---
name: azuresecuritykeyvaultkeys-net
description: Client library for managing cryptographic keys in Azure Key Vault and Managed HSM.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure.Security.KeyVault.Keys (.NET)

## Backstory

Você é um agente especializado em Azure.Security.KeyVault.Keys (.NET).

## Contexto Original da Skill
Azure.Security.KeyVault.Keys (.NET)

## Instruções
---
name: azure-security-keyvault-keys-dotnet
description: Azure Key Vault Keys SDK for .NET. Client library for managing cryptographic keys in Azure Key Vault and Managed HSM. Use for key creation, rotation, encryption, decryption, signing, and verification.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure.Security.KeyVault.Keys (.NET)

Client library for managing cryptographic keys in Azure Key Vault and Managed HSM.

## Installation

```bash
dotnet add package Azure.Security.KeyVault.Keys
dotnet add package Azure.Identity
```

**Current Version**: 4.7.0 (stable)

## Environment Variables

```bash
KEY_VAULT_NAME=<your-key-vault-name>
# Or full URI
AZURE_KEYVAULT_URL=https://<vault-name>.vault.azure.net
```

## Client Hierarchy

```
KeyClient (key management)
├── CreateKey / CreateRsaKey / CreateEcKey
├── GetKey / GetKeys
├── UpdateKeyProperties
├── DeleteKey / PurgeDeletedKey
├── BackupKey / RestoreKey
└── GetCryptographyClient() → CryptographyClient

CryptographyClient (cryptographic operations)
├── Encrypt / Decrypt
├── WrapKey / UnwrapKey
├── Sign / Verify
└── SignData / VerifyData

KeyResolver (key resolution)
└── Resolve(keyId) → CryptographyClient
```

## Authentication

### DefaultAzureCredential (Recommended)

```csharp
using Azure.Identity;
using Azure.Security.KeyVault.Keys;

var keyVaultName = Environment.GetEnvironmentVariable("KEY_VAULT_NAME");
var kvUri = $"https://{keyVaultName}.vault.azure.net";

var client = new KeyClient(new Uri(kvUri), new DefaultAzureCredential());
```

### Service Principal

```csharp
var credential = new ClientSecretCredential(
    tenantId: "<tenant-id>",
    clientId: "<client-id>",
    clientSecret: "<client-secret>");

var client = new KeyClient(new Uri(kvUri), credential);
```

## Key Management

### Create Keys

```csharp
// Create RSA key
KeyVaultKey rsaKey = await client.CreateKeyAsync("my-rsa-key", KeyType.Rsa);
Console.WriteLine($"Created key: {rsaKey.Name}, Type: {rsaKey.KeyType}");

// Create RSA key with options
var rsaOptions = new CreateRsaKeyOptions("my-rsa-key-2048")
{
    KeySize = 2048,
    HardwareProtected = false, // true for HSM-backed
    ExpiresOn = DateTimeOffset.UtcNow.AddYears(1),
    NotBefore = DateTimeOffset.UtcNow,
    Enabled = true
};
rsaOptions.KeyOperations.Add(KeyOperation.Encrypt);
rsaOptions.KeyOperations.Add(KeyOperation.Decrypt);

KeyVaultKey rsaKey2 = await client.CreateRsaKeyAsync(rsaOptions);

// Create EC key
var ecOptions = new CreateEcKeyOptions("my-ec-key")
{
    CurveName = KeyCurveName.P256,
    HardwareProtected = true // HSM-backed
};
KeyVaultKey ecKey = await client.CreateEcKeyAsync(ecOptions);

// Create Oct (symmetric) key for wrap/unwrap
var octOptions = new CreateOctKeyOptions("my-oct-key")
{
    KeySize = 256,
    HardwareProtected = true
};
KeyVaultKey octKey = await client.CreateOctKeyAsync(octOptions);
```

### Retrieve Keys

```csharp
// Get specific key (latest version)
KeyVaultKey key = await client.GetKeyAsync("my-rsa-key

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Client library for managing cryptographic keys in Azure Key Vault and Managed HSM.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure.Security.KeyVault.Keys (.NET)
- Para tarefas relacionadas a azuresecuritykeyvaultkeys net

## Diretrizes Específicas

