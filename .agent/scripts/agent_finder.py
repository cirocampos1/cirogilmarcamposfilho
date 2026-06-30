#!/usr/bin/env python3
"""
Agent Finder - Sistema de busca inteligente de agentes/skills
Uso: python agent_finder.py [termo de busca]
"""
import sys
import yaml
from pathlib import Path
from typing import List, Dict, Any

AGENTS_DIR = Path("/home/leonardobarbosa/dev//.agent/agents")
SKILLS_DIR = Path("/home/leonardobarbosa/dev//.agent/skills")

def load_agent_metadata(agent_file: Path) -> Dict[str, Any]:
    """Extrai metadata de um arquivo de agente."""
    try:
        with open(agent_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extrai frontmatter YAML
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 2:
                metadata = yaml.safe_load(parts[1])
                return metadata or {}
        return {}
    except Exception:
        return {}

def search_agents(query: str) -> List[Dict[str, Any]]:
    """Busca agentes por termo."""
    query_lower = query.lower()
    results = []
    
    # Busca em arquivos de agentes
    for agent_file in AGENTS_DIR.glob("*.md"):
        name = agent_file.stem
        metadata = load_agent_metadata(agent_file)
        
        # Verifica match em nome, descrição ou skills
        description = metadata.get('description', '').lower()
        skills = ' '.join(metadata.get('skills', [])).lower()
        triggers = metadata.get('triggers', '').lower()
        
        if (query_lower in name.lower() or 
            query_lower in description or
            query_lower in skills or
            query_lower in triggers):
            
            results.append({
                'name': name,
                'description': metadata.get('description', 'Sem descrição'),
                'skills': metadata.get('skills', []),
                'file': str(agent_file.relative_to(AGENTS_DIR.parent))
            })
    
    return results

def get_stats() -> Dict[str, int]:
    """Retorna estatísticas do catálogo."""
    agents = list(AGENTS_DIR.glob("*.md"))
    skills = [d for d in SKILLS_DIR.iterdir() if d.is_dir()]
    
    return {
        'total_agents': len(agents),
        'total_skills': len(skills)
    }

def main():
    if len(sys.argv) < 2:
        print("=" * 60)
        print("🎯 AGENT FINDER - ")
        print("=" * 60)
        print("\nUso: python agent_finder.py [termo de busca]")
        print("\nExemplos:")
        print('  python agent_finder.py "nestjs"')
        print('  python agent_finder.py "database"')
        print('  python agent_finder.py "security"')
        print('  python agent_finder.py "react"')
        print("\nEstatísticas:")
        stats = get_stats()
        print(f"  📊 Total de Agentes: {stats['total_agents']}")
        print(f"  📚 Total de Skills: {stats['total_skills']}")
        print("=" * 60)
        return
    
    query = sys.argv[1]
    results = search_agents(query)
    
    print("=" * 60)
    print(f'🔍 Resultados para: "{query}"')
    print("=" * 60)
    
    if not results:
        print("\n❌ Nenhum agente encontrado.")
        print("\n💡 Dicas:")
        print("  - Tente termos mais genéricos (ex: 'api' em vez de 'fastapi')")
        print("  - Use palavras-chave de tecnologia (python, react, docker)")
        print("  - Busque por domínio (backend, frontend, security)")
    else:
        print(f"\n✅ {len(results)} agente(s) encontrado(s):\n")
        
        for i, agent in enumerate(results[:10], 1):
            print(f"{i}. 🎯 {agent['name']}")
            print(f"   📝 {agent['description'][:80]}...")
            if agent['skills']:
                print(f"   🔧 Skills: {', '.join(agent['skills'][:3])}")
            print()
        
        if len(results) > 10:
            print(f"... e mais {len(results) - 10} resultados")
        
        print("=" * 60)
        print("💡 Para ativar um agente, mencione-o no contexto:")
        print(f'   "Ative o agente {results[0]["name"]}"')
        print("=" * 60)

if __name__ == "__main__":
    main()
