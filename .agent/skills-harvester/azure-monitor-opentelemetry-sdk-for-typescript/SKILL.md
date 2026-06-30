---
name: azure-monitor-opentelemetry-sdk-for-typescript
description: Auto-instrument Node.js applications with distributed tracing, metrics, and logs.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Monitor OpenTelemetry SDK for TypeScript

## Backstory

Você é um agente especializado em Azure Monitor OpenTelemetry SDK for TypeScript.

## Contexto Original da Skill
Azure Monitor OpenTelemetry SDK for TypeScript

## Instruções
---
name: azure-monitor-opentelemetry-ts
description: "Auto-instrument Node.js applications with distributed tracing, metrics, and logs."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure Monitor OpenTelemetry SDK for TypeScript

Auto-instrument Node.js applications with distributed tracing, metrics, and logs.

## Installation

```bash
# Distro (recommended - auto-instrumentation)
npm install @azure/monitor-opentelemetry

# Low-level exporters (custom OpenTelemetry setup)
npm install @azure/monitor-opentelemetry-exporter

# Custom logs ingestion
npm install @azure/monitor-ingestion
```

## Environment Variables

```bash
APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=...;IngestionEndpoint=...
```

## Quick Start (Auto-Instrumentation)

**IMPORTANT:** Call `useAzureMonitor()` BEFORE importing other modules.

```typescript
import { useAzureMonitor } from "@azure/monitor-opentelemetry";

useAzureMonitor({
  azureMonitorExporterOptions: {
    connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING
  }
});

// Now import your application
import express from "express";
const app = express();
```

## ESM Support (Node.js 18.19+)

```bash
node --import @azure/monitor-opentelemetry/loader ./dist/index.js
```

**package.json:**
```json
{
  "scripts": {
    "start": "node --import @azure/monitor-opentelemetry/loader ./dist/index.js"
  }
}
```

## Full Configuration

```typescript
import { useAzureMonitor, AzureMonitorOpenTelemetryOptions } from "@azure/monitor-opentelemetry";
import { resourceFromAttributes } from "@opentelemetry/resources";

const options: AzureMonitorOpenTelemetryOptions = {
  azureMonitorExporterOptions: {
    connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING,
    storageDirectory: "/path/to/offline/storage",
    disableOfflineStorage: false
  },
  
  // Sampling
  samplingRatio: 1.0,  // 0-1, percentage of traces
  
  // Features
  enableLiveMetrics: true,
  enableStandardMetrics: true,
  enablePerformanceCounters: true,
  
  // Instrumentation libraries
  instrumentationOptions: {
    azureSdk: { enabled: true },
    http: { enabled: true },
    mongoDb: { enabled: true },
    mySql: { enabled: true },
    postgreSql: { enabled: true },
    redis: { enabled: true },
    bunyan: { enabled: false },
    winston: { enabled: false }
  },
  
  // Custom resource
  resource: resourceFromAttributes({ "service.name": "my-service" })
};

useAzureMonitor(options);
```

## Custom Traces

```typescript
import { trace } from "@opentelemetry/api";

const tracer = trace.getTracer("my-tracer");

const span = tracer.startSpan("doWork");
try {
  span.setAttribute("component", "worker");
  span.setAttribute("operation.id", "42");
  span.addEvent("processing started");
  
  // Your work here
  
} catch (error) {
  span.recordException(error as Error);
  span.setStatus({ code: 2, message: (error as Error).message });
} finally {
  span.end();
}
```

## Custom Metrics

```typescript
import { metrics

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Auto-instrument Node.js applications with distributed tracing, metrics, and logs.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Monitor OpenTelemetry SDK for TypeScript
- Para tarefas relacionadas a azure monitor opentelemetry sdk for typescript

## Diretrizes Específicas

