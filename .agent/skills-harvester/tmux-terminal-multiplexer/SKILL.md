---
name: tmux-terminal-multiplexer
description: `tmux` keeps terminal sessions alive across SSH disconnects, splits work across multiple panes, and enables fully scriptable terminal automation. This skill covers session management, window/pane layo
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# tmux — Terminal Multiplexer

## Backstory

Você é um agente especializado em tmux — Terminal Multiplexer.

## Contexto Original da Skill
tmux — Terminal Multiplexer

## Instruções
---
name: tmux
description: "Expert tmux session, window, and pane management for terminal multiplexing, persistent remote workflows, and shell scripting automation."
category: development
risk: safe
source: community
date_added: "2026-03-28"
author: kostakost2
tags: [tmux, terminal, multiplexer, sessions, shell, remote, automation]
tools: [claude, cursor, gemini]
---

# tmux — Terminal Multiplexer

## Overview

`tmux` keeps terminal sessions alive across SSH disconnects, splits work across multiple panes, and enables fully scriptable terminal automation. This skill covers session management, window/pane layout, keybinding patterns, and using `tmux` non-interactively from shell scripts — essential for remote servers, long-running jobs, and automated workflows.

## When to Use This Skill

- Use when setting up or managing persistent terminal sessions on remote servers
- Use when the user needs to run long-running processes that survive SSH disconnects
- Use when scripting multi-pane terminal layouts (e.g., logs + shell + editor)
- Use when automating `tmux` commands from bash scripts without user interaction

## How It Works

`tmux` has three hierarchy levels: **sessions** (top level, survives disconnects), **windows** (tabs within a session), and **panes** (splits within a window). Everything is controllable from outside via `tmux <command>` or from inside via the prefix key (`Ctrl-b` by default).

### Session Management

```bash
# Create a new named session
tmux new-session -s work

# Create detached (background) session
tmux new-session -d -s work

# Create detached session and start a command
tmux new-session -d -s build -x 220 -y 50 "make all"

# Attach to a session
tmux attach -t work
tmux attach          # attaches to most recent session

# List all sessions
tmux list-sessions
tmux ls

# Detach from inside tmux
# Prefix + d   (Ctrl-b d)

# Kill a session
tmux kill-session -t work

# Kill all sessions except the current one
tmux kill-session -a

# Rename a session from outside
tmux rename-session -t old-name new-name

# Switch to another session from outside
tmux switch-client -t other-session

# Check if a session exists (useful in scripts)
tmux has-session -t work 2>/dev/null && echo "exists"
```

### Window Management

```bash
# Create a new window in the current session
tmux new-window -t work -n "logs"

# Create a window running a specific command
tmux new-window -t work:3 -n "server" "python -m http.server 8080"

# List windows
tmux list-windows -t work

# Select (switch to) a window
tmux select-window -t work:logs
tmux select-window -t work:2       # by index

# Rename a window
tmux rename-window -t work:2 "editor"

# Kill a window
tmux kill-window -t work:logs

# Move window to a new index
tmux move-window -s work:3 -t work:1

# From inside tmux:
# Prefix + c     — new window
# Prefix + ,     — rename window
# Prefix + &     — kill window
# Prefix + n/p   — next/previous window
# Prefix + 0-9   — switch to window by number
```

### P

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

`tmux` keeps terminal sessions alive across SSH disconnects, splits work across multiple panes, and enables fully scriptable terminal automation. This skill covers session management, window/pane layo

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em tmux — Terminal Multiplexer
- Para tarefas relacionadas a tmux terminal multiplexer

## Diretrizes Específicas

