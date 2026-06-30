# speckit-implement

Executa a implementação de uma feature seguindo as tarefas definidas, invocando as 3400+ skills do  conforme necessário.

---

## Quando usar

Use esta skill quando:
- O tasks.md está completo e aprovado
- Precisar implementar código seguindo a spec e o plano
- Quiser executar uma ou mais tarefas específicas
- Necessite invocar skills especializadas do catálogo

---

## Comando de Ativação

```
/speckit.implement [###-nome-da-feature] [opções]
```

Opções:
- `--task TXXX`: Implementar tarefa específica
- `--phase N`: Implementar todas as tarefas da fase N
- `--story USN`: Implementar todas as tarefas da user story N
- `--all`: Implementar todas as tarefas pendentes
- `--skill [nome]`: Usar skill específica do catálogo

Ou:

```
@ implementar [###-nome-da-feature] --task T001
```

---

## Pré-requisitos

- Arquivo `specs/###-nome-da-feature/tasks.md` deve existir
- Arquivo `specs/###-nome-da-feature/spec.md` deve existir
- Arquivo `specs/###-nome-da-feature/plan.md` deve existir
- Catálogo de skills disponível: `.agent/skills/INDEX.md`

---

## Fluxo de Trabalho

### 1. Ler contexto completo

```bash
# Documentos obrigatórios
cat specs/###-nome-da-feature/spec.md
cat specs/###-nome-da-feature/plan.md
cat specs/###-nome-da-feature/tasks.md

# Documentos de suporte
cat specs/###-nome-da-feature/data-model.md 2>/dev/null
cat specs/###-nome-da-feature/contracts/api-contracts.md 2>/dev/null
cat specs/###-nome-da-feature/constitution.md 2>/dev/null || cat .agent/templates/constitution-template.md
```

### 2. Identificar tarefas a executar

Baseado nos parâmetros:

| Parâmetro | Ação |
|-----------|------|
| `--task T001` | Executar apenas T001 |
| `--phase 1` | Executar todas as tarefas da Fase 1 |
| `--story US1` | Executar todas as tarefas da US1 |
| `--all` | Executar todas as tarefas pendentes |

### 3. Para cada tarefa, identificar e invocar skills

Cada tarefa em `tasks.md` tem uma **skill atribuída**. Para executar:

#### 3.1 Verificar a skill da tarefa

```markdown
- [ ] T012 [P] [US1] Criar modelo Contrato em `src/models/contrato.py`
  **Skill**: `database-design` + `sqlalchemy-patterns`
```

#### 3.2 Ler a skill do catálogo

```bash
# Ler skill
cat .agent/skills/database-design/SKILL.md
cat .agent/skills/sqlalchemy-patterns/SKILL.md
```

#### 3.3 Aplicar padrões da skill

Siga as instruções da skill para implementar a tarefa.

### 4. Verificar dependências

- Tarefas da Fase 2 precisam da Fase 1 completa
- Tarefas de implementação precisam de testes escritos primeiro
- Respeitar ordem: Setup → Fundacional → User Stories

### 5. Executar com qualidade

**Antes de escrever código**:
1. Verificar se é tarefa de teste → escrever teste que FALHA
2. Verificar se é tarefa de implementação → garantir que testes existem
3. **Ler a skill atribuída** para seguir padrões

**Ao escrever código**:
1. Seguir padrões da skill atribuída
2. Usar type hints completos
3. Adicionar docstrings
4. Seguir princípios da Constituição

**Após escrever código**:
1. Executar testes: `uv run pytest [arquivo]`
2. Verificar lint: `uv run ruff check [arquivo]`
3. Verificar types: `uv run mypy [arquivo]`

### 6. Gates de Qualidade

Antes de considerar uma tarefa completa, verificar:

```markdown
### Gate de Código
- [ ] Ruff passando
- [ ] MyPy passando (ou justificativa)
- [ ] Type hints completos
- [ ] Docstrings em funções públicas
- [ ] Segue padrões da skill atribuída

### Gate de Testes
- [ ] Testes escritos (se aplicável)
- [ ] Testes passando
- [ ] Cobertura mantida ou aumentada

### Gate de Segurança ⚠️
- [ ] Nenhuma escrita Sankhya sem validação
- [ ] Dados sensíveis não em logs
- [ ] Input validado
- [ ] Sem secrets no código
```

---

## Invocação de Skills

### Exemplo 1: Tarefa de Modelagem

**Tarefa**: T012 - Criar modelo Contrato

**Skill atribuída**: `database-design`

**Fluxo**:
```bash
# 1. Ler skill
cat .agent/skills/database-design/SKILL.md

# 2. Aplicar padrões da skill
# (seguir instruções do SKILL.md)

# 3. Implementar
# src/models/contrato.py
```

### Exemplo 2: Tarefa de API

**Tarefa**: T014 - Criar endpoint de consulta

**Skill atribuída**: `fastapi-router` + `api-patterns`

**Fluxo**:
```bash
# 1. Ler skills
cat .agent/skills/fastapi-router/SKILL.md
cat .agent/skills/api-patterns/SKILL.md

# 2. Aplicar padrões combinados

# 3. Implementar
# src/api/contratos.py
```

### Exemplo 3: Tarefa de Segurança

**Tarefa**: T020 - Adicionar validação de input

**Skill atribuída**: `input-validation-patterns` + `vulnerability-scanner`

**Fluxo**:
```bash
# 1. Ler skills
cat .agent/skills/input-validation-patterns/SKILL.md

# 2. Implementar validações

# 3. Scan de segurança
python .agent/scripts/sdd_checklist.py . --security-only
```

---

## Padrões de Implementação

### Estrutura de Arquivos

```python
# src/models/user.py
"""Modelo de usuário."""
# Skill: database-design, sqlalchemy-patterns

from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.db.base import Base


class User(Base):
    """Entidade de usuário do sistema."""
    
    __tablename__ = "users"
    
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
```

```python
# src/services/auth.py
"""Serviço de autenticação."""
# Skill: service-layer-patterns, authentication-patterns

from typing import Protocol
from src.models.user import User


class AuthService:
    """Serviço para operações de autenticação."""
    
    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo
    
    async def authenticate(self, email: str, password: str) -> User | None:
        """Autentica usuário por email e senha.
        
        Args:
            email: Email do usuário
            password: Senha em texto plano
            
        Returns:
            User se autenticado, None caso contrário
        """
        ...
```

```python
# src/api/auth.py
"""Rotas de autenticação."""
# Skill: fastapi-router, api-patterns

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    user_id: str
    token: str


@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest) -> LoginResponse:
    """Autentica usuário e retorna token."""
    ...
```

### Testes

```python
# tests/contract/test_auth.py
"""Testes de contrato para auth."""
# Skill: contract-testing

import pytest


class TestAuthContract:
    """Testes de contrato para endpoints de autenticação."""
    
    def test_login_contract(self, client: TestClient) -> None:
        """POST /auth/login deve seguir contrato."""
        response = client.post("/auth/login", json={
            "email": "test@example.com",
            "password": "secret"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert "user_id" in data
        assert "token" in data
```

---

## Checklist Final

Antes de finalizar implementação:

- [ ] Todas as tarefas solicitadas completas
- [ ] `tasks.md` atualizado com marcações
- [ ] Código commitado (mensagem descritiva)
- [ ] Tests passando: `uv run pytest`
- [ ] Lint passando: `uv run ruff check .`
- [ ] Type check: `uv run mypy .`
- [ ] Security scan: `python .agent/scripts/sdd_checklist.py .`
- [ ] **Skills aplicadas corretamente em cada tarefa**

---

## Comandos Úteis

```bash
# Buscar skill
ls .agent/skills/ | grep "[termo]"

# Ler skill
cat .agent/skills/[skill-name]/SKILL.md

# Ver índice
cat .agent/skills/INDEX.md | grep -A3 "[categoria]"

# Total de skills
ls .agent/skills/ | wc -l
```

---

## Próximos Passos

Após implementação:
1. Executar validação do `quickstart.md`
2. Revisar com usuário
3. Preparar para merge

---

*Skill v1.0 -  SDD*
