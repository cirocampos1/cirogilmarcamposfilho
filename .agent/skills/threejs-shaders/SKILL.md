---
name: threejs-shaders
description: - You need custom shader logic in Three.js. - The task involves `ShaderMaterial`, uniforms, GLSL, vertex deformation, or fragment-based effects. - You are extending material behavior beyond what built
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Three.js Shaders

## Backstory

Você é um agente especializado em Three.js Shaders.

## Contexto Original da Skill
Three.js Shaders

## Instruções
---
name: threejs-shaders
description: Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. Use when creating custom visual effects, modifying vertices, writing fragment shaders, or extending built-in materials.
risk: unknown
source: community
---

# Three.js Shaders

## When to Use

- You need custom shader logic in Three.js.
- The task involves `ShaderMaterial`, uniforms, GLSL, vertex deformation, or fragment-based effects.
- You are extending material behavior beyond what built-in materials provide.

## Quick Start

```javascript
import * as THREE from "three";

const material = new THREE.ShaderMaterial({
  uniforms: {
    time: { value: 0 },
    color: { value: new THREE.Color(0xff0000) },
  },
  vertexShader: `
    void main() {
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
  fragmentShader: `
    uniform vec3 color;

    void main() {
      gl_FragColor = vec4(color, 1.0);
    }
  `,
});

// Update in animation loop
material.uniforms.time.value = clock.getElapsedTime();
```

## ShaderMaterial vs RawShaderMaterial

### ShaderMaterial

Three.js provides built-in uniforms and attributes.

```javascript
const material = new THREE.ShaderMaterial({
  vertexShader: `
    // Built-in uniforms available:
    // uniform mat4 modelMatrix;
    // uniform mat4 modelViewMatrix;
    // uniform mat4 projectionMatrix;
    // uniform mat4 viewMatrix;
    // uniform mat3 normalMatrix;
    // uniform vec3 cameraPosition;

    // Built-in attributes available:
    // attribute vec3 position;
    // attribute vec3 normal;
    // attribute vec2 uv;

    void main() {
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
  fragmentShader: `
    void main() {
      gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
    }
  `,
});
```

### RawShaderMaterial

Full control - you define everything.

```javascript
const material = new THREE.RawShaderMaterial({
  uniforms: {
    projectionMatrix: { value: camera.projectionMatrix },
    modelViewMatrix: { value: new THREE.Matrix4() },
  },
  vertexShader: `
    precision highp float;

    attribute vec3 position;
    uniform mat4 projectionMatrix;
    uniform mat4 modelViewMatrix;

    void main() {
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
  fragmentShader: `
    precision highp float;

    void main() {
      gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
    }
  `,
});
```

## Uniforms

### Uniform Types

```javascript
const material = new THREE.ShaderMaterial({
  uniforms: {
    // Numbers
    floatValue: { value: 1.5 },
    intValue: { value: 1 },

    // Vectors
    vec2Value: { value: new THREE.Vector2(1, 2) },
    vec3Value: { value: new THREE.Vector3(1, 2, 3) },
    vec4Value: { value: new THREE.Vector4(1, 2, 3, 4) },

    // Colors (converted to vec3)
    colorValue: { value: new THREE.Color(0xff0000) },

    // Matrices
    mat3Value: { value: new THREE.Matrix3() },
    mat4Value: { value: 

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- You need custom shader logic in Three.js. - The task involves `ShaderMaterial`, uniforms, GLSL, vertex deformation, or fragment-based effects. - You are extending material behavior beyond what built

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Three.js Shaders
- Para tarefas relacionadas a threejs shaders

## Diretrizes Específicas

