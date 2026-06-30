---
name: terraform-module-library
description: Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Terraform Module Library

## Backstory

Você é um agente especializado em Terraform Module Library.

## Contexto Original da Skill
Terraform Module Library

## Instruções
---
name: terraform-module-library
description: "Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Terraform Module Library

Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure.

## Do not use this skill when

- The task is unrelated to terraform module library
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Create reusable, well-tested Terraform modules for common cloud infrastructure patterns across multiple cloud providers.

## Use this skill when

- Build reusable infrastructure components
- Standardize cloud resource provisioning
- Implement infrastructure as code best practices
- Create multi-cloud compatible modules
- Establish organizational Terraform standards

## Module Structure

```
terraform-modules/
├── aws/
│   ├── vpc/
│   ├── eks/
│   ├── rds/
│   └── s3/
├── azure/
│   ├── vnet/
│   ├── aks/
│   └── storage/
└── gcp/
    ├── vpc/
    ├── gke/
    └── cloud-sql/
```

## Standard Module Pattern

```
module-name/
├── main.tf          # Main resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider versions
├── README.md        # Documentation
├── examples/        # Usage examples
│   └── complete/
│       ├── main.tf
│       └── variables.tf
└── tests/           # Terratest files
    └── module_test.go
```

## AWS VPC Module Example

**main.tf:**
```hcl
resource "aws_vpc" "main" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support   = var.enable_dns_support

  tags = merge(
    {
      Name = var.name
    },
    var.tags
  )
}

resource "aws_subnet" "private" {
  count             = length(var.private_subnet_cidrs)
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]

  tags = merge(
    {
      Name = "${var.name}-private-${count.index + 1}"
      Tier = "private"
    },
    var.tags
  )
}

resource "aws_internet_gateway" "main" {
  count  = var.create_internet_gateway ? 1 : 0
  vpc_id = aws_vpc.main.id

  tags = merge(
    {
      Name = "${var.name}-igw"
    },
    var.tags
  )
}
```

**variables.tf:**
```hcl
variable "name" {
  description = "Name of the VPC"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for VPC"
  type        = string
  validation {
    condition     = can(regex("^([0-9]{1,3}\\.){3}[0-9]{1,3}/[0-9]{1,2}$", var.cidr_block))
    error_message = "CIDR block must be valid IPv4 CIDR notation."
  }
}

variable "availability_zones" {
  description = "List of availability zo

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Terraform Module Library
- Para tarefas relacionadas a terraform module library

## Diretrizes Específicas

