---
name: azure-ai-text-translation-sdk-for-python
description: Client library for Azure AI Translator text translation service for real-time text translation, transliteration, and language operations.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure AI Text Translation SDK for Python

## Backstory

Você é um agente especializado em Azure AI Text Translation SDK for Python.

## Contexto Original da Skill
Azure AI Text Translation SDK for Python

## Instruções
---
name: azure-ai-translation-text-py
description: Azure AI Text Translation SDK for real-time text translation, transliteration, language detection, and dictionary lookup. Use for translating text content in applications.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure AI Text Translation SDK for Python

Client library for Azure AI Translator text translation service for real-time text translation, transliteration, and language operations.

## Installation

```bash
pip install azure-ai-translation-text
```

## Environment Variables

```bash
AZURE_TRANSLATOR_KEY=<your-api-key>
AZURE_TRANSLATOR_REGION=<your-region>  # e.g., eastus, westus2
# Or use custom endpoint
AZURE_TRANSLATOR_ENDPOINT=https://<resource>.cognitiveservices.azure.com
```

## Authentication

### API Key with Region

```python
import os
from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential

key = os.environ["AZURE_TRANSLATOR_KEY"]
region = os.environ["AZURE_TRANSLATOR_REGION"]

# Create credential with region
credential = AzureKeyCredential(key)
client = TextTranslationClient(credential=credential, region=region)
```

### API Key with Custom Endpoint

```python
endpoint = os.environ["AZURE_TRANSLATOR_ENDPOINT"]

client = TextTranslationClient(
    credential=AzureKeyCredential(key),
    endpoint=endpoint
)
```

### Entra ID (Recommended)

```python
from azure.ai.translation.text import TextTranslationClient
from azure.identity import DefaultAzureCredential

client = TextTranslationClient(
    credential=DefaultAzureCredential(),
    endpoint=os.environ["AZURE_TRANSLATOR_ENDPOINT"]
)
```

## Basic Translation

```python
# Translate to a single language
result = client.translate(
    body=["Hello, how are you?", "Welcome to Azure!"],
    to=["es"]  # Spanish
)

for item in result:
    for translation in item.translations:
        print(f"Translated: {translation.text}")
        print(f"Target language: {translation.to}")
```

## Translate to Multiple Languages

```python
result = client.translate(
    body=["Hello, world!"],
    to=["es", "fr", "de", "ja"]  # Spanish, French, German, Japanese
)

for item in result:
    print(f"Source: {item.detected_language.language if item.detected_language else 'unknown'}")
    for translation in item.translations:
        print(f"  {translation.to}: {translation.text}")
```

## Specify Source Language

```python
result = client.translate(
    body=["Bonjour le monde"],
    from_parameter="fr",  # Source is French
    to=["en", "es"]
)
```

## Language Detection

```python
result = client.translate(
    body=["Hola, como estas?"],
    to=["en"]
)

for item in result:
    if item.detected_language:
        print(f"Detected language: {item.detected_language.language}")
        print(f"Confidence: {item.detected_language.score:.2f}")
```

## Transliteration

Convert text from one script to another:

```python
result = client.transliterate(
    body=["konnichiwa"],
   

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Client library for Azure AI Translator text translation service for real-time text translation, transliteration, and language operations.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure AI Text Translation SDK for Python
- Para tarefas relacionadas a azure ai text translation sdk for python

## Diretrizes Específicas

