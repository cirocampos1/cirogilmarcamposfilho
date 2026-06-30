---
name: live-support-chat-widget
description: Build a real-time support chat system with a floating widget for users and an admin dashboard for support staff.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Live Support Chat Widget

## Backstory

Você é um agente especializado em Live Support Chat Widget.

## Contexto Original da Skill
Live Support Chat Widget

## Instruções
---
name: chat-widget
description: Build a real-time support chat system with a floating widget for users and an admin dashboard for support staff. Use when the user wants live chat, customer support chat, real-time messaging, or in-app support.
risk: unknown
source: community
---

# Live Support Chat Widget

Build a real-time support chat system with a floating widget for users and an admin dashboard for support staff.

## When to Use This Skill

Use when the user wants to:
- Add a live chat widget to their app
- Build customer support chat functionality
- Create real-time messaging between users and admins
- Add an in-app support channel

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND                                 │
├─────────────────────────────┬───────────────────────────────────┤
│   User Widget               │   Admin Dashboard                 │
│   - Floating chat button    │   - Chat list (active/archived)   │
│   - Message panel           │   - Conversation view             │
│   - Unread badge            │   - Archive/restore controls      │
│   - Connection indicator    │   - User info display             │
└─────────────┬───────────────┴───────────────┬───────────────────┘
              │                               │
              │     WebSocket + REST API      │
              ▼                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                        BACKEND                                  │
├─────────────────────────────────────────────────────────────────┤
│   Channels                  │   Controllers                     │
│   - ChatChannel (per chat)  │   - User: get/create chat         │
│   - AdminChannel (global)   │   - Admin: list, view, archive    │
├─────────────────────────────┼───────────────────────────────────┤
│   Models                    │   Jobs                            │
│   - Chat (1 per user)       │   - Email notification (delayed)  │
│   - Message (many per chat) │                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Implementation Guide

### Step 1: Data Models

Create two tables: `support_chats` and `support_messages`.

**support_chats**
```
id              - primary key (UUID recommended)
user_id         - foreign key to users (UNIQUE - one chat per user)
last_message_at - timestamp (for sorting chats by recency)
admin_viewed_at - timestamp (tracks when admin last viewed)
archived_at     - timestamp (null = active, set = archived)
created_at
updated_at
```

**support_messages**
```
id              - primary key (UUID recommended)
chat_id         - foreign key to support_chats
content         - text (required)
sender_type     - enum: 'user' | 'admin'
read_at         - timestamp (null = unread)
created_at
updated_at
```

**Key indexes:**
- `support_chats.user_id` (unique)
- `support_chats.last_message_at` (for

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Build a real-time support chat system with a floating widget for users and an admin dashboard for support staff.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Live Support Chat Widget
- Para tarefas relacionadas a live support chat widget

## Diretrizes Específicas

