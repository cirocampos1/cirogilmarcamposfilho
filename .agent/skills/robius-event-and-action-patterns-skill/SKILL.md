---
name: robius-event-and-action-patterns-skill
description: Best practices for event handling and action patterns in Makepad applications based on Robrix and Moly codebases.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Robius Event and Action Patterns Skill

## Backstory

Você é um agente especializado em Robius Event and Action Patterns Skill.

## Contexto Original da Skill
Robius Event and Action Patterns Skill

## Instruções
---
name: robius-event-action
description: |
  CRITICAL: Use for Robius event and action patterns. Triggers on:
  custom action, MatchEvent, post_action, cx.widget_action,
  handle_actions, DefaultNone, widget action, event handling,
  事件处理, 自定义动作
risk: unknown
source: community
---

# Robius Event and Action Patterns Skill

Best practices for event handling and action patterns in Makepad applications based on Robrix and Moly codebases.

**Source codebases:**
- **Robrix**: Matrix chat client - MessageAction, RoomsListAction, AppStateAction
- **Moly**: AI chat application - StoreAction, ChatAction, NavigationAction, Timer patterns

## When to Use

Use this skill when:
- Implementing custom actions in Makepad
- Handling events in widgets
- Centralizing action handling in App
- Widget-to-widget communication
- Keywords: makepad action, makepad event, widget action, handle_actions, cx.widget_action

## Custom Action Pattern

### Defining Domain-Specific Actions

```rust
use makepad_widgets::*;

/// Actions emitted by the Message widget
#[derive(Clone, DefaultNone, Debug)]
pub enum MessageAction {
    /// User wants to react to a message
    React { details: MessageDetails, reaction: String },
    /// User wants to reply to a message
    Reply(MessageDetails),
    /// User wants to edit a message
    Edit(MessageDetails),
    /// User wants to delete a message
    Delete(MessageDetails),
    /// User requested to open context menu
    OpenContextMenu { details: MessageDetails, abs_pos: DVec2 },
    /// Required default variant
    None,
}

/// Data associated with a message action
#[derive(Clone, Debug)]
pub struct MessageDetails {
    pub room_id: OwnedRoomId,
    pub event_id: OwnedEventId,
    pub content: String,
    pub sender_id: OwnedUserId,
}
```

### Emitting Actions from Widgets

```rust
impl Widget for Message {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.view.handle_event(cx, event, scope);

        let area = self.view.area();
        match event.hits(cx, area) {
            Hit::FingerDown(_fe) => {
                cx.set_key_focus(area);
            }
            Hit::FingerUp(fe) => {
                if fe.is_over && fe.is_primary_hit() && fe.was_tap() {
                    // Emit widget action
                    cx.widget_action(
                        self.widget_uid(),
                        &scope.path,
                        MessageAction::Reply(self.get_details()),
                    );
                }
            }
            Hit::FingerLongPress(lpe) => {
                cx.widget_action(
                    self.widget_uid(),
                    &scope.path,
                    MessageAction::OpenContextMenu {
                        details: self.get_details(),
                        abs_pos: lpe.abs,
                    },
                );
            }
            _ => {}
        }
    }
}
```

## Centralized Action Handling in App

### Using MatchEvent Trait

```

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Best practices for event handling and action patterns in Makepad applications based on Robrix and Moly codebases.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Robius Event and Action Patterns Skill
- Para tarefas relacionadas a robius event and action patterns skill

## Diretrizes Específicas

