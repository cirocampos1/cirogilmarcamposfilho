---
name: microsoftazurewebjobsextensionsauthenticationevent
description: Azure Functions extension for handling Microsoft Entra ID custom authentication events.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Microsoft.Azure.WebJobs.Extensions.AuthenticationEvents (.NET)

## Backstory

Você é um agente especializado em Microsoft.Azure.WebJobs.Extensions.AuthenticationEvents (.NET).

## Contexto Original da Skill
Microsoft.Azure.WebJobs.Extensions.AuthenticationEvents (.NET)

## Instruções
---
name: microsoft-azure-webjobs-extensions-authentication-events-dotnet
description: Microsoft Entra Authentication Events SDK for .NET. Azure Functions triggers for custom authentication extensions.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Microsoft.Azure.WebJobs.Extensions.AuthenticationEvents (.NET)

Azure Functions extension for handling Microsoft Entra ID custom authentication events.

## Installation

```bash
dotnet add package Microsoft.Azure.WebJobs.Extensions.AuthenticationEvents
```

**Current Version**: v1.1.0 (stable)

## Supported Events

| Event | Purpose |
|-------|---------|
| `OnTokenIssuanceStart` | Add custom claims to tokens during issuance |
| `OnAttributeCollectionStart` | Customize attribute collection UI before display |
| `OnAttributeCollectionSubmit` | Validate/modify attributes after user submission |
| `OnOtpSend` | Custom OTP delivery (SMS, email, etc.) |

## Core Workflows

### 1. Token Enrichment (Add Custom Claims)

Add custom claims to access or ID tokens during sign-in.

```csharp
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.AuthenticationEvents;
using Microsoft.Azure.WebJobs.Extensions.AuthenticationEvents.TokenIssuanceStart;
using Microsoft.Extensions.Logging;

public static class TokenEnrichmentFunction
{
    [FunctionName("OnTokenIssuanceStart")]
    public static WebJobsAuthenticationEventResponse Run(
        [WebJobsAuthenticationEventsTrigger] WebJobsTokenIssuanceStartRequest request,
        ILogger log)
    {
        log.LogInformation("Token issuance event for user: {UserId}", 
            request.Data?.AuthenticationContext?.User?.Id);

        // Create response with custom claims
        var response = new WebJobsTokenIssuanceStartResponse();
        
        // Add claims to the token
        response.Actions.Add(new WebJobsProvideClaimsForToken
        {
            Claims = new Dictionary<string, string>
            {
                { "customClaim1", "customValue1" },
                { "department", "Engineering" },
                { "costCenter", "CC-12345" },
                { "apiVersion", "v2" }
            }
        });

        return response;
    }
}
```

### 2. Token Enrichment with External Data

Fetch claims from external systems (databases, APIs).

```csharp
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.AuthenticationEvents;
using Microsoft.Azure.WebJobs.Extensions.AuthenticationEvents.TokenIssuanceStart;
using Microsoft.Extensions.Logging;
using System.Net.Http;
using System.Text.Json;

public static class TokenEnrichmentWithExternalData
{
    private static readonly HttpClient _httpClient = new();

    [FunctionName("OnTokenIssuanceStartExternal")]
    public static async Task<WebJobsAuthenticationEventResponse> Run(
        [WebJobsAuthenticationEventsTrigger] WebJobsTokenIssuanceStartRequest request,
        ILogger log)
    {
        string? userId = request.Data?.AuthenticationContext?.User?.Id;
     

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Azure Functions extension for handling Microsoft Entra ID custom authentication events.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Microsoft.Azure.WebJobs.Extensions.AuthenticationEvents (.NET)
- Para tarefas relacionadas a microsoftazurewebjobsextensionsauthenticationevent

## Diretrizes Específicas

