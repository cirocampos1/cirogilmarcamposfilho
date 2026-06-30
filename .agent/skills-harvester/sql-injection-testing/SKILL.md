---
name: sql-injection-testing
description: > AUTHORIZED USE ONLY: Use this skill only for authorized security assessments, defensive validation, or controlled educational environments.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# SQL Injection Testing

## Backstory

Você é um agente especializado em SQL Injection Testing.

## Contexto Original da Skill
SQL Injection Testing

## Instruções
---
name: sql-injection-testing
description: "Execute comprehensive SQL injection vulnerability assessments on web applications to identify database security flaws, demonstrate exploitation techniques, and validate input sanitization mechanisms."
risk: offensive
source: community
author: zebbern
date_added: "2026-02-27"
---

> AUTHORIZED USE ONLY: Use this skill only for authorized security assessments, defensive validation, or controlled educational environments.

# SQL Injection Testing

## Purpose

Execute comprehensive SQL injection vulnerability assessments on web applications to identify database security flaws, demonstrate exploitation techniques, and validate input sanitization mechanisms. This skill enables systematic detection and exploitation of SQL injection vulnerabilities across in-band, blind, and out-of-band attack vectors to assess application security posture.

## Inputs / Prerequisites

### Required Access
- Target web application URL with injectable parameters
- Burp Suite or equivalent proxy tool for request manipulation
- SQLMap installation for automated exploitation
- Browser with developer tools enabled

### Technical Requirements
- Understanding of SQL query syntax (MySQL, MSSQL, PostgreSQL, Oracle)
- Knowledge of HTTP request/response cycle
- Familiarity with database schemas and structures
- Write permissions for testing reports

### Legal Prerequisites
- Written authorization for penetration testing
- Defined scope including target URLs and parameters
- Emergency contact procedures established
- Data handling agreements in place

## Outputs / Deliverables

### Primary Outputs
- SQL injection vulnerability report with severity ratings
- Extracted database schemas and table structures
- Authentication bypass proof-of-concept demonstrations
- Remediation recommendations with code examples

### Evidence Artifacts
- Screenshots of successful injections
- HTTP request/response logs
- Database dumps (sanitized)
- Payload documentation

## Core Workflow

### Phase 1: Detection and Reconnaissance

#### Identify Injectable Parameters
Locate user-controlled input fields that interact with database queries:

```
# Common injection points
- URL parameters: ?id=1, ?user=admin, ?category=books
- Form fields: username, password, search, comments
- Cookie values: session_id, user_preference
- HTTP headers: User-Agent, Referer, X-Forwarded-For
```

#### Test for Basic Vulnerability Indicators
Insert special characters to trigger error responses:

```sql
-- Single quote test
'

-- Double quote test
"

-- Comment sequences
--
#
/**/

-- Semicolon for query stacking
;

-- Parentheses
)
```

Monitor application responses for:
- Database error messages revealing query structure
- Unexpected application behavior changes
- HTTP 500 Internal Server errors
- Modified response content or length

#### Logic Testing Payloads
Verify boolean-based vulnerability presence:

```sql
-- True condition tests
page.asp?id=1 or 1=1
page.asp?id=1' or 1=1--
pa

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

> AUTHORIZED USE ONLY: Use this skill only for authorized security assessments, defensive validation, or controlled educational environments.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em SQL Injection Testing
- Para tarefas relacionadas a sql injection testing

## Diretrizes Específicas

