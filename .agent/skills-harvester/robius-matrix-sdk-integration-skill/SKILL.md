---
name: robius-matrix-sdk-integration-skill
description: Best practices for integrating external APIs with Makepad applications based on Robrix and Moly codebases.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Robius Matrix SDK Integration Skill

## Backstory

Você é um agente especializado em Robius Matrix SDK Integration Skill.

## Contexto Original da Skill
Robius Matrix SDK Integration Skill

## Instruções
---
name: robius-matrix-integration
description: |
  CRITICAL: Use for Matrix SDK integration with Makepad. Triggers on:
  Matrix SDK, sliding sync, MatrixRequest, timeline,
  matrix-sdk, matrix client, robrix, matrix room,
  Matrix 集成, 聊天客户端
risk: unknown
source: community
---

# Robius Matrix SDK Integration Skill

Best practices for integrating external APIs with Makepad applications based on Robrix and Moly codebases.

**Source codebases:**
- **Robrix**: Matrix SDK integration - sliding sync, timeline subscriptions, real-time updates
- **Moly**: OpenAI/LLM API integration - SSE streaming, MCP protocol, multi-provider support

## When to Use

Use this skill when:
- Integrating Matrix SDK with Makepad
- Building a Matrix client with Makepad
- Implementing Matrix features (rooms, timelines, messages)
- Handling Matrix SDK async operations in UI
- Keywords: matrix-sdk, matrix client, robrix, matrix timeline, matrix room, sliding sync

## Overview

Robrix uses the `matrix-sdk` and `matrix-sdk-ui` crates to connect to Matrix homeservers. The key architectural decisions:

1. **Sliding Sync**: Uses native sliding sync for efficient room list updates
2. **Separate Runtime**: Tokio runtime runs Matrix operations, Makepad handles UI
3. **Request/Response Pattern**: UI sends requests, receives actions/updates back
4. **Per-Room Background Tasks**: Each room has dedicated timeline subscriber task

## MatrixRequest Pattern

### Request Enum Definition

```rust
/// All async requests that can be made to the Matrix worker task
pub enum MatrixRequest {
    /// Login requests
    Login(LoginRequest),
    Logout { is_desktop: bool },

    /// Timeline operations
    PaginateRoomTimeline {
        room_id: OwnedRoomId,
        num_events: u16,
        direction: PaginationDirection,
    },
    SendMessage {
        room_id: OwnedRoomId,
        message: RoomMessageEventContent,
        replied_to: Option<Reply>,
    },
    EditMessage {
        room_id: OwnedRoomId,
        timeline_event_item_id: TimelineEventItemId,
        edited_content: EditedContent,
    },
    RedactMessage {
        room_id: OwnedRoomId,
        timeline_event_id: TimelineEventItemId,
        reason: Option<String>,
    },

    /// Room operations
    JoinRoom { room_id: OwnedRoomId },
    LeaveRoom { room_id: OwnedRoomId },
    GetRoomMembers {
        room_id: OwnedRoomId,
        memberships: RoomMemberships,
        local_only: bool,
    },

    /// User operations
    GetUserProfile {
        user_id: OwnedUserId,
        room_id: Option<OwnedRoomId>,
        local_only: bool,
    },
    IgnoreUser {
        ignore: bool,
        room_member: RoomMember,
        room_id: OwnedRoomId,
    },

    /// Media operations
    FetchAvatar {
        mxc_uri: OwnedMxcUri,
        on_fetched: fn(AvatarUpdate),
    },
    FetchMedia {
        media_request: MediaRequestParameters,
        on_fetched: OnMediaFetchedFn,
        destination: MediaCacheEntryRef,
        update_sender: Option<cross

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Best practices for integrating external APIs with Makepad applications based on Robrix and Moly codebases.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Robius Matrix SDK Integration Skill
- Para tarefas relacionadas a robius matrix sdk integration skill

## Diretrizes Específicas

