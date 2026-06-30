---
name: azure-key-vault-sdk-for-python
description: Secure storage and management for secrets, cryptographic keys, and certificates.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Key Vault SDK for Python

## Backstory

Você é um agente especializado em Azure Key Vault SDK for Python.

## Contexto Original da Skill
Azure Key Vault SDK for Python

## Instruções
---
name: azure-keyvault-py
description: Azure Key Vault SDK for Python. Use for secrets, keys, and certificates management with secure storage.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure Key Vault SDK for Python

Secure storage and management for secrets, cryptographic keys, and certificates.

## Installation

```bash
# Secrets
pip install azure-keyvault-secrets azure-identity

# Keys (cryptographic operations)
pip install azure-keyvault-keys azure-identity

# Certificates
pip install azure-keyvault-certificates azure-identity

# All
pip install azure-keyvault-secrets azure-keyvault-keys azure-keyvault-certificates azure-identity
```

## Environment Variables

```bash
AZURE_KEYVAULT_URL=https://<vault-name>.vault.azure.net/
```

## Secrets

### SecretClient Setup

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()
vault_url = "https://<vault-name>.vault.azure.net/"

client = SecretClient(vault_url=vault_url, credential=credential)
```

### Secret Operations

```python
# Set secret
secret = client.set_secret("database-password", "super-secret-value")
print(f"Created: {secret.name}, version: {secret.properties.version}")

# Get secret
secret = client.get_secret("database-password")
print(f"Value: {secret.value}")

# Get specific version
secret = client.get_secret("database-password", version="abc123")

# List secrets (names only, not values)
for secret_properties in client.list_properties_of_secrets():
    print(f"Secret: {secret_properties.name}")

# List versions
for version in client.list_properties_of_secret_versions("database-password"):
    print(f"Version: {version.version}, Created: {version.created_on}")

# Delete secret (soft delete)
poller = client.begin_delete_secret("database-password")
deleted_secret = poller.result()

# Purge (permanent delete, if soft-delete enabled)
client.purge_deleted_secret("database-password")

# Recover deleted secret
client.begin_recover_deleted_secret("database-password").result()
```

## Keys

### KeyClient Setup

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient

credential = DefaultAzureCredential()
vault_url = "https://<vault-name>.vault.azure.net/"

client = KeyClient(vault_url=vault_url, credential=credential)
```

### Key Operations

```python
from azure.keyvault.keys import KeyType

# Create RSA key
rsa_key = client.create_rsa_key("rsa-key", size=2048)

# Create EC key
ec_key = client.create_ec_key("ec-key", curve="P-256")

# Get key
key = client.get_key("rsa-key")
print(f"Key type: {key.key_type}")

# List keys
for key_properties in client.list_properties_of_keys():
    print(f"Key: {key_properties.name}")

# Delete key
poller = client.begin_delete_key("rsa-key")
deleted_key = poller.result()
```

### Cryptographic Operations

```python
from azure.keyvault.keys.crypto import CryptographyClient, EncryptionAlgorithm

# Get crypt

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Secure storage and management for secrets, cryptographic keys, and certificates.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Key Vault SDK for Python
- Para tarefas relacionadas a azure key vault sdk for python

## Diretrizes Específicas

