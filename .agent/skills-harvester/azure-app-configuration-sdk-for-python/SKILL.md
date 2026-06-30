---
name: azure-app-configuration-sdk-for-python
description: Centralized configuration management with feature flags and dynamic settings.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure App Configuration SDK for Python

## Backstory

Você é um agente especializado em Azure App Configuration SDK for Python.

## Contexto Original da Skill
Azure App Configuration SDK for Python

## Instruções
---
name: azure-appconfiguration-py
description: Azure App Configuration SDK for Python. Use for centralized configuration management, feature flags, and dynamic settings.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure App Configuration SDK for Python

Centralized configuration management with feature flags and dynamic settings.

## Installation

```bash
pip install azure-appconfiguration
```

## Environment Variables

```bash
AZURE_APPCONFIGURATION_CONNECTION_STRING=Endpoint=https://<name>.azconfig.io;Id=...;Secret=...
# Or for Entra ID:
AZURE_APPCONFIGURATION_ENDPOINT=https://<name>.azconfig.io
```

## Authentication

### Connection String

```python
from azure.appconfiguration import AzureAppConfigurationClient

client = AzureAppConfigurationClient.from_connection_string(
    os.environ["AZURE_APPCONFIGURATION_CONNECTION_STRING"]
)
```

### Entra ID

```python
from azure.appconfiguration import AzureAppConfigurationClient
from azure.identity import DefaultAzureCredential

client = AzureAppConfigurationClient(
    base_url=os.environ["AZURE_APPCONFIGURATION_ENDPOINT"],
    credential=DefaultAzureCredential()
)
```

## Configuration Settings

### Get Setting

```python
setting = client.get_configuration_setting(key="app:settings:message")
print(f"{setting.key} = {setting.value}")
```

### Get with Label

```python
# Labels allow environment-specific values
setting = client.get_configuration_setting(
    key="app:settings:message",
    label="production"
)
```

### Set Setting

```python
from azure.appconfiguration import ConfigurationSetting

setting = ConfigurationSetting(
    key="app:settings:message",
    value="Hello, World!",
    label="development",
    content_type="text/plain",
    tags={"environment": "dev"}
)

client.set_configuration_setting(setting)
```

### Delete Setting

```python
client.delete_configuration_setting(
    key="app:settings:message",
    label="development"
)
```

## List Settings

### All Settings

```python
settings = client.list_configuration_settings()
for setting in settings:
    print(f"{setting.key} [{setting.label}] = {setting.value}")
```

### Filter by Key Prefix

```python
settings = client.list_configuration_settings(
    key_filter="app:settings:*"
)
```

### Filter by Label

```python
settings = client.list_configuration_settings(
    label_filter="production"
)
```

## Feature Flags

### Set Feature Flag

```python
from azure.appconfiguration import ConfigurationSetting
import json

feature_flag = ConfigurationSetting(
    key=".appconfig.featureflag/beta-feature",
    value=json.dumps({
        "id": "beta-feature",
        "enabled": True,
        "conditions": {
            "client_filters": []
        }
    }),
    content_type="application/vnd.microsoft.appconfig.ff+json;charset=utf-8"
)

client.set_configuration_setting(feature_flag)
```

### Get Feature Flag

```python
setting = client.get_configuration_setting(
    key=".appconfig.featureflag/beta-feature"
)
flag_data =

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Centralized configuration management with feature flags and dynamic settings.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure App Configuration SDK for Python
- Para tarefas relacionadas a azure app configuration sdk for python

## Diretrizes Específicas

