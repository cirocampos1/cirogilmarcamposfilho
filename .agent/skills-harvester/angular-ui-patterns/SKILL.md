---
name: angular-ui-patterns
description: 1. **Never show stale UI** - Loading states only when actually loading 2. **Always surface errors** - Users must know when something fails 3. **Optimistic updates** - Make the UI feel instant 4. **Pro
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Angular UI Patterns

## Backstory

Você é um agente especializado em Angular UI Patterns.

## Contexto Original da Skill
Angular UI Patterns

## Instruções
---
name: angular-ui-patterns
description: "Modern Angular UI patterns for loading states, error handling, and data display. Use when building UI components, handling async data, or managing component states."
risk: safe
source: self
date_added: "2026-02-27"
---

# Angular UI Patterns

## Core Principles

1. **Never show stale UI** - Loading states only when actually loading
2. **Always surface errors** - Users must know when something fails
3. **Optimistic updates** - Make the UI feel instant
4. **Progressive disclosure** - Use `@defer` to show content as available
5. **Graceful degradation** - Partial data is better than no data

---

## Loading State Patterns

### The Golden Rule

**Show loading indicator ONLY when there's no data to display.**

```typescript
@Component({
  template: `
    @if (error()) {
      <app-error-state [error]="error()" (retry)="load()" />
    } @else if (loading() && !items().length) {
      <app-skeleton-list />
    } @else if (!items().length) {
      <app-empty-state message="No items found" />
    } @else {
      <app-item-list [items]="items()" />
    }
  `,
})
export class ItemListComponent {
  private store = inject(ItemStore);

  items = this.store.items;
  loading = this.store.loading;
  error = this.store.error;
}
```

### Loading State Decision Tree

```
Is there an error?
  → Yes: Show error state with retry option
  → No: Continue

Is it loading AND we have no data?
  → Yes: Show loading indicator (spinner/skeleton)
  → No: Continue

Do we have data?
  → Yes, with items: Show the data
  → Yes, but empty: Show empty state
  → No: Show loading (fallback)
```

### Skeleton vs Spinner

| Use Skeleton When    | Use Spinner When      |
| -------------------- | --------------------- |
| Known content shape  | Unknown content shape |
| List/card layouts    | Modal actions         |
| Initial page load    | Button submissions    |
| Content placeholders | Inline operations     |

---

## Control Flow Patterns

### @if/@else for Conditional Rendering

```html
@if (user(); as user) {
<span>Welcome, {{ user.name }}</span>
} @else if (loading()) {
<app-spinner size="small" />
} @else {
<a routerLink="/login">Sign In</a>
}
```

### @for with Track

```html
@for (item of items(); track item.id) {
<app-item-card [item]="item" (delete)="remove(item.id)" />
} @empty {
<app-empty-state
  icon="inbox"
  message="No items yet"
  actionLabel="Create Item"
  (action)="create()"
/>
}
```

### @defer for Progressive Loading

```html
<!-- Critical content loads immediately -->
<app-header />
<app-hero-section />

<!-- Non-critical content deferred -->
@defer (on viewport) {
<app-comments [postId]="postId()" />
} @placeholder {
<div class="h-32 bg-gray-100 animate-pulse"></div>
} @loading (minimum 200ms) {
<app-spinner />
} @error {
<app-error-state message="Failed to load comments" />
}
```

---

## Error Handling Patterns

### Error Handling Hierarchy

```
1. Inline error (field-level) → Form validation errors
2. Toast notificat

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

1. **Never show stale UI** - Loading states only when actually loading 2. **Always surface errors** - Users must know when something fails 3. **Optimistic updates** - Make the UI feel instant 4. **Pro

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Angular UI Patterns
- Para tarefas relacionadas a angular ui patterns

## Diretrizes Específicas

