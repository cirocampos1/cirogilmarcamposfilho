---
name: threejs-animation
description: - You need to animate objects, rigs, morph targets, or imported GLTF animations in Three.js. - The task involves mixers, clips, keyframes, procedural motion, or animation blending. - You are building 
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Three.js Animation

## Backstory

Você é um agente especializado em Three.js Animation.

## Contexto Original da Skill
Three.js Animation

## Instruções
---
name: threejs-animation
description: Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. Use when animating objects, playing GLTF animations, creating procedural motion, or blending animations.
risk: unknown
source: community
---

# Three.js Animation

## When to Use

- You need to animate objects, rigs, morph targets, or imported GLTF animations in Three.js.
- The task involves mixers, clips, keyframes, procedural motion, or animation blending.
- You are building motion behavior in a Three.js scene rather than just static rendering.

## Quick Start

```javascript
import * as THREE from "three";

// Simple procedural animation with Timer (recommended in r183)
const timer = new THREE.Timer();

renderer.setAnimationLoop(() => {
  timer.update();
  const delta = timer.getDelta();
  const elapsed = timer.getElapsed();

  mesh.rotation.y += delta;
  mesh.position.y = Math.sin(elapsed) * 0.5;

  renderer.render(scene, camera);
});
```

**Note:** `THREE.Timer` is recommended over `THREE.Clock` as of r183. Timer pauses when the page is hidden and has a cleaner API. `THREE.Clock` still works but is considered legacy.

## Animation System Overview

Three.js animation system has three main components:

1. **AnimationClip** - Container for keyframe data
2. **AnimationMixer** - Plays animations on a root object
3. **AnimationAction** - Controls playback of a clip

## AnimationClip

Stores keyframe animation data.

```javascript
// Create animation clip
const times = [0, 1, 2]; // Keyframe times (seconds)
const values = [0, 1, 0]; // Values at each keyframe

const track = new THREE.NumberKeyframeTrack(
  ".position[y]", // Property path
  times,
  values,
);

const clip = new THREE.AnimationClip("bounce", 2, [track]);
```

### KeyframeTrack Types

```javascript
// Number track (single value)
new THREE.NumberKeyframeTrack(".opacity", times, [1, 0]);
new THREE.NumberKeyframeTrack(".material.opacity", times, [1, 0]);

// Vector track (position, scale)
new THREE.VectorKeyframeTrack(".position", times, [
  0,
  0,
  0, // t=0
  1,
  2,
  0, // t=1
  0,
  0,
  0, // t=2
]);

// Quaternion track (rotation)
const q1 = new THREE.Quaternion().setFromEuler(new THREE.Euler(0, 0, 0));
const q2 = new THREE.Quaternion().setFromEuler(new THREE.Euler(0, Math.PI, 0));
new THREE.QuaternionKeyframeTrack(
  ".quaternion",
  [0, 1],
  [q1.x, q1.y, q1.z, q1.w, q2.x, q2.y, q2.z, q2.w],
);

// Color track
new THREE.ColorKeyframeTrack(".material.color", times, [
  1,
  0,
  0, // red
  0,
  1,
  0, // green
  0,
  0,
  1, // blue
]);

// Boolean track
new THREE.BooleanKeyframeTrack(".visible", [0, 0.5, 1], [true, false, true]);

// String track (for morph targets)
new THREE.StringKeyframeTrack(
  ".morphTargetInfluences[smile]",
  [0, 1],
  ["0", "1"],
);
```

### Interpolation Modes

```javascript
const track = new THREE.VectorKeyframeTrack(".position", times, values);

// Interpolation
track.setInterpolation(THREE.InterpolateLinear); // D

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- You need to animate objects, rigs, morph targets, or imported GLTF animations in Three.js. - The task involves mixers, clips, keyframes, procedural motion, or animation blending. - You are building 

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Three.js Animation
- Para tarefas relacionadas a threejs animation

## Diretrizes Específicas

