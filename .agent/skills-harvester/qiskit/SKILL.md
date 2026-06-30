---
name: qiskit
description: - You are building or optimizing quantum circuits with Qiskit for simulators or real hardware. - You need IBM Quantum-style tooling for transpilation, execution, visualization, or algorithm libraries.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Qiskit

## Backstory

Você é um agente especializado em Qiskit.

## Contexto Original da Skill
Qiskit

## Instruções
---
name: qiskit
description: "Qiskit is the world's most popular open-source quantum computing framework with 13M+ downloads. Build quantum circuits, optimize for hardware, execute on simulators or real quantum computers, and analyze results. Supports IBM Quantum (100+ qubit systems), IonQ, Amazon Braket, and other providers."
license: Apache-2.0 license
metadata:
    skill-author: K-Dense Inc.
risk: unknown
source: community
---

# Qiskit

## When to Use

- You are building or optimizing quantum circuits with Qiskit for simulators or real hardware.
- You need IBM Quantum-style tooling for transpilation, execution, visualization, or algorithm libraries.
- You want guidance on moving from a simple circuit prototype to backend-aware execution.

## Overview

Qiskit is the world's most popular open-source quantum computing framework with 13M+ downloads. Build quantum circuits, optimize for hardware, execute on simulators or real quantum computers, and analyze results. Supports IBM Quantum (100+ qubit systems), IonQ, Amazon Braket, and other providers.

**Key Features:**
- 83x faster transpilation than competitors
- 29% fewer two-qubit gates in optimized circuits
- Backend-agnostic execution (local simulators or cloud hardware)
- Comprehensive algorithm libraries for optimization, chemistry, and ML

## Quick Start

### Installation

```bash
uv pip install qiskit
uv pip install "qiskit[visualization]" matplotlib
```

### First Circuit

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Create Bell state (entangled qubits)
qc = QuantumCircuit(2)
qc.h(0)           # Hadamard on qubit 0
qc.cx(0, 1)       # CNOT from qubit 0 to 1
qc.measure_all()  # Measure both qubits

# Run locally
sampler = StatevectorSampler()
result = sampler.run([qc], shots=1024).result()
counts = result[0].data.meas.get_counts()
print(counts)  # {'00': ~512, '11': ~512}
```

### Visualization

```python
from qiskit.visualization import plot_histogram

qc.draw('mpl')           # Circuit diagram
plot_histogram(counts)   # Results histogram
```

## Core Capabilities

### 1. Setup and Installation
For detailed installation, authentication, and IBM Quantum account setup:
- **See `references/setup.md`**

Topics covered:
- Installation with uv
- Python environment setup
- IBM Quantum account and API token configuration
- Local vs. cloud execution

### 2. Building Quantum Circuits
For constructing quantum circuits with gates, measurements, and composition:
- **See `references/circuits.md`**

Topics covered:
- Creating circuits with QuantumCircuit
- Single-qubit gates (H, X, Y, Z, rotations, phase gates)
- Multi-qubit gates (CNOT, SWAP, Toffoli)
- Measurements and barriers
- Circuit composition and properties
- Parameterized circuits for variational algorithms

### 3. Primitives (Sampler and Estimator)
For executing quantum circuits and computing results:
- **See `references/primitives.md`**

Topics covered:
- **Sampler**: Get bitstring measureme

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- You are building or optimizing quantum circuits with Qiskit for simulators or real hardware. - You need IBM Quantum-style tooling for transpilation, execution, visualization, or algorithm libraries.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Qiskit
- Para tarefas relacionadas a qiskit

## Diretrizes Específicas

