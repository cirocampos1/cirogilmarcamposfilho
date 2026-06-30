---
name: kubernetes-security-policies
description: Comprehensive guide for implementing NetworkPolicy, PodSecurityPolicy, RBAC, and Pod Security Standards in Kubernetes.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Kubernetes Security Policies

## Backstory

Você é um agente especializado em Kubernetes Security Policies.

## Contexto Original da Skill
Kubernetes Security Policies

## Instruções
---
name: k8s-security-policies
description: "Comprehensive guide for implementing NetworkPolicy, PodSecurityPolicy, RBAC, and Pod Security Standards in Kubernetes."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Kubernetes Security Policies

Comprehensive guide for implementing NetworkPolicy, PodSecurityPolicy, RBAC, and Pod Security Standards in Kubernetes.

## Do not use this skill when

- The task is unrelated to kubernetes security policies
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Implement defense-in-depth security for Kubernetes clusters using network policies, pod security standards, and RBAC.

## Use this skill when

- Implement network segmentation
- Configure pod security standards
- Set up RBAC for least-privilege access
- Create security policies for compliance
- Implement admission control
- Secure multi-tenant clusters

## Pod Security Standards

### 1. Privileged (Unrestricted)
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: privileged-ns
  labels:
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/warn: privileged
```

### 2. Baseline (Minimally restrictive)
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: baseline-ns
  labels:
    pod-security.kubernetes.io/enforce: baseline
    pod-security.kubernetes.io/audit: baseline
    pod-security.kubernetes.io/warn: baseline
```

### 3. Restricted (Most restrictive)
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: restricted-ns
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
```

## Network Policies

### Default Deny All
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

### Allow Frontend to Backend
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
```

### Allow DNS
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          name: kube-system
    ports:
    - protocol: UDP
      port: 53
```

**Reference:** See `assets/network-policy-template.yaml`

## RBAC Configuration

### Role (Name

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Comprehensive guide for implementing NetworkPolicy, PodSecurityPolicy, RBAC, and Pod Security Standards in Kubernetes.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Kubernetes Security Policies
- Para tarefas relacionadas a kubernetes security policies

## Diretrizes Específicas

