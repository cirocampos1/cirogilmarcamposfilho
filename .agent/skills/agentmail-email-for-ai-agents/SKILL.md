---
name: agentmail-email-for-ai-agents
description: AgentMail gives AI agents real email addresses (`@theagentmail.net`) with a REST API. Agents can send and receive email, sign up for services (GitHub, AWS, Slack, etc.), and get verification codes. A 
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Mail — Email for AI Agents

## Backstory

Você é um agente especializado em Mail — Email for AI Agents.

## Contexto Original da Skill
AgentMail — Email for AI Agents

## Instruções
---
name: agentmail
description: Email infrastructure for AI agents. Create accounts, send/receive emails, manage webhooks, and check karma balance via the AgentMail API.
risk: safe
source: community
---

# AgentMail — Email for AI Agents

AgentMail gives AI agents real email addresses (`@theagentmail.net`) with a REST API. Agents can send and receive email, sign up for services (GitHub, AWS, Slack, etc.), and get verification codes. A karma system prevents spam and keeps the shared domain's reputation high.

Base URL: `https://api.theagentmail.net`

## When to Use

- An AI agent needs a real inbox/outbox for signups, verification flows, or transactional communication.
- You need to provision AgentMail accounts, send messages, read inbox contents, or register inbound webhooks.
- You need to monitor karma usage or wire email events into agent automation.

## Quick start

All requests require `Authorization: Bearer am_...` header (API key from dashboard).

### Create an email account (-10 karma)

```bash
curl -X POST https://api.theagentmail.net/v1/accounts \
  -H "Authorization: Bearer am_..." \
  -H "Content-Type: application/json" \
  -d '{"address": "my-agent@theagentmail.net"}'
```

Response: `{"data": {"id": "...", "address": "my-agent@theagentmail.net", "displayName": null, "createdAt": 123}}`

### Send email (-1 karma)

```bash
curl -X POST https://api.theagentmail.net/v1/accounts/{accountId}/messages \
  -H "Authorization: Bearer am_..." \
  -H "Content-Type: application/json" \
  -d '{
    "to": ["recipient@example.com"],
    "subject": "Hello from my agent",
    "text": "Plain text body",
    "html": "<p>Optional HTML body</p>"
  }'
```

Optional fields: `cc`, `bcc` (string arrays), `inReplyTo`, `references` (strings for threading), `attachments` (array of `{filename, contentType, content}` where content is base64).

### Read inbox

```bash
# List messages
curl https://api.theagentmail.net/v1/accounts/{accountId}/messages \
  -H "Authorization: Bearer am_..."

# Get full message (with body and attachments)
curl https://api.theagentmail.net/v1/accounts/{accountId}/messages/{messageId} \
  -H "Authorization: Bearer am_..."
```

### Check karma

```bash
curl https://api.theagentmail.net/v1/karma \
  -H "Authorization: Bearer am_..."
```

Response: `{"data": {"balance": 90, "events": [...]}}`

### Register webhook (real-time inbound)

```bash
curl -X POST https://api.theagentmail.net/v1/accounts/{accountId}/webhooks \
  -H "Authorization: Bearer am_..." \
  -H "Content-Type: application/json" \
  -d '{"url": "https://my-agent.example.com/inbox"}'
```

Webhook deliveries include two security headers:
- `X-AgentMail-Signature` -- HMAC-SHA256 hex digest of the request body, signed with the webhook secret
- `X-AgentMail-Timestamp` -- millisecond timestamp of when the delivery was sent

Verify the signature and reject requests with timestamps older than 5 minutes to prevent replay attacks:

```typescript
import { createHmac } from "crypto";

cons

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

AgentMail gives AI agents real email addresses (`@theagentmail.net`) with a REST API. Agents can send and receive email, sign up for services (GitHub, AWS, Slack, etc.), and get verification codes. A 

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Mail — Email for AI Agents
- Para tarefas relacionadas a agentmail email for ai agents

## Diretrizes Específicas

