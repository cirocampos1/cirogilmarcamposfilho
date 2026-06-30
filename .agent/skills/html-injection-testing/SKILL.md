---
name: html-injection-testing
description: > AUTHORIZED USE ONLY: Use this skill only for authorized security assessments, defensive validation, or controlled educational environments.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# HTML Injection Testing

## Backstory

Você é um agente especializado em HTML Injection Testing.

## Contexto Original da Skill
HTML Injection Testing

## Instruções
---
name: html-injection-testing
description: "Identify and exploit HTML injection vulnerabilities that allow attackers to inject malicious HTML content into web applications. This vulnerability enables attackers to modify page appearance, create phishing pages, and steal user credentials through injected forms."
risk: offensive
source: community
author: zebbern
date_added: "2026-02-27"
---

> AUTHORIZED USE ONLY: Use this skill only for authorized security assessments, defensive validation, or controlled educational environments.

# HTML Injection Testing

## Purpose

Identify and exploit HTML injection vulnerabilities that allow attackers to inject malicious HTML content into web applications. This vulnerability enables attackers to modify page appearance, create phishing pages, and steal user credentials through injected forms.

## Prerequisites

### Required Tools
- Web browser with developer tools
- Burp Suite or OWASP ZAP
- Tamper Data or similar proxy
- cURL for testing payloads

### Required Knowledge
- HTML fundamentals
- HTTP request/response structure
- Web application input handling
- Difference between HTML injection and XSS

## Outputs and Deliverables

1. **Vulnerability Report** - Identified injection points
2. **Exploitation Proof** - Demonstrated content manipulation
3. **Impact Assessment** - Potential phishing and defacement risks
4. **Remediation Guidance** - Input validation recommendations

## Core Workflow

### Phase 1: Understanding HTML Injection

HTML injection occurs when user input is reflected in web pages without proper sanitization:

```html
<!-- Vulnerable code example -->
<div>
    Welcome, <?php echo $_GET['name']; ?>
</div>

<!-- Attack input -->
?name=<h1>Injected Content</h1>

<!-- Rendered output -->
<div>
    Welcome, <h1>Injected Content</h1>
</div>
```

Key differences from XSS:
- HTML injection: Only HTML tags are rendered
- XSS: JavaScript code is executed
- HTML injection is often stepping stone to XSS

Attack goals:
- Modify website appearance (defacement)
- Create fake login forms (phishing)
- Inject malicious links
- Display misleading content

### Phase 2: Identifying Injection Points

Map application for potential injection surfaces:

```
1. Search bars and search results
2. Comment sections
3. User profile fields
4. Contact forms and feedback
5. Registration forms
6. URL parameters reflected on page
7. Error messages
8. Page titles and headers
9. Hidden form fields
10. Cookie values reflected on page
```

Common vulnerable parameters:
```
?name=
?user=
?search=
?query=
?message=
?title=
?content=
?redirect=
?url=
?page=
```

### Phase 3: Basic HTML Injection Testing

Test with simple HTML tags:

```html
<!-- Basic text formatting -->
<h1>Test Injection</h1>
<b>Bold Text</b>
<i>Italic Text</i>
<u>Underlined Text</u>
<font color="red">Red Text</font>

<!-- Structural elements -->
<div style="background:red;color:white;padding:10px">Injected DIV</div>
<p>Injected paragraph</p>
<br><br><br>Line break

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

> AUTHORIZED USE ONLY: Use this skill only for authorized security assessments, defensive validation, or controlled educational environments.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em HTML Injection Testing
- Para tarefas relacionadas a html injection testing

## Diretrizes Específicas

