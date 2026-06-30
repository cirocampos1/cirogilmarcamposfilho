---
name: red-team-tactics
description: > AUTHORIZED USE ONLY: Use this skill only for authorized security assessments, defensive validation, or controlled educational environments.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Red Team Tactics

## Backstory

Você é um agente especializado em Red Team Tactics.

## Contexto Original da Skill
Red Team Tactics

## Instruções
---
name: red-team-tactics
description: "Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting."
risk: offensive
source: community
date_added: "2026-02-27"
---

> AUTHORIZED USE ONLY: Use this skill only for authorized security assessments, defensive validation, or controlled educational environments.

# Red Team Tactics

> Adversary simulation principles based on MITRE ATT&CK framework.

---

## 1. MITRE ATT&CK Phases

### Attack Lifecycle

```
RECONNAISSANCE → INITIAL ACCESS → EXECUTION → PERSISTENCE
       ↓              ↓              ↓            ↓
   PRIVILEGE ESC → DEFENSE EVASION → CRED ACCESS → DISCOVERY
       ↓              ↓              ↓            ↓
LATERAL MOVEMENT → COLLECTION → C2 → EXFILTRATION → IMPACT
```

### Phase Objectives

| Phase | Objective |
|-------|-----------|
| **Recon** | Map attack surface |
| **Initial Access** | Get first foothold |
| **Execution** | Run code on target |
| **Persistence** | Survive reboots |
| **Privilege Escalation** | Get admin/root |
| **Defense Evasion** | Avoid detection |
| **Credential Access** | Harvest credentials |
| **Discovery** | Map internal network |
| **Lateral Movement** | Spread to other systems |
| **Collection** | Gather target data |
| **C2** | Maintain command channel |
| **Exfiltration** | Extract data |

---

## 2. Reconnaissance Principles

### Passive vs Active

| Type | Trade-off |
|------|-----------|
| **Passive** | No target contact, limited info |
| **Active** | Direct contact, more detection risk |

### Information Targets

| Category | Value |
|----------|-------|
| Technology stack | Attack vector selection |
| Employee info | Social engineering |
| Network ranges | Scanning scope |
| Third parties | Supply chain attack |

---

## 3. Initial Access Vectors

### Selection Criteria

| Vector | When to Use |
|--------|-------------|
| **Phishing** | Human target, email access |
| **Public exploits** | Vulnerable services exposed |
| **Valid credentials** | Leaked or cracked |
| **Supply chain** | Third-party access |

---

## 4. Privilege Escalation Principles

### Windows Targets

| Check | Opportunity |
|-------|-------------|
| Unquoted service paths | Write to path |
| Weak service permissions | Modify service |
| Token privileges | Abuse SeDebug, etc. |
| Stored credentials | Harvest |

### Linux Targets

| Check | Opportunity |
|-------|-------------|
| SUID binaries | Execute as owner |
| Sudo misconfiguration | Command execution |
| Kernel vulnerabilities | Kernel exploits |
| Cron jobs | Writable scripts |

---

## 5. Defense Evasion Principles

### Key Techniques

| Technique | Purpose |
|-----------|---------|
| LOLBins | Use legitimate tools |
| Obfuscation | Hide malicious code |
| Timestomping | Hide file modifications |
| Log clearing | Remove evidence |

### Operational Security

- Work during business hours
- Mimic legitimate traffic patterns
- Use encrypted channels
- Blend with normal behavior

---

## 6

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

> AUTHORIZED USE ONLY: Use this skill only for authorized security assessments, defensive validation, or controlled educational environments.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Red Team Tactics
- Para tarefas relacionadas a red team tactics

## Diretrizes Específicas

