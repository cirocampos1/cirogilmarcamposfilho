---
name: expo-ui-guidelines
description: - You are building a native-feeling Expo Router application and need guidance on navigation, controls, effects, or platform-specific UI. - You need to decide whether Expo Go is sufficient or a custom 
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Expo UI Guidelines

## Backstory

Você é um agente especializado em Expo UI Guidelines.

## Contexto Original da Skill
Expo UI Guidelines

## Instruções
---
name: building-native-ui
description: Complete guide for building beautiful apps with Expo Router. Covers fundamentals, styling, components, navigation, animations, patterns, and native tabs.
risk: unknown
source: community
version: 1.0.1
license: MIT
---

# Expo UI Guidelines

## When to Use

- You are building a native-feeling Expo Router application and need guidance on navigation, controls, effects, or platform-specific UI.
- You need to decide whether Expo Go is sufficient or a custom native build is actually required.
- The task involves modern Expo UI patterns across animations, tabs, headers, storage, media, or visual effects.

## References

Consult these resources as needed:

```
references/
  animations.md          Reanimated: entering, exiting, layout, scroll-driven, gestures
  controls.md            Native iOS: Switch, Slider, SegmentedControl, DateTimePicker, Picker
  form-sheet.md          Form sheets in expo-router: configuration, footers and background interaction. 
  gradients.md           CSS gradients via experimental_backgroundImage (New Arch only)
  icons.md               SF Symbols via expo-image (sf: source), names, animations, weights
  media.md               Camera, audio, video, and file saving
  route-structure.md     Route conventions, dynamic routes, groups, folder organization
  search.md              Search bar with headers, useSearch hook, filtering patterns
  storage.md             SQLite, AsyncStorage, SecureStore
  tabs.md                NativeTabs, migration from JS tabs, iOS 26 features
  toolbar-and-headers.md Stack headers and toolbar buttons, menus, search (iOS only)
  visual-effects.md      Blur (expo-blur) and liquid glass (expo-glass-effect)
  webgpu-three.md        3D graphics, games, GPU visualizations with WebGPU and Three.js
  zoom-transitions.md    Apple Zoom: fluid zoom transitions with Link.AppleZoom (iOS 18+)
```

## Running the App

**CRITICAL: Always try Expo Go first before creating custom builds.**

Most Expo apps work in Expo Go without any custom native code. Before running `npx expo run:ios` or `npx expo run:android`:

1. **Start with Expo Go**: Run `npx expo start` and scan the QR code with Expo Go
2. **Check if features work**: Test your app thoroughly in Expo Go
3. **Only create custom builds when required** - see below

### When Custom Builds Are Required

You need `npx expo run:ios/android` or `eas build` ONLY when using:

- **Local Expo modules** (custom native code in `modules/`)
- **Apple targets** (widgets, app clips, extensions via `@bacons/apple-targets`)
- **Third-party native modules** not included in Expo Go
- **Custom native configuration** that can't be expressed in `app.json`

### When Expo Go Works

Expo Go supports a huge range of features out of the box:

- All `expo-*` packages (camera, location, notifications, etc.)
- Expo Router navigation
- Most UI libraries (reanimated, gesture handler, etc.)
- Push notifications, deep links, and more

**If you're unsure, try 

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- You are building a native-feeling Expo Router application and need guidance on navigation, controls, effects, or platform-specific UI. - You need to decide whether Expo Go is sufficient or a custom 

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Expo UI Guidelines
- Para tarefas relacionadas a expo ui guidelines

## Diretrizes Específicas

