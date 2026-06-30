---
name: clerk-auth
description: "Expert patterns for Clerk auth implementation, middleware, organizations, webhooks, and user sync Use when: adding authentication, clerk auth, user authentication, sign in, sign up."
source: vibeship-spawner-skills (Apache 2.0)
version: 3.0
architecture_focus: "Option B"
last_updated: 2026-03-28
verification_script: "scripts/verify.py"
---

# Clerk Authentication

## Patterns

### Next.js App Router Setup

Complete Clerk setup for Next.js 14/15 App Router.

Includes ClerkProvider, environment variables, and basic
sign-in/sign-up components.

Key components:
- ClerkProvider: Wraps app for auth context
- <SignIn />, <SignUp />: Pre-built auth forms
- <UserButton />: User menu with session management


### Middleware Route Protection

Protect routes using clerkMiddleware and createRouteMatcher.

Best practices:
- Single middleware.ts file at project root
- Use createRouteMatcher for route groups
- auth.protect() for explicit protection
- Centralize all auth logic in middleware


### Server Component Authentication

Access auth state in Server Components using auth() and currentUser().

Key functions:
- auth(): Returns userId, sessionId, orgId, claims
- currentUser(): Returns full User object
- Both require clerkMiddleware to be configured


## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | critical | See docs |
| Issue | high | See docs |
| Issue | high | See docs |
| Issue | high | See docs |
| Issue | medium | See docs |
| Issue | medium | See docs |
| Issue | medium | See docs |
| Issue | medium | See docs |


## 🚀 Option B: Efficiency Guidelines (MANDATORY)

1. **Direct Action**: Never explain what you are going to do. Just do it.
2. **Token Economy**: Minimize chatter. Use the most concise tool calls possible.
3. **Verification First**: Run validation scripts immediately after any change.
4. **GPU Acceleration**: Use local GPU/Ollama for heavy analysis tasks when possible.
