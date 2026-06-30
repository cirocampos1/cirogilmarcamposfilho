---
name: gitops-workflow
description: Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# GitOps Workflow

## Backstory

Você é um agente especializado em GitOps Workflow.

## Contexto Original da Skill
GitOps Workflow

## Instruções
---
name: gitops-workflow
description: "Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments."
risk: critical
source: community
date_added: "2026-02-27"
---

# GitOps Workflow

Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments.

## Purpose

Implement declarative, Git-based continuous delivery for Kubernetes using ArgoCD or Flux CD, following OpenGitOps principles.

## Use this skill when

- Set up GitOps for Kubernetes clusters
- Automate application deployments from Git
- Implement progressive delivery strategies
- Manage multi-cluster deployments
- Configure automated sync policies
- Set up secret management in GitOps

## Do not use this skill when

- You need a one-off manual deployment
- You cannot manage cluster access or repo permissions
- You are not deploying to Kubernetes

## Instructions

1. Define repo layout and desired-state conventions.
2. Install ArgoCD or Flux and connect clusters.
3. Configure sync policies, environments, and promotion flow.
4. Validate rollbacks and secret handling.

## Safety

- Avoid auto-sync to production without approvals.
- Keep secrets out of Git and use sealed or external secret managers.

## OpenGitOps Principles

1. **Declarative** - Entire system described declaratively
2. **Versioned and Immutable** - Desired state stored in Git
3. **Pulled Automatically** - Software agents pull desired state
4. **Continuously Reconciled** - Agents reconcile actual vs desired state

## ArgoCD Setup

### 1. Installation

```bash
# Create namespace
kubectl create namespace argocd

# Install ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Get admin password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

**Reference:** See `references/argocd-setup.md` for detailed setup

### 2. Repository Structure

```
gitops-repo/
├── apps/
│   ├── production/
│   │   ├── app1/
│   │   │   ├── kustomization.yaml
│   │   │   └── deployment.yaml
│   │   └── app2/
│   └── staging/
├── infrastructure/
│   ├── ingress-nginx/
│   ├── cert-manager/
│   └── monitoring/
└── argocd/
    ├── applications/
    └── projects/
```

### 3. Create Application

```yaml
# argocd/applications/my-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/gitops-repo
    targetRevision: main
    path: apps/production/my-app
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```

### 4. App of Apps Pattern

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: applications
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https:

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em GitOps Workflow
- Para tarefas relacionadas a gitops workflow

## Diretrizes Específicas

