---
name: threejs-lighting
description: - You need to add or tune lighting in a Three.js scene. - The task involves light types, shadows, environment lighting, or lighting performance tradeoffs. - You want to improve scene readability, real
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Three.js Lighting

## Backstory

Você é um agente especializado em Three.js Lighting.

## Contexto Original da Skill
Three.js Lighting

## Instruções
---
name: threejs-lighting
description: Three.js lighting - light types, shadows, environment lighting. Use when adding lights, configuring shadows, setting up IBL, or optimizing lighting performance.
risk: unknown
source: community
---

# Three.js Lighting

## When to Use

- You need to add or tune lighting in a Three.js scene.
- The task involves light types, shadows, environment lighting, or lighting performance tradeoffs.
- You want to improve scene readability, realism, or mood through Three.js lighting setup.

## Quick Start

```javascript
import * as THREE from "three";

// Basic lighting setup
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(5, 5, 5);
scene.add(directionalLight);
```

## Light Types Overview

| Light            | Description            | Shadow Support | Cost     |
| ---------------- | ---------------------- | -------------- | -------- |
| AmbientLight     | Uniform everywhere     | No             | Very Low |
| HemisphereLight  | Sky/ground gradient    | No             | Very Low |
| DirectionalLight | Parallel rays (sun)    | Yes            | Low      |
| PointLight       | Omnidirectional (bulb) | Yes            | Medium   |
| SpotLight        | Cone-shaped            | Yes            | Medium   |
| RectAreaLight    | Area light (window)    | No\*           | High     |

\*RectAreaLight shadows require custom solutions

## AmbientLight

Illuminates all objects equally. No direction, no shadows.

```javascript
// AmbientLight(color, intensity)
const ambient = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambient);

// Modify at runtime
ambient.color.set(0xffffcc);
ambient.intensity = 0.3;
```

## HemisphereLight

Gradient from sky to ground color. Good for outdoor scenes.

```javascript
// HemisphereLight(skyColor, groundColor, intensity)
const hemi = new THREE.HemisphereLight(0x87ceeb, 0x8b4513, 0.6);
hemi.position.set(0, 50, 0);
scene.add(hemi);

// Properties
hemi.color; // Sky color
hemi.groundColor; // Ground color
hemi.intensity;
```

## DirectionalLight

Parallel light rays. Simulates distant light source (sun).

```javascript
// DirectionalLight(color, intensity)
const dirLight = new THREE.DirectionalLight(0xffffff, 1);
dirLight.position.set(5, 10, 5);

// Light points at target (default: 0, 0, 0)
dirLight.target.position.set(0, 0, 0);
scene.add(dirLight.target);

scene.add(dirLight);
```

### DirectionalLight Shadows

```javascript
dirLight.castShadow = true;

// Shadow map size (higher = sharper, more expensive)
dirLight.shadow.mapSize.width = 2048;
dirLight.shadow.mapSize.height = 2048;

// Shadow camera (orthographic)
dirLight.shadow.camera.near = 0.5;
dirLight.shadow.camera.far = 50;
dirLight.shadow.camera.left = -10;
dirLight.shadow.camera.right = 10;
dirLight.shadow.camera.top = 10;
dirLight.shadow.camera.bottom = -10;

// Shadow softness
dirLight.shadow.radius = 4; // Bl

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- You need to add or tune lighting in a Three.js scene. - The task involves light types, shadows, environment lighting, or lighting performance tradeoffs. - You want to improve scene readability, real

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Three.js Lighting
- Para tarefas relacionadas a threejs lighting

## Diretrizes Específicas

