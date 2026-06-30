# 🛡️ GUARDIA — Manual do Usuário

> Sistema privado de restore points para o .  
> **Localização**: `.agent/scripts/guardia/` (invisível — dentro do `.gitignore`)

---

## O que é?

O Guardia cria **fotos do estado dos módulos** usando Git tags locais. Se alguém quebrar algo, você consegue restaurar em segundos — sem precisar fazer `git revert` público ou avisar ninguém.

---

## Comandos

```bash
cd /home/leonardobarbosa/dev/

# Criar restore point ANTES de fazer alguma coisa arriscada
bash .agent/scripts/guardia/guardia.sh save stable

# Ver todos os restore points criados
bash .agent/scripts/guardia/guardia.sh list

# Ver o que mudou desde o último RP
bash .agent/scripts/guardia/guardia.sh diff

# Status rápido
bash .agent/scripts/guardia/guardia.sh status

# RESTAURAR (quando precisar de fato)
bash .agent/scripts/guardia/guardia.sh restore rp/20260414-120000-stable
```

---

## Fluxo Recomendado

### Antes de começar seu trabalho
```bash
# 1. Pull
git pull origin master

# 2. RP do estado pós-pull (baseline limpo)
bash .agent/scripts/guardia/guardia.sh save pos-pull
```

### Depois de implementar algo importante (ex: SinalSheet)
```bash
bash .agent/scripts/guardia/guardia.sh save sinalsheet-v1-ok
```

### Se os juniors quebrarem algo
```bash
# 1. Ver o que mudou
bash .agent/scripts/guardia/guardia.sh diff

# 2. Restaurar o módulo quebrado
bash .agent/scripts/guardia/guardia.sh restore rp/20260414-XXXXXX-sinalsheet-v1-ok
```

---

## Como funciona (por baixo)

- Cria **git tags locais** com prefixo `rp/` (ex: `rp/20260414-120000-stable`)
- As tags ficam **somente na sua máquina** (não fazem push automático)
- O restore usa `git checkout <tag> -- app/` para restaurar só os arquivos dos módulos
- Log de todas as operações em `.agent/scripts/guardia/.guardia.log`

---

## ⚠️ Importante

- As tags são locais — elas NÃO aparecem no GitLab para os outros devs
- Se você fizer `git push --tags`, as tags irão para o servidor (evite isso)
- Para restaurar um arquivo específico: `git checkout rp/XXXXXX -- app/routers/sinalsheet.py`

---

## Atalho (adicionar ao .bashrc da sua máquina)

```bash
# Guardia 
alias grd='bash /home/leonardobarbosa/dev//.agent/scripts/guardia/guardia.sh'

# Uso: grd save, grd list, grd diff, grd status
```
