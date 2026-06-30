---
name: networkx
description: NetworkX is a Python package for creating, manipulating, and analyzing complex networks and graphs. Use this skill when working with network or graph data structures, including social networks, biolog
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# NetworkX

## Backstory

Você é um agente especializado em NetworkX.

## Contexto Original da Skill
NetworkX

## Instruções
---
name: networkx
description: "NetworkX is a Python package for creating, manipulating, and analyzing complex networks and graphs."
license: 3-clause BSD license
metadata:
    skill-author: K-Dense Inc.
risk: unknown
source: "https://github.com/networkx/networkx"
---

# NetworkX

## Overview

NetworkX is a Python package for creating, manipulating, and analyzing complex networks and graphs. Use this skill when working with network or graph data structures, including social networks, biological networks, transportation systems, citation networks, knowledge graphs, or any system involving relationships between entities.

## When to Use This Skill

Invoke this skill when tasks involve:

- **Creating graphs**: Building network structures from data, adding nodes and edges with attributes
- **Graph analysis**: Computing centrality measures, finding shortest paths, detecting communities, measuring clustering
- **Graph algorithms**: Running standard algorithms like Dijkstra's, PageRank, minimum spanning trees, maximum flow
- **Network generation**: Creating synthetic networks (random, scale-free, small-world models) for testing or simulation
- **Graph I/O**: Reading from or writing to various formats (edge lists, GraphML, JSON, CSV, adjacency matrices)
- **Visualization**: Drawing and customizing network visualizations with matplotlib or interactive libraries
- **Network comparison**: Checking isomorphism, computing graph metrics, analyzing structural properties

## Core Capabilities

### 1. Graph Creation and Manipulation

NetworkX supports four main graph types:
- **Graph**: Undirected graphs with single edges
- **DiGraph**: Directed graphs with one-way connections
- **MultiGraph**: Undirected graphs allowing multiple edges between nodes
- **MultiDiGraph**: Directed graphs with multiple edges

Create graphs by:
```python
import networkx as nx

# Create empty graph
G = nx.Graph()

# Add nodes (can be any hashable type)
G.add_node(1)
G.add_nodes_from([2, 3, 4])
G.add_node("protein_A", type='enzyme', weight=1.5)

# Add edges
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 4)])
G.add_edge(1, 4, weight=0.8, relation='interacts')
```

**Reference**: See `references/graph-basics.md` for comprehensive guidance on creating, modifying, examining, and managing graph structures, including working with attributes and subgraphs.

### 2. Graph Algorithms

NetworkX provides extensive algorithms for network analysis:

**Shortest Paths**:
```python
# Find shortest path
path = nx.shortest_path(G, source=1, target=5)
length = nx.shortest_path_length(G, source=1, target=5, weight='weight')
```

**Centrality Measures**:
```python
# Degree centrality
degree_cent = nx.degree_centrality(G)

# Betweenness centrality
betweenness = nx.betweenness_centrality(G)

# PageRank
pagerank = nx.pagerank(G)
```

**Community Detection**:
```python
from networkx.algorithms import community

# Detect communities
communities = community.greedy_modularity_communities(G)
```

**Connectivity**:


## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

NetworkX is a Python package for creating, manipulating, and analyzing complex networks and graphs. Use this skill when working with network or graph data structures, including social networks, biolog

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em NetworkX
- Para tarefas relacionadas a networkx

## Diretrizes Específicas

