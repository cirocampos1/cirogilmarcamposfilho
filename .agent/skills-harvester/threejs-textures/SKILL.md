---
name: threejs-textures
description: - You need to load, configure, or optimize textures in Three.js. - The task involves UV mapping, texture settings, cubemaps, environment maps, or HDR texture workflows. - You are working on surface de
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Three.js Textures

## Backstory

Você é um agente especializado em Three.js Textures.

## Contexto Original da Skill
Three.js Textures

## Instruções
---
name: threejs-textures
description: Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when working with images, UV coordinates, cubemaps, HDR environments, or texture optimization.
risk: unknown
source: community
---

# Three.js Textures

## When to Use

- You need to load, configure, or optimize textures in Three.js.
- The task involves UV mapping, texture settings, cubemaps, environment maps, or HDR texture workflows.
- You are working on surface detail and material inputs rather than geometry or animation.

## Quick Start

```javascript
import * as THREE from "three";

// Load texture
const loader = new THREE.TextureLoader();
const texture = loader.load("texture.jpg");

// Apply to material
const material = new THREE.MeshStandardMaterial({
  map: texture,
});
```

## Texture Loading

### Basic Loading

```javascript
const loader = new THREE.TextureLoader();

// Async with callbacks
loader.load(
  "texture.jpg",
  (texture) => console.log("Loaded"),
  (progress) => console.log("Progress"),
  (error) => console.error("Error"),
);

// Synchronous style (loads async internally)
const texture = loader.load("texture.jpg");
material.map = texture;
```

### Promise Wrapper

```javascript
function loadTexture(url) {
  return new Promise((resolve, reject) => {
    new THREE.TextureLoader().load(url, resolve, undefined, reject);
  });
}

// Usage
const [colorMap, normalMap, roughnessMap] = await Promise.all([
  loadTexture("color.jpg"),
  loadTexture("normal.jpg"),
  loadTexture("roughness.jpg"),
]);
```

## Texture Configuration

### Color Space

Critical for accurate color reproduction.

```javascript
// Color/albedo textures - use sRGB
colorTexture.colorSpace = THREE.SRGBColorSpace;

// Data textures (normal, roughness, metalness, AO) - leave as default
// Do NOT set colorSpace for data textures (NoColorSpace is default)
```

### Wrapping Modes

```javascript
texture.wrapS = THREE.RepeatWrapping; // Horizontal
texture.wrapT = THREE.RepeatWrapping; // Vertical

// Options:
// THREE.ClampToEdgeWrapping - Stretches edge pixels (default)
// THREE.RepeatWrapping - Tiles the texture
// THREE.MirroredRepeatWrapping - Tiles with mirror flip
```

### Repeat, Offset, Rotation

```javascript
// Tile texture 4x4
texture.repeat.set(4, 4);
texture.wrapS = THREE.RepeatWrapping;
texture.wrapT = THREE.RepeatWrapping;

// Offset (0-1 range)
texture.offset.set(0.5, 0.5);

// Rotation (radians, around center)
texture.rotation = Math.PI / 4;
texture.center.set(0.5, 0.5); // Rotation pivot
```

### Filtering

```javascript
// Minification (texture larger than screen pixels)
texture.minFilter = THREE.LinearMipmapLinearFilter; // Default, smooth
texture.minFilter = THREE.NearestFilter; // Pixelated
texture.minFilter = THREE.LinearFilter; // Smooth, no mipmaps

// Magnification (texture smaller than screen pixels)
texture.magFilter = THREE.LinearFilter; // Smooth (default)
texture.magFilter = THREE.NearestFilter; // Pixelated (retro ga

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- You need to load, configure, or optimize textures in Three.js. - The task involves UV mapping, texture settings, cubemaps, environment maps, or HDR texture workflows. - You are working on surface de

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Three.js Textures
- Para tarefas relacionadas a threejs textures

## Diretrizes Específicas

