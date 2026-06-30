---
name: threejs-interaction
description: - You need user interaction inside a Three.js scene. - The task involves raycasting, object picking, pointer handling, touch input, or camera controls. - You are building an interactive 3D experience 
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Three.js Interaction

## Backstory

Você é um agente especializado em Three.js Interaction.

## Contexto Original da Skill
Three.js Interaction

## Instruções
---
name: threejs-interaction
description: Three.js interaction - raycasting, controls, mouse/touch input, object selection. Use when handling user input, implementing click detection, adding camera controls, or creating interactive 3D experiences.
risk: unknown
source: community
---

# Three.js Interaction

## When to Use

- You need user interaction inside a Three.js scene.
- The task involves raycasting, object picking, pointer handling, touch input, or camera controls.
- You are building an interactive 3D experience rather than a passive render.

## Quick Start

```javascript
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

// Camera controls
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

// Raycasting for click detection
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

function onClick(event) {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(scene.children);

  if (intersects.length > 0) {
    console.log("Clicked:", intersects[0].object);
  }
}

window.addEventListener("click", onClick);
```

## Raycaster

### Basic Raycasting

```javascript
const raycaster = new THREE.Raycaster();

// From camera (mouse picking)
raycaster.setFromCamera(mousePosition, camera);

// From any origin and direction
raycaster.set(origin, direction); // origin: Vector3, direction: normalized Vector3

// Get intersections
const intersects = raycaster.intersectObjects(objects, recursive);

// intersects array contains:
// {
//   distance: number,          // Distance from ray origin
//   point: Vector3,            // Intersection point in world coords
//   face: Face3,               // Intersected face
//   faceIndex: number,         // Face index
//   object: Object3D,          // Intersected object
//   uv: Vector2,               // UV coordinates at intersection
//   uv1: Vector2,              // Second UV channel
//   normal: Vector3,           // Interpolated face normal
//   instanceId: number         // For InstancedMesh
// }
```

### Mouse Position Conversion

```javascript
const mouse = new THREE.Vector2();

function updateMouse(event) {
  // For full window
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
}

// For specific canvas element
function updateMouseCanvas(event, canvas) {
  const rect = canvas.getBoundingClientRect();
  mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
}
```

### Touch Support

```javascript
function onTouchStart(event) {
  event.preventDefault();

  if (event.touches.length === 1) {
    const touch = event.touches[0];
    mouse.x = (touch.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(touch.cl

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- You need user interaction inside a Three.js scene. - The task involves raycasting, object picking, pointer handling, touch input, or camera controls. - You are building an interactive 3D experience 

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Three.js Interaction
- Para tarefas relacionadas a threejs interaction

## Diretrizes Específicas

