---
name: earllm-one-build-maintain
description: Build, maintain, and extend the EarLLM One Android project — a Kotlin/Compose app that connects Bluetooth earbuds to an LLM via voice pipeline.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# EarLLM One — Build & Maintain

## Backstory

Você é um agente especializado em EarLLM One — Build & Maintain.

## Contexto Original da Skill
EarLLM One — Build & Maintain

## Instruções
---
name: earllm-build
description: "Build, maintain, and extend the EarLLM One Android project — a Kotlin/Compose app that connects Bluetooth earbuds to an LLM via voice pipeline."
risk: safe
source: community
date_added: '2026-03-06'
author: renat
tags:
- android
- kotlin
- bluetooth
- llm
- voice
tools:
- claude-code
- antigravity
- cursor
- gemini-cli
- codex-cli
---

# EarLLM One — Build & Maintain

## Overview

Build, maintain, and extend the EarLLM One Android project — a Kotlin/Compose app that connects Bluetooth earbuds to an LLM via voice pipeline.

## When to Use This Skill

- When the user mentions "earllm" or related topics
- When the user mentions "earbudllm" or related topics
- When the user mentions "earbud app" or related topics
- When the user mentions "voice pipeline kotlin" or related topics
- When the user mentions "bluetooth audio android" or related topics
- When the user mentions "sco microphone" or related topics

## Do Not Use This Skill When

- The task is unrelated to earllm build
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

EarLLM One is a multi-module Android app (Kotlin + Jetpack Compose) that captures voice from Bluetooth earbuds, transcribes it, sends it to an LLM, and speaks the response back.

## Project Location

`C:\Users\renat\earbudllm`

## Module Dependency Graph

```
app ──→ voice ──→ audio ──→ core-logging
  │       │
  ├──→ bluetooth ──→ core-logging
  └──→ llm ──→ core-logging
```

## Modules And Key Files

| Module | Purpose | Key Files |
|--------|---------|-----------|
| **core-logging** | Structured logging, performance tracking | `EarLogger.kt`, `PerformanceTracker.kt` |
| **bluetooth** | BT discovery, pairing, A2DP/HFP profiles | `BluetoothController.kt`, `BluetoothState.kt`, `BluetoothPermissions.kt` |
| **audio** | Audio routing (SCO/BLE), capture, headset buttons | `AudioRouteController.kt`, `VoiceCaptureController.kt`, `HeadsetButtonController.kt` |
| **voice** | STT (SpeechRecognizer + Vosk stub), TTS, pipeline | `SpeechToTextController.kt`, `TextToSpeechController.kt`, `VoicePipeline.kt` |
| **llm** | LLM interface, stub, OpenAI-compatible client | `LlmClient.kt`, `StubLlmClient.kt`, `RealLlmClient.kt`, `SecureTokenStore.kt` |
| **app** | UI, ViewModel, Service, Settings, all screens | `MainViewModel.kt`, `EarLlmForegroundService.kt`, 6 Compose screens |

## Build Configuration

- **SDK**: minSdk 26, targetSdk 34, compileSdk 34
- **Build tools**: AGP 8.2.2, Kotlin 1.9.22, Gradle 8.5
- **Compose BOM**: 2024.02.00
- **Key deps**: OkHttp, AndroidX Security (EncryptedSharedPreferences), DataStore, Media

## Target Hardware

| Device | Model | Key Details |
|--------|-------|-------------|
| Phone | Samsung Galaxy S24 Ultra | Android 14, One UI 6.1, Snapdragon 8 Gen 3 |
| Earbuds | Xiaomi Redmi Buds 6 Pro | BT 5.3, A2DP/HFP/AVRCP, ANC, LDAC |

## Critical Technical Facts

These are verified facts from

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Build, maintain, and extend the EarLLM One Android project — a Kotlin/Compose app that connects Bluetooth earbuds to an LLM via voice pipeline.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em EarLLM One — Build & Maintain
- Para tarefas relacionadas a earllm one build maintain

## Diretrizes Específicas

