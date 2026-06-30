---
name: neon-postgres
description: "Expert patterns for Neon serverless Postgres, branching, connection pooling, and Prisma/Drizzle integration Use when: neon database, serverless postgres, database branching, neon postgres, postgres serverless."
source: vibeship-spawner-skills (Apache 2.0)
version: 3.0
architecture_focus: "Option B"
last_updated: 2026-03-28
verification_script: "scripts/verify.py"
---

# Neon Postgres

## Patterns

### Prisma with Neon Connection

Configure Prisma for Neon with connection pooling.

Use two connection strings:
- DATABASE_URL: Pooled connection for Prisma Client
- DIRECT_URL: Direct connection for Prisma Migrate

The pooled connection uses PgBouncer for up to 10K connections.
Direct connection required for migrations (DDL operations).


### Drizzle with Neon Serverless Driver

Use Drizzle ORM with Neon's serverless HTTP driver for
edge/serverless environments.

Two driver options:
- neon-http: Single queries over HTTP (fastest for one-off queries)
- neon-serverless: WebSocket for transactions and sessions


### Connection Pooling with PgBouncer

Neon provides built-in connection pooling via PgBouncer.

Key limits:
- Up to 10,000 concurrent connections to pooler
- Connections still consume underlying Postgres connections
- 7 connections reserved for Neon superuser

Use pooled endpoint for application, direct for migrations.


## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | high | See docs |
| Issue | high | See docs |
| Issue | high | See docs |
| Issue | medium | See docs |
| Issue | medium | See docs |
| Issue | low | See docs |
| Issue | medium | See docs |
| Issue | high | See docs |


## 🚀 Option B: Efficiency Guidelines (MANDATORY)

1. **Direct Action**: Never explain what you are going to do. Just do it.
2. **Token Economy**: Minimize chatter. Use the most concise tool calls possible.
3. **Verification First**: Run validation scripts immediately after any change.
4. **GPU Acceleration**: Use local GPU/Ollama for heavy analysis tasks when possible.
