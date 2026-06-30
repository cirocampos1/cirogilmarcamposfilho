---
name: libreoffice-base
description: LibreOffice Base skill for creating, managing, and automating database workflows using the native ODB (OpenDocument Database) format.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# LibreOffice Base

## Backstory

Você é um agente especializado em LibreOffice Base.

## Contexto Original da Skill
LibreOffice Base

## Instruções
---
name: base
description: "Database management, forms, reports, and data operations with LibreOffice Base."
category: database-processing
risk: safe
source: personal
date_added: "2026-02-27"
---

# LibreOffice Base

## Overview

LibreOffice Base skill for creating, managing, and automating database workflows using the native ODB (OpenDocument Database) format.

## When to Use This Skill

Use this skill when:
- Creating new databases in ODB format
- Connecting to external databases (MySQL, PostgreSQL, etc.)
- Automating database operations and reports
- Creating forms and reports
- Building database applications

## Core Capabilities

### 1. Database Creation
- Create new ODB databases from scratch
- Design tables, views, and relationships
- Create embedded HSQLDB/Firebird databases
- Connect to external databases

### 2. Data Operations
- Import data from CSV, spreadsheets
- Export data to various formats
- Query execution and management
- Batch data processing

### 3. Form and Report Automation
- Create data entry forms
- Design custom reports
- Automate report generation
- Build form templates

### 4. Query and SQL
- Visual query design
- SQL query execution
- Query optimization
- Result set manipulation

### 5. Integration
- Command-line automation
- Python scripting with UNO
- JDBC/ODBC connectivity

## Workflows

### Creating a New Database

#### Method 1: Command-Line
```bash
soffice --base
```

#### Method 2: Python with UNO
```python
import uno

def create_database():
    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_ctx
    )
    ctx = resolver.resolve(
        "uno:socket,host=localhost,port=8100;urp;StarOffice.ComponentContext"
    )
    smgr = ctx.ServiceManager
    doc = smgr.createInstanceWithContext("com.sun.star.sdb.DatabaseDocument", ctx)
    doc.storeToURL("file:///path/to/database.odb", ())
    doc.close(True)
```

### Connecting to External Database

```python
import uno

def connect_to_mysql(host, port, database, user, password):
    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_ctx
    )
    ctx = resolver.resolve(
        "uno:socket,host=localhost,port=8100;urp;StarOffice.ComponentContext"
    )
    smgr = ctx.ServiceManager
    
    doc = smgr.createInstanceWithContext("com.sun.star.sdb.DatabaseDocument", ctx)
    datasource = doc.getDataSource()
    datasource.URL = f"sdbc:mysql:jdbc:mysql://{host}:{port}/{database}"
    datasource.Properties["UserName"] = user
    datasource.Properties["Password"] = password
    
    doc.storeToURL("file:///path/to/connected.odb", ())
    return doc
```

## Database Connection Reference

### Supported Database Types
- HSQLDB (embedded)
- Firebird (embedded)
- MySQL/MariaDB
- PostgreSQL
- SQLite
- ODBC data sources
- JDBC data sources

### Connection Strings

```
# My

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

LibreOffice Base skill for creating, managing, and automating database workflows using the native ODB (OpenDocument Database) format.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em LibreOffice Base
- Para tarefas relacionadas a libreoffice base

## Diretrizes Específicas

