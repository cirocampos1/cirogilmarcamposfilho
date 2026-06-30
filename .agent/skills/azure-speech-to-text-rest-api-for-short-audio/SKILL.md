---
name: azure-speech-to-text-rest-api-for-short-audio
description: Simple REST API for speech-to-text transcription of short audio files (up to 60 seconds). No SDK required - just HTTP requests.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Speech to Text REST API for Short Audio

## Backstory

Você é um agente especializado em Azure Speech to Text REST API for Short Audio.

## Contexto Original da Skill
Azure Speech to Text REST API for Short Audio

## Instruções
---
name: azure-speech-to-text-rest-py
description: Azure Speech to Text REST API for short audio (Python). Use for simple speech recognition of audio files up to 60 seconds without the Speech SDK.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure Speech to Text REST API for Short Audio

Simple REST API for speech-to-text transcription of short audio files (up to 60 seconds). No SDK required - just HTTP requests.

## Prerequisites

1. **Azure subscription** - [Create one free](https://azure.microsoft.com/free/)
2. **Speech resource** - Create in [Azure Portal](https://portal.azure.com/#create/Microsoft.CognitiveServicesSpeechServices)
3. **Get credentials** - After deployment, go to resource > Keys and Endpoint

## Environment Variables

```bash
# Required
AZURE_SPEECH_KEY=<your-speech-resource-key>
AZURE_SPEECH_REGION=<region>  # e.g., eastus, westus2, westeurope

# Alternative: Use endpoint directly
AZURE_SPEECH_ENDPOINT=https://<region>.stt.speech.microsoft.com
```

## Installation

```bash
pip install requests
```

## Quick Start

```python
import os
import requests

def transcribe_audio(audio_file_path: str, language: str = "en-US") -> dict:
    """Transcribe short audio file (max 60 seconds) using REST API."""
    region = os.environ["AZURE_SPEECH_REGION"]
    api_key = os.environ["AZURE_SPEECH_KEY"]
    
    url = f"https://{region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1"
    
    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "audio/wav; codecs=audio/pcm; samplerate=16000",
        "Accept": "application/json"
    }
    
    params = {
        "language": language,
        "format": "detailed"  # or "simple"
    }
    
    with open(audio_file_path, "rb") as audio_file:
        response = requests.post(url, headers=headers, params=params, data=audio_file)
    
    response.raise_for_status()
    return response.json()

# Usage
result = transcribe_audio("audio.wav", "en-US")
print(result["DisplayText"])
```

## Audio Requirements

| Format | Codec | Sample Rate | Notes |
|--------|-------|-------------|-------|
| WAV | PCM | 16 kHz, mono | **Recommended** |
| OGG | OPUS | 16 kHz, mono | Smaller file size |

**Limitations:**
- Maximum 60 seconds of audio
- For pronunciation assessment: maximum 30 seconds
- No partial/interim results (final only)

## Content-Type Headers

```python
# WAV PCM 16kHz
"Content-Type": "audio/wav; codecs=audio/pcm; samplerate=16000"

# OGG OPUS
"Content-Type": "audio/ogg; codecs=opus"
```

## Response Formats

### Simple Format (default)

```python
params = {"language": "en-US", "format": "simple"}
```

```json
{
  "RecognitionStatus": "Success",
  "DisplayText": "Remind me to buy 5 pencils.",
  "Offset": "1236645672289",
  "Duration": "1236645672289"
}
```

### Detailed Format

```python
params = {"language": "en-US", "format": "detailed"}
```

```json
{
  "RecognitionStatus": "Success",
  "Offset": "1236645672289",
  "D

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Simple REST API for speech-to-text transcription of short audio files (up to 60 seconds). No SDK required - just HTTP requests.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Speech to Text REST API for Short Audio
- Para tarefas relacionadas a azure speech to text rest api for short audio

## Diretrizes Específicas

