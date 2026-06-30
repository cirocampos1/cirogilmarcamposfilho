---
name: gemini-api-integration
description: This skill guides AI agents through integrating Google Gemini API into applications — from basic text generation to advanced multimodal, function calling, and streaming use cases. It covers the full G
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Gemini API Integration

## Backstory

Você é um agente especializado em Gemini API Integration.

## Contexto Original da Skill
Gemini API Integration

## Instruções
---
name: gemini-api-integration
description: "Use when integrating Google Gemini API into projects. Covers model selection, multimodal inputs, streaming, function calling, and production best practices."
risk: safe
source: community
date_added: "2026-03-04"
---

# Gemini API Integration

## Overview

This skill guides AI agents through integrating Google Gemini API into applications — from basic text generation to advanced multimodal, function calling, and streaming use cases. It covers the full Gemini SDK lifecycle with production-grade patterns.

## When to Use This Skill

- Use when setting up Gemini API for the first time in a Node.js, Python, or browser project
- Use when implementing multimodal inputs (text + image/audio/video)
- Use when adding streaming responses to improve perceived latency
- Use when implementing function calling / tool use with Gemini
- Use when optimizing model selection (Flash vs Pro vs Ultra) for cost and performance
- Use when debugging Gemini API errors, rate limits, or quota issues

## Step-by-Step Guide

### 1. Installation & Setup

**Node.js / TypeScript:**
```bash
npm install @google/generative-ai
```

**Python:**
```bash
pip install google-generativeai
```

Set your API key securely:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

### 2. Basic Text Generation

**Node.js:**
```javascript
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

const result = await model.generateContent("Explain async/await in JavaScript");
console.log(result.response.text());
```

**Python:**
```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Explain async/await in JavaScript")
print(response.text)
```

### 3. Streaming Responses

```javascript
const result = await model.generateContentStream("Write a detailed blog post about AI");

for await (const chunk of result.stream) {
  process.stdout.write(chunk.text());
}
```

### 4. Multimodal Input (Text + Image)

```javascript
import fs from "fs";

const imageData = fs.readFileSync("screenshot.png");
const imagePart = {
  inlineData: {
    data: imageData.toString("base64"),
    mimeType: "image/png",
  },
};

const result = await model.generateContent(["Describe this image:", imagePart]);
console.log(result.response.text());
```

### 5. Function Calling / Tool Use

```javascript
const tools = [{
  functionDeclarations: [{
    name: "get_weather",
    description: "Get current weather for a city",
    parameters: {
      type: "OBJECT",
      properties: {
        city: { type: "STRING", description: "City name" },
      },
      required: ["city"],
    },
  }],
}];

const model = genAI.getGenerativeModel({ model: "gemini-1.5-pro", tools });
const result = await model.generateContent("What's

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

This skill guides AI agents through integrating Google Gemini API into applications — from basic text generation to advanced multimodal, function calling, and streaming use cases. It covers the full G

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Gemini API Integration
- Para tarefas relacionadas a gemini api integration

## Diretrizes Específicas

