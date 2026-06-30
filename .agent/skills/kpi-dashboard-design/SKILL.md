---
name: kpi-dashboard-design
description: Comprehensive patterns for designing effective Key Performance Indicator (KPI) dashboards that drive business decisions.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# KPI Dashboard Design

## Backstory

Você é um agente especializado em KPI Dashboard Design.

## Contexto Original da Skill
KPI Dashboard Design

## Instruções
---
name: kpi-dashboard-design
description: "Comprehensive patterns for designing effective Key Performance Indicator (KPI) dashboards that drive business decisions."
risk: unknown
source: community
date_added: "2026-02-27"
---

# KPI Dashboard Design

Comprehensive patterns for designing effective Key Performance Indicator (KPI) dashboards that drive business decisions.

## Do not use this skill when

- The task is unrelated to kpi dashboard design
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Designing executive dashboards
- Selecting meaningful KPIs
- Building real-time monitoring displays
- Creating department-specific metrics views
- Improving existing dashboard layouts
- Establishing metric governance

## Core Concepts

### 1. KPI Framework

| Level           | Focus            | Update Frequency  | Audience   |
| --------------- | ---------------- | ----------------- | ---------- |
| **Strategic**   | Long-term goals  | Monthly/Quarterly | Executives |
| **Tactical**    | Department goals | Weekly/Monthly    | Managers   |
| **Operational** | Day-to-day       | Real-time/Daily   | Teams      |

### 2. SMART KPIs

```
Specific: Clear definition
Measurable: Quantifiable
Achievable: Realistic targets
Relevant: Aligned to goals
Time-bound: Defined period
```

### 3. Dashboard Hierarchy

```
├── Executive Summary (1 page)
│   ├── 4-6 headline KPIs
│   ├── Trend indicators
│   └── Key alerts
├── Department Views
│   ├── Sales Dashboard
│   ├── Marketing Dashboard
│   ├── Operations Dashboard
│   └── Finance Dashboard
└── Detailed Drilldowns
    ├── Individual metrics
    └── Root cause analysis
```

## Common KPIs by Department

### Sales KPIs

```yaml
Revenue Metrics:
  - Monthly Recurring Revenue (MRR)
  - Annual Recurring Revenue (ARR)
  - Average Revenue Per User (ARPU)
  - Revenue Growth Rate

Pipeline Metrics:
  - Sales Pipeline Value
  - Win Rate
  - Average Deal Size
  - Sales Cycle Length

Activity Metrics:
  - Calls/Emails per Rep
  - Demos Scheduled
  - Proposals Sent
  - Close Rate
```

### Marketing KPIs

```yaml
Acquisition:
  - Cost Per Acquisition (CPA)
  - Customer Acquisition Cost (CAC)
  - Lead Volume
  - Marketing Qualified Leads (MQL)

Engagement:
  - Website Traffic
  - Conversion Rate
  - Email Open/Click Rate
  - Social Engagement

ROI:
  - Marketing ROI
  - Campaign Performance
  - Channel Attribution
  - CAC Payback Period
```

### Product KPIs

```yaml
Usage:
  - Daily/Monthly Active Users (DAU/MAU)
  - Session Duration
  - Feature Adoption Rate
  - Stickiness (DAU/MAU)

Quality:
  - Net Promoter Score (NPS)
  - Customer Satisfaction (CSAT)
  - Bug/Issue Count
  - Time to Resolution

Growth:
  - User Growth Rate
  - Activation Rate
  -

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Comprehensive patterns for designing effective Key Performance Indicator (KPI) dashboards that drive business decisions.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em KPI Dashboard Design
- Para tarefas relacionadas a kpi dashboard design

## Diretrizes Específicas

