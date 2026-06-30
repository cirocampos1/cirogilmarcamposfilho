---
name: azure-key-vault-certificates-sdk-for-rust
description: Client library for Azure Key Vault Certificates — secure storage and management of certificates.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Key Vault Certificates SDK for Rust

## Backstory

Você é um agente especializado em Azure Key Vault Certificates SDK for Rust.

## Contexto Original da Skill
Azure Key Vault Certificates SDK for Rust

## Instruções
---
name: azure-keyvault-certificates-rust
description: Azure Key Vault Certificates SDK for Rust. Use for creating, importing, and managing certificates.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure Key Vault Certificates SDK for Rust

Client library for Azure Key Vault Certificates — secure storage and management of certificates.

## Installation

```sh
cargo add azure_security_keyvault_certificates azure_identity
```

## Environment Variables

```bash
AZURE_KEYVAULT_URL=https://<vault-name>.vault.azure.net/
```

## Authentication

```rust
use azure_identity::DeveloperToolsCredential;
use azure_security_keyvault_certificates::CertificateClient;

let credential = DeveloperToolsCredential::new(None)?;
let client = CertificateClient::new(
    "https://<vault-name>.vault.azure.net/",
    credential.clone(),
    None,
)?;
```

## Core Operations

### Get Certificate

```rust
use azure_core::base64;

let certificate = client
    .get_certificate("certificate-name", None)
    .await?
    .into_model()?;

println!(
    "Thumbprint: {:?}",
    certificate.x509_thumbprint.map(base64::encode_url_safe)
);
```

### Create Certificate

```rust
use azure_security_keyvault_certificates::models::{
    CreateCertificateParameters, CertificatePolicy,
    IssuerParameters, X509CertificateProperties,
};

let policy = CertificatePolicy {
    issuer_parameters: Some(IssuerParameters {
        name: Some("Self".into()),
        ..Default::default()
    }),
    x509_certificate_properties: Some(X509CertificateProperties {
        subject: Some("CN=example.com".into()),
        ..Default::default()
    }),
    ..Default::default()
};

let params = CreateCertificateParameters {
    certificate_policy: Some(policy),
    ..Default::default()
};

let operation = client
    .create_certificate("cert-name", params.try_into()?, None)
    .await?;
```

### Import Certificate

```rust
use azure_security_keyvault_certificates::models::ImportCertificateParameters;

let params = ImportCertificateParameters {
    base64_encoded_certificate: Some(base64_cert_data),
    password: Some("optional-password".into()),
    ..Default::default()
};

let certificate = client
    .import_certificate("cert-name", params.try_into()?, None)
    .await?
    .into_model()?;
```

### Delete Certificate

```rust
client.delete_certificate("certificate-name", None).await?;
```

### List Certificates

```rust
use azure_security_keyvault_certificates::ResourceExt;
use futures::TryStreamExt;

let mut pager = client.list_certificate_properties(None)?.into_stream();
while let Some(cert) = pager.try_next().await? {
    let name = cert.resource_id()?.name;
    println!("Certificate: {}", name);
}
```

### Get Certificate Policy

```rust
let policy = client
    .get_certificate_policy("certificate-name", None)
    .await?
    .into_model()?;
```

### Update Certificate Policy

```rust
use azure_security_keyvault_certificates::models::UpdateCertificatePolicyParameters;

let params = Upda

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Client library for Azure Key Vault Certificates — secure storage and management of certificates.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Key Vault Certificates SDK for Rust
- Para tarefas relacionadas a azure key vault certificates sdk for rust

## Diretrizes Específicas

