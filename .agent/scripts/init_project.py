#!/usr/bin/env python3
"""
Init Project - Script para iniciar novos projetos no 
Uso: python init_project.py [nome-do-projeto]
"""
import sys
import shutil
from pathlib import Path
from datetime import datetime

TEMPLATES_DIR = Path("/home/leonardobarbosa/dev//templates/war-room")
PROJECTS_DIR = Path("/home/leonardobarbosa/dev//projects")

def create_project(project_name: str) -> Path:
    """Cria estrutura inicial do projeto."""
    
    # Cria diretório do projeto
    project_dir = PROJECTS_DIR / project_name
    war_room_dir = project_dir / "war-room"
    
    if project_dir.exists():
        print(f"❌ Erro: Projeto '{project_name}' já existe!")
        sys.exit(1)
    
    project_dir.mkdir(parents=True)
    war_room_dir.mkdir()
    
    # Copia templates
    for template_file in TEMPLATES_DIR.glob("*.md"):
        dest_file = war_room_dir / template_file.name
        shutil.copy(template_file, dest_file)
        
        # Substitui placeholders
        with open(dest_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace('[NOME_DO_PROJETO]', project_name)
        content = content.replace('[Nome do Projeto]', project_name.replace('-', ' ').title())
        content = content.replace('[DATA]', datetime.now().strftime('%Y-%m-%d'))
        
        with open(dest_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Cria README principal do projeto
    readme_content = f"""# {project_name.replace('-', ' ').title()}

> Projeto gerenciado pelo 

## 📁 Estrutura

```
.
├── war-room/          # Sala de guerra (SDD, TODO, DECISIONS, AGENTS)
├── src/               # Código fonte (a criar)
├── tests/             # Testes (a criar)
├── docs/              # Documentação (a criar)
├── pyproject.toml     # Config Python (a criar)
└── README.md          # Este arquivo
```

## 🚀 Início Rápido

1. **Leia a Sala de Guerra:**
   ```bash
   cd war-room/
   cat README.md
   ```

2. **Revise o SDD:**
   - Documento de especificação
   - Define o que será construído

3. **Acompanhe o TODO:**
   - Backlog de tarefas
   - Progresso do projeto

4. **Ative o Esquadrão:**
   ```markdown
   "@maestro-leo iniciar projeto {project_name}"
   ```

## 🎼 Comandos Úteis

| Comando | Descrição |
|---------|-----------|
| `"@maestro-leo status"` | Ver progresso |
| `"@maestro-leo próxima tarefa"` | Próxima tarefa |
| `"@maestro-leo [agente]"` | Ativar agente específico |

## 📋 Checklist de Início

- [ ] SDD.md revisado e aprovado
- [ ] TODO.md com tarefas definidas
- [ ] Esquadrão alocado (AGENTS.md)
- [ ] Setup inicial do projeto
- [ ] Primeira tarefa atribuída

---

*Projeto criado em: {datetime.now().strftime('%Y-%m-%d')}*
* v3.1*
"""
    
    with open(project_dir / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    return project_dir

def main():
    if len(sys.argv) < 2:
        print("=" * 60)
        print("🚀 INIT PROJECT - ")
        print("=" * 60)
        print("\nUso: python init_project.py [nome-do-projeto]")
        print("\nExemplos:")
        print('  python init_project.py "api-pagamentos"')
        print('  python init_project.py "dashboard-analytics"')
        print('  python init_project.py "microservico-auth"')
        print("=" * 60)
        return
    
    project_name = sys.argv[1].lower().replace(' ', '-')
    
    print("=" * 60)
    print(f"🚀 Iniciando Projeto: {project_name}")
    print("=" * 60)
    
    try:
        project_dir = create_project(project_name)
        
        print(f"\n✅ Projeto criado com sucesso!")
        print(f"\n📁 Local: {project_dir}")
        print(f"\n📋 Estrutura criada:")
        print(f"   ├── war-room/")
        print(f"   │   ├── README.md")
        print(f"   │   ├── SDD.md")
        print(f"   │   ├── TODO.md")
        print(f"   │   ├── DECISIONS.md")
        print(f"   │   └── AGENTS.md")
        print(f"   └── README.md")
        
        print(f"\n🎯 Próximos passos:")
        print(f"   1. cd {project_dir}/war-room")
        print(f"   2. Revise e complete o SDD.md")
        print(f"   3. Defina as tarefas no TODO.md")
        print(f"   4. Ative o esquadrão: '@maestro-leo iniciar projeto'")
        
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Erro ao criar projeto: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
