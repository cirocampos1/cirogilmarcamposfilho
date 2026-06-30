---
name: aws-compliance-checker
description: Automated compliance validation against industry standards including CIS AWS Foundations, PCI-DSS, HIPAA, and SOC 2.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# AWS Compliance Checker

## Backstory

Você é um agente especializado em AWS Compliance Checker.

## Contexto Original da Skill
AWS Compliance Checker

## Instruções
---
name: aws-compliance-checker
description: "Automated compliance checking against CIS, PCI-DSS, HIPAA, and SOC 2 benchmarks"
category: security
risk: safe
source: community
tags: "[aws, compliance, audit, cis, pci-dss, hipaa, kiro-cli]"
date_added: "2026-02-27"
---

# AWS Compliance Checker

Automated compliance validation against industry standards including CIS AWS Foundations, PCI-DSS, HIPAA, and SOC 2.

## When to Use
Use this skill when you need to validate AWS compliance against industry standards, prepare for audits, or maintain continuous compliance monitoring.

## Supported Frameworks

**CIS AWS Foundations Benchmark**
- Identity and Access Management
- Logging and Monitoring
- Networking
- Data Protection

**PCI-DSS (Payment Card Industry)**
- Network security
- Access controls
- Encryption
- Monitoring and logging

**HIPAA (Healthcare)**
- Access controls
- Audit controls
- Data encryption
- Transmission security

**SOC 2**
- Security
- Availability
- Confidentiality
- Privacy

## CIS AWS Foundations Checks

### Identity & Access Management (1.x)

```bash
#!/bin/bash
# cis-iam-checks.sh

echo "=== CIS IAM Compliance Checks ==="

# 1.1: Root account usage
echo "1.1: Checking root account usage..."
root_usage=$(aws iam get-credential-report --output text | \
  awk -F, 'NR==2 {print $5,$11}')
echo "  Root password last used: $root_usage"

# 1.2: MFA on root account
echo "1.2: Checking root MFA..."
root_mfa=$(aws iam get-account-summary \
  --query 'SummaryMap.AccountMFAEnabled' --output text)
echo "  Root MFA enabled: $root_mfa"

# 1.3: Unused credentials
echo "1.3: Checking for unused credentials (>90 days)..."
aws iam get-credential-report --output text | \
  awk -F, 'NR>1 {
    if ($5 != "N/A" && $5 != "no_information") {
      cmd = "date -d \"" $5 "\" +%s"
      cmd | getline last_used
      close(cmd)
      now = systime()
      days = (now - last_used) / 86400
      if (days > 90) print "  ⚠️  " $1 ": " int(days) " days inactive"
    }
  }'

# 1.4: Access keys rotated
echo "1.4: Checking access key age..."
aws iam list-users --query 'Users[*].UserName' --output text | \
while read user; do
  aws iam list-access-keys --user-name "$user" \
    --query 'AccessKeyMetadata[*].[AccessKeyId,CreateDate]' \
    --output text | \
  while read key_id create_date; do
    age_days=$(( ($(date +%s) - $(date -d "$create_date" +%s)) / 86400 ))
    if [ $age_days -gt 90 ]; then
      echo "  ⚠️  $user: Key $key_id is $age_days days old"
    fi
  done
done

# 1.5-1.11: Password policy
echo "1.5-1.11: Checking password policy..."
policy=$(aws iam get-account-password-policy 2>&1)
if echo "$policy" | grep -q "NoSuchEntity"; then
  echo "  ❌ No password policy configured"
else
  echo "  ✓ Password policy exists"
  echo "$policy" | jq '.PasswordPolicy | {
    MinimumPasswordLength,
    RequireSymbols,
    RequireNumbers,
    RequireUppercaseCharacters,
    RequireLowercaseCharacters,
    MaxPasswordAge,
    PasswordReusePrevention
  }'
fi

# 1.12-1.1

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automated compliance validation against industry standards including CIS AWS Foundations, PCI-DSS, HIPAA, and SOC 2.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em AWS Compliance Checker
- Para tarefas relacionadas a aws compliance checker

## Diretrizes Específicas

