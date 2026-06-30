---
name: plotly
description: Python graphing library for creating interactive, publication-quality visualizations with 40+ chart types.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Plotly

## Backstory

Você é um agente especializado em Plotly.

## Contexto Original da Skill
Plotly

## Instruções
---
name: plotly
description: Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. Best for dashboards, exploratory analysis, and presentations. For static publication figures use matplotlib or scientific-visualization.
license: MIT license
metadata:
    skill-author: K-Dense Inc.
risk: unknown
source: community
---

# Plotly

Python graphing library for creating interactive, publication-quality visualizations with 40+ chart types.

## When to Use

- You need interactive charts with hover, zoom, pan, or web embedding.
- You are building dashboards, exploratory analysis notebooks, or presentations that benefit from rich interaction.
- You want to choose between Plotly Express and Graph Objects for the same visualization task.

## Quick Start

Install Plotly:
```bash
uv pip install plotly
```

Basic usage with Plotly Express (high-level API):
```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 11, 12, 13]
})

fig = px.scatter(df, x='x', y='y', title='My First Plot')
fig.show()
```

## Choosing Between APIs

### Use Plotly Express (px)
For quick, standard visualizations with sensible defaults:
- Working with pandas DataFrames
- Creating common chart types (scatter, line, bar, histogram, etc.)
- Need automatic color encoding and legends
- Want minimal code (1-5 lines)

See reference/plotly-express.md for complete guide.

### Use Graph Objects (go)
For fine-grained control and custom visualizations:
- Chart types not in Plotly Express (3D mesh, isosurface, complex financial charts)
- Building complex multi-trace figures from scratch
- Need precise control over individual components
- Creating specialized visualizations with custom shapes and annotations

See reference/graph-objects.md for complete guide.

**Note:** Plotly Express returns graph objects Figure, so you can combine approaches:
```python
fig = px.scatter(df, x='x', y='y')
fig.update_layout(title='Custom Title')  # Use go methods on px figure
fig.add_hline(y=10)                     # Add shapes
```

## Core Capabilities

### 1. Chart Types

Plotly supports 40+ chart types organized into categories:

**Basic Charts:** scatter, line, bar, pie, area, bubble

**Statistical Charts:** histogram, box plot, violin, distribution, error bars

**Scientific Charts:** heatmap, contour, ternary, image display

**Financial Charts:** candlestick, OHLC, waterfall, funnel, time series

**Maps:** scatter maps, choropleth, density maps (geographic visualization)

**3D Charts:** scatter3d, surface, mesh, cone, volume

**Specialized:** sunburst, treemap, sankey, parallel coordinates, gauge

For detailed examples and usage of all chart types, see reference/chart-types.md.

### 2. Layouts and Styling

**Subplots:** Create multi-plot figures with shared axes:
```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2, subplot_titles=('A', 'B'

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Python graphing library for creating interactive, publication-quality visualizations with 40+ chart types.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Plotly
- Para tarefas relacionadas a plotly

## Diretrizes Específicas

