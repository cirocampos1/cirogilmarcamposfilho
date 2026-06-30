---
name: react-flow-node
description: Create React Flow node components following established patterns with proper TypeScript types and store integration.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# React Flow Node

## Backstory

Você é um agente especializado em React Flow Node.

## Contexto Original da Skill
React Flow Node

## Instruções
---
name: react-flow-node-ts
description: "Create React Flow node components following established patterns with proper TypeScript types and store integration."
risk: unknown
source: community
date_added: "2026-02-27"
---

# React Flow Node

Create React Flow node components following established patterns with proper TypeScript types and store integration.

## Quick Start

Copy templates from assets/ and replace placeholders:
- `{{NodeName}}` → PascalCase component name (e.g., `VideoNode`)
- `{{nodeType}}` → kebab-case type identifier (e.g., `video-node`)
- `{{NodeData}}` → Data interface name (e.g., `VideoNodeData`)

## Templates

- assets/template.tsx - Node component
- assets/types.template.ts - TypeScript definitions

## Node Component Pattern

```tsx
export const MyNode = memo(function MyNode({
  id,
  data,
  selected,
  width,
  height,
}: MyNodeProps) {
  const updateNode = useAppStore((state) => state.updateNode);
  const canvasMode = useAppStore((state) => state.canvasMode);
  
  return (
    <>
      <NodeResizer isVisible={selected && canvasMode === 'editing'} />
      <div className="node-container">
        <Handle type="target" position={Position.Top} />
        {/* Node content */}
        <Handle type="source" position={Position.Bottom} />
      </div>
    </>
  );
});
```

## Type Definition Pattern

```typescript
export interface MyNodeData extends Record<string, unknown> {
  title: string;
  description?: string;
}

export type MyNode = Node<MyNodeData, 'my-node'>;
```

## Integration Steps

1. Add type to `src/frontend/src/types/index.ts`
2. Create component in `src/frontend/src/components/nodes/`
3. Export from `src/frontend/src/components/nodes/index.ts`
4. Add defaults in `src/frontend/src/store/app-store.ts`
5. Register in canvas `nodeTypes`
6. Add to AddBlockMenu and ConnectMenu

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Create React Flow node components following established patterns with proper TypeScript types and store integration.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em React Flow Node
- Para tarefas relacionadas a react flow node

## Diretrizes Específicas

