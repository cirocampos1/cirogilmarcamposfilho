---
name: azure-document-intelligence-rest-sdk-for-typescrip
description: Extract text, tables, and structured data from documents using prebuilt and custom models.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Document Intelligence REST SDK for TypeScript

## Backstory

Você é um agente especializado em Azure Document Intelligence REST SDK for TypeScript.

## Contexto Original da Skill
Azure Document Intelligence REST SDK for TypeScript

## Instruções
---
name: azure-ai-document-intelligence-ts
description: "Extract text, tables, and structured data from documents using prebuilt and custom models."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure Document Intelligence REST SDK for TypeScript

Extract text, tables, and structured data from documents using prebuilt and custom models.

## Installation

```bash
npm install @azure-rest/ai-document-intelligence @azure/identity
```

## Environment Variables

```bash
DOCUMENT_INTELLIGENCE_ENDPOINT=https://<resource>.cognitiveservices.azure.com
DOCUMENT_INTELLIGENCE_API_KEY=<api-key>
```

## Authentication

**Important**: This is a REST client. `DocumentIntelligence` is a **function**, not a class.

### DefaultAzureCredential

```typescript
import DocumentIntelligence from "@azure-rest/ai-document-intelligence";
import { DefaultAzureCredential } from "@azure/identity";

const client = DocumentIntelligence(
  process.env.DOCUMENT_INTELLIGENCE_ENDPOINT!,
  new DefaultAzureCredential()
);
```

### API Key

```typescript
import DocumentIntelligence from "@azure-rest/ai-document-intelligence";

const client = DocumentIntelligence(
  process.env.DOCUMENT_INTELLIGENCE_ENDPOINT!,
  { key: process.env.DOCUMENT_INTELLIGENCE_API_KEY! }
);
```

## Analyze Document (URL)

```typescript
import DocumentIntelligence, {
  isUnexpected,
  getLongRunningPoller,
  AnalyzeOperationOutput
} from "@azure-rest/ai-document-intelligence";

const initialResponse = await client
  .path("/documentModels/{modelId}:analyze", "prebuilt-layout")
  .post({
    contentType: "application/json",
    body: {
      urlSource: "https://example.com/document.pdf"
    },
    queryParameters: { locale: "en-US" }
  });

if (isUnexpected(initialResponse)) {
  throw initialResponse.body.error;
}

const poller = getLongRunningPoller(client, initialResponse);
const result = (await poller.pollUntilDone()).body as AnalyzeOperationOutput;

console.log("Pages:", result.analyzeResult?.pages?.length);
console.log("Tables:", result.analyzeResult?.tables?.length);
```

## Analyze Document (Local File)

```typescript
import { readFile } from "node:fs/promises";

const fileBuffer = await readFile("./document.pdf");
const base64Source = fileBuffer.toString("base64");

const initialResponse = await client
  .path("/documentModels/{modelId}:analyze", "prebuilt-invoice")
  .post({
    contentType: "application/json",
    body: { base64Source }
  });

if (isUnexpected(initialResponse)) {
  throw initialResponse.body.error;
}

const poller = getLongRunningPoller(client, initialResponse);
const result = (await poller.pollUntilDone()).body as AnalyzeOperationOutput;
```

## Prebuilt Models

| Model ID | Description |
|----------|-------------|
| `prebuilt-read` | OCR - text and language extraction |
| `prebuilt-layout` | Text, tables, selection marks, structure |
| `prebuilt-invoice` | Invoice fields |
| `prebuilt-receipt` | Receipt fields |
| `prebuilt-idDocument` | ID document fields |
| `prebui

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Extract text, tables, and structured data from documents using prebuilt and custom models.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Document Intelligence REST SDK for TypeScript
- Para tarefas relacionadas a azure document intelligence rest sdk for typescrip

## Diretrizes Específicas

