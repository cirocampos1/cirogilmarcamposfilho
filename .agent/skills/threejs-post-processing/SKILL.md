---
name: threejs-post-processing
description: - You need screen-space visual effects in a Three.js render pipeline. - The task involves `EffectComposer`, bloom, depth of field, color grading, blur, or custom passes. - You are enhancing the final 
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Three.js Post-Processing

## Backstory

Você é um agente especializado em Three.js Post-Processing.

## Contexto Original da Skill
Three.js Post-Processing

## Instruções
---
name: threejs-postprocessing
description: Three.js post-processing - EffectComposer, bloom, DOF, screen effects. Use when adding visual effects, color grading, blur, glow, or creating custom screen-space shaders.
risk: unknown
source: community
---

# Three.js Post-Processing

## When to Use

- You need screen-space visual effects in a Three.js render pipeline.
- The task involves `EffectComposer`, bloom, depth of field, color grading, blur, or custom passes.
- You are enhancing the final rendered image rather than base scene setup alone.

## Quick Start

```javascript
import * as THREE from "three";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";

// Setup composer
const composer = new EffectComposer(renderer);

// Render scene
const renderPass = new RenderPass(scene, camera);
composer.addPass(renderPass);

// Add bloom
const bloomPass = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  1.5, // strength
  0.4, // radius
  0.85, // threshold
);
composer.addPass(bloomPass);

// Animation loop - use composer instead of renderer
function animate() {
  requestAnimationFrame(animate);
  composer.render(); // NOT renderer.render()
}
```

## EffectComposer Setup

```javascript
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";

const composer = new EffectComposer(renderer);

// First pass: render scene
const renderPass = new RenderPass(scene, camera);
composer.addPass(renderPass);

// Add more passes...
composer.addPass(effectPass);

// Last pass should render to screen
effectPass.renderToScreen = true; // Default for last pass

// Handle resize
function onResize() {
  const width = window.innerWidth;
  const height = window.innerHeight;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();

  renderer.setSize(width, height);
  composer.setSize(width, height);
}
```

## Common Effects

### Bloom (Glow)

```javascript
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";

const bloomPass = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  1.5, // strength - intensity of glow
  0.4, // radius - spread of glow
  0.85, // threshold - brightness threshold
);

composer.addPass(bloomPass);

// Adjust at runtime
bloomPass.strength = 2.0;
bloomPass.threshold = 0.5;
bloomPass.radius = 0.8;
```

### Selective Bloom

Apply bloom only to specific objects.

```javascript
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { ShaderPass } from "three/addons/postprocessing/ShaderPass.js";

// Layer setup
const BLOOM_LAYER = 1;
const bloomLayer = new THREE.Layers();
bloomLayer.set(BLOOM_LAYER);

// Mark objects to bloom
glowingMesh.layers.en

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- You need screen-space visual effects in a Three.js render pipeline. - The task involves `EffectComposer`, bloom, depth of field, color grading, blur, or custom passes. - You are enhancing the final 

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Three.js Post-Processing
- Para tarefas relacionadas a threejs post processing

## Diretrizes Específicas

