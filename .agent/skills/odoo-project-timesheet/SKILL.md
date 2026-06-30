---
name: odoo-project-timesheet
description: This skill helps you configure Odoo Project and Timesheets for service businesses, agencies, and consulting firms. It covers project setup with budgets, task stage management, employee timesheet loggi
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Odoo Project & Timesheet

## Backstory

Você é um agente especializado em Odoo Project & Timesheet.

## Contexto Original da Skill
Odoo Project & Timesheet

## Instruções
---
name: odoo-project-timesheet
description: "Expert guide for Odoo Project and Timesheets: task stages, billable time tracking, timesheet approval, budget alerts, and invoicing from timesheets."
risk: safe
source: "self"
---

# Odoo Project & Timesheet

## Overview

This skill helps you configure Odoo Project and Timesheets for service businesses, agencies, and consulting firms. It covers project setup with budgets, task stage management, employee timesheet logging, approval workflows, and converting approved timesheet hours to customer invoices.

## When to Use This Skill

- Setting up a new project with tasks, deadlines, and team assignments.
- Configuring billable vs. non-billable time tracking per project.
- Creating a timesheet approval workflow for managers.
- Invoicing customers based on logged hours (Time & Materials billing).

## How It Works

1. **Activate**: Mention `@odoo-project-timesheet` and describe your project or billing scenario.
2. **Configure**: Receive step-by-step setup instructions.
3. **Automate**: Get guidance on automatically generating invoices from approved timesheets.

## Examples

### Example 1: Create a Billable Project

```text
Menu: Project → New Project (or the "+" button in Project view)

Name:     Website Redesign — Acme Corp
Customer: Acme Corporation
Billable: YES  (toggle ON)

Settings tab:
  Billing Type: Based on Timesheets (Time & Materials)
  Service Product: Consulting Hours ($150/hr)
  ☑ Timesheets
  ☑ Task Dependencies
  ☑ Subtasks

Budget:
  Planned Hours: 120 hours
  Budget Alert: at 80% (96 hrs) → notify project manager
```

### Example 2: Log Time on a Task

```text
Method A — Directly inside the Task (recommended for accuracy):
  Open Task → Timesheets tab → Add a Line
  Employee:    John Doe
  Date:        Today
  Description: "Initial wireframes and site map" (required for clear invoices)
  Duration:    3:30  (3 hours 30 minutes)

Method B — Timesheets app (for end-of-day bulk entry):
  Menu: Timesheets → My Timesheets → New
  Project:  Website Redesign
  Task:     Wireframe Design
  Duration: 3:30
```

### Example 3: Enable Timesheet Approval Before Invoicing

```text
Menu: Timesheets → Configuration → Settings
  ☑ Timesheet Approval  (employees submit; managers approve)

Approval flow:
  1. Employee submits timesheet at week/month end
  2. Manager reviews: Timesheets → Managers → Timesheets to Approve
  3. Manager clicks "Approve" → entries are locked and billable
  4. Only approved entries flow into the invoice

If Approval is disabled, all logged hours are immediately billable.
```

### Example 4: Invoice from Timesheets

```text
Step 1: Verify approved hours
  Menu: Timesheets → Managers → All Timesheets
  Filter: Billable = YES, Timesheet Invoice State = "To Invoice"

Step 2: Generate Invoice
  Menu: Sales → Orders → To Invoice → Timesheets  (v15/v16)
  or:   Accounting → Customers → Invoiceable Time  (v17)
  Filter by Customer: Acme Corporation
  Select entries → Create Invoices

Step

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

This skill helps you configure Odoo Project and Timesheets for service businesses, agencies, and consulting firms. It covers project setup with budgets, task stage management, employee timesheet loggi

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Odoo Project & Timesheet
- Para tarefas relacionadas a odoo project timesheet

## Diretrizes Específicas

