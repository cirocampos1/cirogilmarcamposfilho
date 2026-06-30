---
name: avalonia-layout-zafiro
description: Guidelines for modern Avalonia UI layout using Zafiro.Avalonia, emphasizing shared styles, generic components, and avoiding XAML redundancy.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 3.0
architecture_focus: "Option B"
last_updated: 2026-03-28
verification_script: "scripts/verify.py"
---

# Avalonia Layout with Zafiro.Avalonia

> Master modern, clean, and maintainable Avalonia UI layouts.
> **Focus on semantic containers, shared styles, and minimal XAML.**

## 🎯 Selective Reading Rule

**Read ONLY files relevant to the layout challenge!**

---

## 📑 Content Map

| File | Description | When to Read |
|------|-------------|--------------|
| `themes.md` | Theme organization and shared styles | Setting up or refining app themes |
| `containers.md` | Semantic containers (`HeaderedContainer`, `EdgePanel`, `Card`) | Structuring views and layouts |
| `icons.md` | Icon usage with `IconExtension` and `IconOptions` | Adding and customizing icons |
| `behaviors.md` | `Xaml.Interaction.Behaviors` and avoiding Converters | Implementing complex interactions |
| `components.md` | Generic components and avoiding nesting | Creating reusable UI elements |

---

## 🔗 Related Project (Exemplary Implementation)

For a real-world example, refer to the **Angor** project:
`/mnt/fast/Repos/angor/src/Angor/Avalonia/Angor.Avalonia.sln`

---

## ✅ Checklist for Clean Layouts

- [ ] **Used semantic containers?** (e.g., `HeaderedContainer` instead of `Border` with manual header)
- [ ] **Avoided redundant properties?** Use shared styles in `axaml` files.
- [ ] **Minimized nesting?** Flatten layouts using `EdgePanel` or generic components.
- [ ] **Icons via extension?** Use `{Icon fa-name}` and `IconOptions` for styling.
- [ ] **Behaviors over code-behind?** Use `Interaction.Behaviors` for UI-logic.
- [ ] **Avoided Converters?** Prefer ViewModel properties or Behaviors unless necessary.

---

## ❌ Anti-Patterns

**DON'T:**
- Use hardcoded colors or sizes (literals) in views.
- Create deep nesting of `Grid` and `StackPanel`.
- Repeat visual properties across multiple elements (use Styles).
- Use `IValueConverter` for simple logic that belongs in the ViewModel.

**DO:**
- Use `DynamicResource` for colors and brushes.
- Extract repeated layouts into generic components.
- Leverage `Zafiro.Avalonia` specific panels like `EdgePanel` for common UI patterns.


## 🚀 Option B: Efficiency Guidelines (MANDATORY)

1. **Direct Action**: Never explain what you are going to do. Just do it.
2. **Token Economy**: Minimize chatter. Use the most concise tool calls possible.
3. **Verification First**: Run validation scripts immediately after any change.
4. **GPU Acceleration**: Use local GPU/Ollama for heavy analysis tasks when possible.
