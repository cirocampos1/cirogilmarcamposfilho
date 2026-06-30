---
name: seaborn-statistical-visualization
description: - You need publication-quality statistical graphics directly from tabular datasets. - You are exploring multivariate relationships, distributions, or grouped comparisons with minimal plotting code. - 
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Seaborn Statistical Visualization

## Backstory

Você é um agente especializado em Seaborn Statistical Visualization.

## Contexto Original da Skill
Seaborn Statistical Visualization

## Instruções
---
name: seaborn
description: "Seaborn is a Python visualization library for creating publication-quality statistical graphics. Use this skill for dataset-oriented plotting, multivariate analysis, automatic statistical estimation, and complex multi-panel figures with minimal code."
license: BSD-3-Clause license
metadata:
    skill-author: K-Dense Inc.
risk: unknown
source: community
---

# Seaborn Statistical Visualization

## When to Use

- You need publication-quality statistical graphics directly from tabular datasets.
- You are exploring multivariate relationships, distributions, or grouped comparisons with minimal plotting code.
- You want seaborn's dataset-oriented API and statistical defaults on top of matplotlib.

## Overview

Seaborn is a Python visualization library for creating publication-quality statistical graphics. Use this skill for dataset-oriented plotting, multivariate analysis, automatic statistical estimation, and complex multi-panel figures with minimal code.

## Design Philosophy

Seaborn follows these core principles:

1. **Dataset-oriented**: Work directly with DataFrames and named variables rather than abstract coordinates
2. **Semantic mapping**: Automatically translate data values into visual properties (colors, sizes, styles)
3. **Statistical awareness**: Built-in aggregation, error estimation, and confidence intervals
4. **Aesthetic defaults**: Publication-ready themes and color palettes out of the box
5. **Matplotlib integration**: Full compatibility with matplotlib customization when needed

## Quick Start

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load example dataset
df = sns.load_dataset('tips')

# Create a simple visualization
sns.scatterplot(data=df, x='total_bill', y='tip', hue='day')
plt.show()
```

## Core Plotting Interfaces

### Function Interface (Traditional)

The function interface provides specialized plotting functions organized by visualization type. Each category has **axes-level** functions (plot to single axes) and **figure-level** functions (manage entire figure with faceting).

**When to use:**
- Quick exploratory analysis
- Single-purpose visualizations
- When you need a specific plot type

### Objects Interface (Modern)

The `seaborn.objects` interface provides a declarative, composable API similar to ggplot2. Build visualizations by chaining methods to specify data mappings, marks, transformations, and scales.

**When to use:**
- Complex layered visualizations
- When you need fine-grained control over transformations
- Building custom plot types
- Programmatic plot generation

```python
from seaborn import objects as so

# Declarative syntax
(
    so.Plot(data=df, x='total_bill', y='tip')
    .add(so.Dot(), color='day')
    .add(so.Line(), so.PolyFit())
)
```

## Plotting Functions by Category

### Relational Plots (Relationships Between Variables)

**Use for:** Exploring how two or more variables relate to each other

- `scatterplot()` - Display

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- You need publication-quality statistical graphics directly from tabular datasets. - You are exploring multivariate relationships, distributions, or grouped comparisons with minimal plotting code. - 

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Seaborn Statistical Visualization
- Para tarefas relacionadas a seaborn statistical visualization

## Diretrizes Específicas

