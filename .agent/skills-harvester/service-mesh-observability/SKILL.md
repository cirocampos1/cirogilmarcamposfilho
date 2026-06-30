---
name: service-mesh-observability
description: Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Service Mesh Observability

## Backstory

Você é um agente especializado em Service Mesh Observability.

## Contexto Original da Skill
Service Mesh Observability

## Instruções
---
name: service-mesh-observability
description: "Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments."
risk: critical
source: community
date_added: "2026-02-27"
---

# Service Mesh Observability

Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments.

## Do not use this skill when

- The task is unrelated to service mesh observability
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Setting up distributed tracing across services
- Implementing service mesh metrics and dashboards
- Debugging latency and error issues
- Defining SLOs for service communication
- Visualizing service dependencies
- Troubleshooting mesh connectivity

## Core Concepts

### 1. Three Pillars of Observability

```
┌─────────────────────────────────────────────────────┐
│                  Observability                       │
├─────────────────┬─────────────────┬─────────────────┤
│     Metrics     │     Traces      │      Logs       │
│                 │                 │                 │
│ • Request rate  │ • Span context  │ • Access logs   │
│ • Error rate    │ • Latency       │ • Error details │
│ • Latency P50   │ • Dependencies  │ • Debug info    │
│ • Saturation    │ • Bottlenecks   │ • Audit trail   │
└─────────────────┴─────────────────┴─────────────────┘
```

### 2. Golden Signals for Mesh

| Signal | Description | Alert Threshold |
|--------|-------------|-----------------|
| **Latency** | Request duration P50, P99 | P99 > 500ms |
| **Traffic** | Requests per second | Anomaly detection |
| **Errors** | 5xx error rate | > 1% |
| **Saturation** | Resource utilization | > 80% |

## Templates

### Template 1: Istio with Prometheus & Grafana

```yaml
# Install Prometheus
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus
  namespace: istio-system
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
    scrape_configs:
      - job_name: 'istio-mesh'
        kubernetes_sd_configs:
          - role: endpoints
            namespaces:
              names:
                - istio-system
        relabel_configs:
          - source_labels: [__meta_kubernetes_service_name]
            action: keep
            regex: istio-telemetry
---
# ServiceMonitor for Prometheus Operator
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: istio-mesh
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istiod
  endpoints:
    - port: http-monitoring
      interval: 15s
```

### Template 2: Key Istio Metrics Queries

```promql
# Request rate by service
sum(rate(istio_requests_total{reporter="destination"}[5m])) by (destination_service_name)

# Error rate (5xx)
sum(rate(ist

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Service Mesh Observability
- Para tarefas relacionadas a service mesh observability

## Diretrizes Específicas

