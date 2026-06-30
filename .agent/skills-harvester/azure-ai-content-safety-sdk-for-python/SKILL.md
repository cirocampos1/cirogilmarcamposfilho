---
name: azure-ai-content-safety-sdk-for-python
description: Detect harmful user-generated and AI-generated content in applications.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure AI Content Safety SDK for Python

## Backstory

Você é um agente especializado em Azure AI Content Safety SDK for Python.

## Contexto Original da Skill
Azure AI Content Safety SDK for Python

## Instruções
---
name: azure-ai-contentsafety-py
description: Azure AI Content Safety SDK for Python. Use for detecting harmful content in text and images with multi-severity classification.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure AI Content Safety SDK for Python

Detect harmful user-generated and AI-generated content in applications.

## Installation

```bash
pip install azure-ai-contentsafety
```

## Environment Variables

```bash
CONTENT_SAFETY_ENDPOINT=https://<resource>.cognitiveservices.azure.com
CONTENT_SAFETY_KEY=<your-api-key>
```

## Authentication

### API Key

```python
from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
import os

client = ContentSafetyClient(
    endpoint=os.environ["CONTENT_SAFETY_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["CONTENT_SAFETY_KEY"])
)
```

### Entra ID

```python
from azure.ai.contentsafety import ContentSafetyClient
from azure.identity import DefaultAzureCredential

client = ContentSafetyClient(
    endpoint=os.environ["CONTENT_SAFETY_ENDPOINT"],
    credential=DefaultAzureCredential()
)
```

## Analyze Text

```python
from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeTextOptions, TextCategory
from azure.core.credentials import AzureKeyCredential

client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

request = AnalyzeTextOptions(text="Your text content to analyze")
response = client.analyze_text(request)

# Check each category
for category in [TextCategory.HATE, TextCategory.SELF_HARM, 
                 TextCategory.SEXUAL, TextCategory.VIOLENCE]:
    result = next((r for r in response.categories_analysis 
                   if r.category == category), None)
    if result:
        print(f"{category}: severity {result.severity}")
```

## Analyze Image

```python
from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeImageOptions, ImageData
from azure.core.credentials import AzureKeyCredential
import base64

client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

# From file
with open("image.jpg", "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

request = AnalyzeImageOptions(
    image=ImageData(content=image_data)
)

response = client.analyze_image(request)

for result in response.categories_analysis:
    print(f"{result.category}: severity {result.severity}")
```

### Image from URL

```python
from azure.ai.contentsafety.models import AnalyzeImageOptions, ImageData

request = AnalyzeImageOptions(
    image=ImageData(blob_url="https://example.com/image.jpg")
)

response = client.analyze_image(request)
```

## Text Blocklist Management

### Create Blocklist

```python
from azure.ai.contentsafety import BlocklistClient
from azure.ai.contentsafety.models import TextBlocklist
from azure.core.credentials import AzureKeyCredential

blocklist_client = BlocklistClient(endpoint, A

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Detect harmful user-generated and AI-generated content in applications.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure AI Content Safety SDK for Python
- Para tarefas relacionadas a azure ai content safety sdk for python

## Diretrizes Específicas

