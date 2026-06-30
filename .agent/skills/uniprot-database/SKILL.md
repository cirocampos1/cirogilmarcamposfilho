---
name: uniprot-database
description: UniProt is the world's leading comprehensive protein sequence and functional information resource. Search proteins by name, gene, or accession, retrieve sequences in FASTA format, perform ID mapping a
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# UniProt Database

## Backstory

Você é um agente especializado em UniProt Database.

## Contexto Original da Skill
UniProt Database

## Instruções
---
name: uniprot-database
description: Direct REST API access to UniProt. Protein searches, FASTA retrieval, ID mapping, Swiss-Prot/TrEMBL. For Python workflows with multiple databases, prefer bioservices (unified interface to 40+ services). Use this for direct HTTP/REST work or UniProt-specific control.
license: Unknown
metadata:
    skill-author: K-Dense Inc.
risk: safe
source: community
---

# UniProt Database

## Overview

UniProt is the world's leading comprehensive protein sequence and functional information resource. Search proteins by name, gene, or accession, retrieve sequences in FASTA format, perform ID mapping across databases, access Swiss-Prot/TrEMBL annotations via REST API for protein analysis.

## When to Use This Skill

This skill should be used when:
- Searching for protein entries by name, gene symbol, accession, or organism
- Retrieving protein sequences in FASTA or other formats
- Mapping identifiers between UniProt and external databases (Ensembl, RefSeq, PDB, etc.)
- Accessing protein annotations including GO terms, domains, and functional descriptions
- Batch retrieving multiple protein entries efficiently
- Querying reviewed (Swiss-Prot) vs. unreviewed (TrEMBL) protein data
- Streaming large protein datasets
- Building custom queries with field-specific search syntax

## Core Capabilities

### 1. Searching for Proteins

Search UniProt using natural language queries or structured search syntax.

**Common search patterns:**
```python
# Search by protein name
query = "insulin AND organism_name:\"Homo sapiens\""

# Search by gene name
query = "gene:BRCA1 AND reviewed:true"

# Search by accession
query = "accession:P12345"

# Search by sequence length
query = "length:[100 TO 500]"

# Search by taxonomy
query = "taxonomy_id:9606"  # Human proteins

# Search by GO term
query = "go:0005515"  # Protein binding
```

Use the API search endpoint: `https://rest.uniprot.org/uniprotkb/search?query={query}&format={format}`

**Supported formats:** JSON, TSV, Excel, XML, FASTA, RDF, TXT

### 2. Retrieving Individual Protein Entries

Retrieve specific protein entries by accession number.

**Accession number formats:**
- Classic: P12345, Q1AAA9, O15530 (6 characters: letter + 5 alphanumeric)
- Extended: A0A022YWF9 (10 characters for newer entries)

**Retrieve endpoint:** `https://rest.uniprot.org/uniprotkb/{accession}.{format}`

Example: `https://rest.uniprot.org/uniprotkb/P12345.fasta`

### 3. Batch Retrieval and ID Mapping

Map protein identifiers between different database systems and retrieve multiple entries efficiently.

**ID Mapping workflow:**
1. Submit mapping job to: `https://rest.uniprot.org/idmapping/run`
2. Check job status: `https://rest.uniprot.org/idmapping/status/{jobId}`
3. Retrieve results: `https://rest.uniprot.org/idmapping/results/{jobId}`

**Supported databases for mapping:**
- UniProtKB AC/ID
- Gene names
- Ensembl, RefSeq, EMBL
- PDB, AlphaFoldDB
- KEGG, GO terms
- And many more (see `/references/id_mapping_databas

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

UniProt is the world's leading comprehensive protein sequence and functional information resource. Search proteins by name, gene, or accession, retrieve sequences in FASTA format, perform ID mapping a

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em UniProt Database
- Para tarefas relacionadas a uniprot database

## Diretrizes Específicas

