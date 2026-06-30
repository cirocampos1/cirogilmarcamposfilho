---
name: distributed-tracing
description: Implement distributed tracing with Jaeger and Tempo for request flow visibility across microservices.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Distributed Tracing

## Backstory

Você é um agente especializado em Distributed Tracing.

## Contexto Original da Skill
Distributed Tracing

## Instruções
---
name: distributed-tracing
description: "Implement distributed tracing with Jaeger and Tempo for request flow visibility across microservices."
risk: critical
source: community
date_added: "2026-02-27"
---

# Distributed Tracing

Implement distributed tracing with Jaeger and Tempo for request flow visibility across microservices.

## Do not use this skill when

- The task is unrelated to distributed tracing
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Track requests across distributed systems to understand latency, dependencies, and failure points.

## Use this skill when

- Debug latency issues
- Understand service dependencies
- Identify bottlenecks
- Trace error propagation
- Analyze request paths

## Distributed Tracing Concepts

### Trace Structure
```
Trace (Request ID: abc123)
  ↓
Span (frontend) [100ms]
  ↓
Span (api-gateway) [80ms]
  ├→ Span (auth-service) [10ms]
  └→ Span (user-service) [60ms]
      └→ Span (database) [40ms]
```

### Key Components
- **Trace** - End-to-end request journey
- **Span** - Single operation within a trace
- **Context** - Metadata propagated between services
- **Tags** - Key-value pairs for filtering
- **Logs** - Timestamped events within a span

## Jaeger Setup

### Kubernetes Deployment

```bash
# Deploy Jaeger Operator
kubectl create namespace observability
kubectl create -f https://github.com/jaegertracing/jaeger-operator/releases/download/v1.51.0/jaeger-operator.yaml -n observability

# Deploy Jaeger instance
kubectl apply -f - <<EOF
apiVersion: jaegertracing.io/v1
kind: Jaeger
metadata:
  name: jaeger
  namespace: observability
spec:
  strategy: production
  storage:
    type: elasticsearch
    options:
      es:
        server-urls: http://elasticsearch:9200
  ingress:
    enabled: true
EOF
```

### Docker Compose

```yaml
version: '3.8'
services:
  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - "5775:5775/udp"
      - "6831:6831/udp"
      - "6832:6832/udp"
      - "5778:5778"
      - "16686:16686"  # UI
      - "14268:14268"  # Collector
      - "14250:14250"  # gRPC
      - "9411:9411"    # Zipkin
    environment:
      - COLLECTOR_ZIPKIN_HOST_PORT=:9411
```

**Reference:** See `references/jaeger-setup.md`

## Application Instrumentation

### OpenTelemetry (Recommended)

#### Python (Flask)
```python
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from flask import Flask

# Initialize tracer
resource = Resource(attribut

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Implement distributed tracing with Jaeger and Tempo for request flow visibility across microservices.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Distributed Tracing
- Para tarefas relacionadas a distributed tracing

## Diretrizes Específicas

