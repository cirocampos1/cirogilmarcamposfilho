---
name: robius-state-management-skill
description: Best practices for state management and persistence in Makepad applications based on Robrix and Moly codebases.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Robius State Management Skill

## Backstory

Você é um agente especializado em Robius State Management Skill.

## Contexto Original da Skill
Robius State Management Skill

## Instruções
---
name: robius-state-management
description: |
  CRITICAL: Use for Robius state management patterns. Triggers on:
  AppState, persistence, theme switch, 状态管理,
  Scope::with_data, save state, load state, serde,
  状态持久化, 主题切换
risk: unknown
source: community
---

# Robius State Management Skill

Best practices for state management and persistence in Makepad applications based on Robrix and Moly codebases.

**Source codebases:**
- **Robrix**: Matrix chat client - AppState, SelectedRoom, persistence via serde
- **Moly**: AI chat application - Central Store pattern, async initialization, Preferences

## When to Use

Use this skill when:
- Designing application state structure
- Implementing state persistence
- Passing state through widget tree
- Managing UI state across sessions
- Keywords: app state, makepad state, persistence, Scope::with_data, save state, load state

## Production Patterns

For production-ready state management patterns, see the `_base/` directory:

| Pattern | Description |
|---------|-------------|
| 06-global-registry | Global widget registry with Cx::set_global |
| 07-radio-navigation | Tab-style navigation with radio buttons |
| 10-state-machine | Enum-based state machine widgets |
| 11-theme-switching | Multi-theme support with apply_over |
| 12-local-persistence | Save/load user preferences |

## AppState Structure

### Core State Definition

```rust
use serde::{Serialize, Deserialize};
use std::collections::HashMap;
use matrix_sdk::ruma::OwnedRoomId;

/// App-wide state that is stored persistently across multiple app runs
/// and shared/updated across various parts of the app.
#[derive(Clone, Default, Debug, Serialize, Deserialize)]
pub struct AppState {
    /// The currently-selected room
    pub selected_room: Option<SelectedRoom>,

    /// Saved UI layout state for main view
    pub saved_layout_state: SavedLayoutState,

    /// Per-item saved states (e.g., per-space dock layouts)
    pub saved_state_per_item: HashMap<OwnedRoomId, SavedLayoutState>,

    /// Whether a user is currently logged in
    #[serde(skip)]  // Don't persist login state
    pub logged_in: bool,
}

/// Represents a currently selected item
#[derive(Clone, Debug, Serialize, Deserialize)]
pub enum SelectedRoom {
    JoinedRoom { room_name_id: RoomNameId },
    InvitedRoom { room_name_id: RoomNameId },
    Space { space_name_id: RoomNameId },
}

impl SelectedRoom {
    pub fn room_id(&self) -> &OwnedRoomId {
        match self {
            Self::JoinedRoom { room_name_id } => room_name_id.room_id(),
            Self::InvitedRoom { room_name_id } => room_name_id.room_id(),
            Self::Space { space_name_id } => space_name_id.room_id(),
        }
    }

    /// Upgrade from invited to joined state
    pub fn upgrade_invite_to_joined(&mut self, room_id: &RoomId) -> bool {
        match self {
            Self::InvitedRoom { room_name_id } if room_name_id.room_id() == room_id => {
                let name = room_name_id.clone();
                *se

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Best practices for state management and persistence in Makepad applications based on Robrix and Moly codebases.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Robius State Management Skill
- Para tarefas relacionadas a robius state management skill

## Diretrizes Específicas

