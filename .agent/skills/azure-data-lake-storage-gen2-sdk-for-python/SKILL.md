---
name: azure-data-lake-storage-gen2-sdk-for-python
description: Hierarchical file system for big data analytics workloads.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Azure Data Lake Storage Gen2 SDK for Python

## Backstory

Você é um agente especializado em Azure Data Lake Storage Gen2 SDK for Python.

## Contexto Original da Skill
Azure Data Lake Storage Gen2 SDK for Python

## Instruções
---
name: azure-storage-file-datalake-py
description: Azure Data Lake Storage Gen2 SDK for Python. Use for hierarchical file systems, big data analytics, and file/directory operations.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure Data Lake Storage Gen2 SDK for Python

Hierarchical file system for big data analytics workloads.

## Installation

```bash
pip install azure-storage-file-datalake azure-identity
```

## Environment Variables

```bash
AZURE_STORAGE_ACCOUNT_URL=https://<account>.dfs.core.windows.net
```

## Authentication

```python
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient

credential = DefaultAzureCredential()
account_url = "https://<account>.dfs.core.windows.net"

service_client = DataLakeServiceClient(account_url=account_url, credential=credential)
```

## Client Hierarchy

| Client | Purpose |
|--------|---------|
| `DataLakeServiceClient` | Account-level operations |
| `FileSystemClient` | Container (file system) operations |
| `DataLakeDirectoryClient` | Directory operations |
| `DataLakeFileClient` | File operations |

## File System Operations

```python
# Create file system (container)
file_system_client = service_client.create_file_system("myfilesystem")

# Get existing
file_system_client = service_client.get_file_system_client("myfilesystem")

# Delete
service_client.delete_file_system("myfilesystem")

# List file systems
for fs in service_client.list_file_systems():
    print(fs.name)
```

## Directory Operations

```python
file_system_client = service_client.get_file_system_client("myfilesystem")

# Create directory
directory_client = file_system_client.create_directory("mydir")

# Create nested directories
directory_client = file_system_client.create_directory("path/to/nested/dir")

# Get directory client
directory_client = file_system_client.get_directory_client("mydir")

# Delete directory
directory_client.delete_directory()

# Rename/move directory
directory_client.rename_directory(new_name="myfilesystem/newname")
```

## File Operations

### Upload File

```python
# Get file client
file_client = file_system_client.get_file_client("path/to/file.txt")

# Upload from local file
with open("local-file.txt", "rb") as data:
    file_client.upload_data(data, overwrite=True)

# Upload bytes
file_client.upload_data(b"Hello, Data Lake!", overwrite=True)

# Append data (for large files)
file_client.append_data(data=b"chunk1", offset=0, length=6)
file_client.append_data(data=b"chunk2", offset=6, length=6)
file_client.flush_data(12)  # Commit the data
```

### Download File

```python
file_client = file_system_client.get_file_client("path/to/file.txt")

# Download all content
download = file_client.download_file()
content = download.readall()

# Download to file
with open("downloaded.txt", "wb") as f:
    download = file_client.download_file()
    download.readinto(f)

# Download range
download = file_client.download_file(offset=0, length=10

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Hierarchical file system for big data analytics workloads.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Azure Data Lake Storage Gen2 SDK for Python
- Para tarefas relacionadas a azure data lake storage gen2 sdk for python

## Diretrizes Específicas

