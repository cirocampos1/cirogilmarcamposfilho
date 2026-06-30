---
name: reddit-automation-via-rube-mcp
description: Automate Reddit operations through Composio's Reddit toolkit via Rube MCP.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Reddit Automation via Rube MCP

## Backstory

Você é um agente especializado em Reddit Automation via Rube MCP.

## Contexto Original da Skill
Reddit Automation via Rube MCP

## Instruções
---
name: reddit-automation
description: "Automate Reddit tasks via Rube MCP (Composio): search subreddits, create posts, manage comments, and browse top content. Always search tools first for current schemas."
risk: critical
source: community
date_added: "2026-02-27"
---

# Reddit Automation via Rube MCP

Automate Reddit operations through Composio's Reddit toolkit via Rube MCP.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Reddit connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `reddit`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.


1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `reddit`
3. If connection is not ACTIVE, follow the returned auth link to complete Reddit OAuth
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. Search Reddit

**When to use**: User wants to find posts across subreddits

**Tool sequence**:
1. `REDDIT_SEARCH_ACROSS_SUBREDDITS` - Search for posts matching a query [Required]

**Key parameters**:
- `query`: Search terms
- `subreddit`: Limit search to a specific subreddit (optional)
- `sort`: Sort results by 'relevance', 'hot', 'top', 'new', 'comments'
- `time_filter`: Time range ('hour', 'day', 'week', 'month', 'year', 'all')
- `limit`: Number of results to return

**Pitfalls**:
- Search results may not include very recent posts due to indexing delay
- The `time_filter` parameter only works with certain sort options
- Results are paginated; use after/before tokens for additional pages
- NSFW content may be filtered based on account settings

### 2. Create Posts

**When to use**: User wants to submit a new post to a subreddit

**Tool sequence**:
1. `REDDIT_LIST_SUBREDDIT_POST_FLAIRS` - Get available post flairs [Optional]
2. `REDDIT_CREATE_REDDIT_POST` - Submit the post [Required]

**Key parameters**:
- `subreddit`: Target subreddit name (without 'r/' prefix)
- `title`: Post title
- `text`: Post body text (for text posts)
- `url`: Link URL (for link posts)
- `flair_id`: Flair ID from the subreddit's flair list

**Pitfalls**:
- Some subreddits require flair; use LIST_SUBREDDIT_POST_FLAIRS first
- Subreddit posting rules vary widely; karma/age restrictions may apply
- Text and URL are mutually exclusive; a post is either text or link
- Rate limits apply; avoid rapid successive post creation
- The subreddit name should not include 'r/' prefix

### 3. Manage Comments

**When to use**: User wants to comment on posts or manage existing comments

**Tool sequence**:
1. `REDDIT_RETRIEVE_POST_COMMENTS` - Get comments on a post [Optional]
2. `REDDIT_POST_REDDIT_COMMENT` - Add a comment to a post or reply to a comment [Required]
3. `REDDIT_EDIT_REDDIT_COMMENT_OR_POST` - Edit an existing com

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate Reddit operations through Composio's Reddit toolkit via Rube MCP.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Reddit Automation via Rube MCP
- Para tarefas relacionadas a reddit automation via rube mcp

## Diretrizes Específicas

