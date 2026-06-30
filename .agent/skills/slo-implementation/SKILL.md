---
name: slo-implementation
description: Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# SLO Implementation

## Backstory

Você é um agente especializado em SLO Implementation.

## Contexto Original da Skill
SLO Implementation

## Instruções
---
name: slo-implementation
description: "Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets."
risk: unknown
source: community
date_added: "2026-02-27"
---

# SLO Implementation

Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets.

## Do not use this skill when

- The task is unrelated to slo implementation
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Implement measurable reliability targets using SLIs, SLOs, and error budgets to balance reliability with innovation velocity.

## Use this skill when

- Define service reliability targets
- Measure user-perceived reliability
- Implement error budgets
- Create SLO-based alerts
- Track reliability goals

## SLI/SLO/SLA Hierarchy

```
SLA (Service Level Agreement)
  ↓ Contract with customers
SLO (Service Level Objective)
  ↓ Internal reliability target
SLI (Service Level Indicator)
  ↓ Actual measurement
```

## Defining SLIs

### Common SLI Types

#### 1. Availability SLI
```promql
# Successful requests / Total requests
sum(rate(http_requests_total{status!~"5.."}[28d]))
/
sum(rate(http_requests_total[28d]))
```

#### 2. Latency SLI
```promql
# Requests below latency threshold / Total requests
sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))
/
sum(rate(http_request_duration_seconds_count[28d]))
```

#### 3. Durability SLI
```
# Successful writes / Total writes
sum(storage_writes_successful_total)
/
sum(storage_writes_total)
```

**Reference:** See `references/slo-definitions.md`

## Setting SLO Targets

### Availability SLO Examples

| SLO % | Downtime/Month | Downtime/Year |
|-------|----------------|---------------|
| 99%   | 7.2 hours      | 3.65 days     |
| 99.9% | 43.2 minutes   | 8.76 hours    |
| 99.95%| 21.6 minutes   | 4.38 hours    |
| 99.99%| 4.32 minutes   | 52.56 minutes |

### Choose Appropriate SLOs

**Consider:**
- User expectations
- Business requirements
- Current performance
- Cost of reliability
- Competitor benchmarks

**Example SLOs:**
```yaml
slos:
  - name: api_availability
    target: 99.9
    window: 28d
    sli: |
      sum(rate(http_requests_total{status!~"5.."}[28d]))
      /
      sum(rate(http_requests_total[28d]))

  - name: api_latency_p95
    target: 99
    window: 28d
    sli: |
      sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))
      /
      sum(rate(http_request_duration_seconds_count[28d]))
```

## Error Budget Calculation

### Error Budget Formula

```
Error Budget = 1 - SLO Target
```

**Example:**
- SLO: 99.9% availability
- Error Budget: 0.1% = 43.2 minutes/month
- Current Error: 0.05% = 21.6 minutes/month
- Remai

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em SLO Implementation
- Para tarefas relacionadas a slo implementation

## Diretrizes Específicas

