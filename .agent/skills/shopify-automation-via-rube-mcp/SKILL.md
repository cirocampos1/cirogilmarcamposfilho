---
name: shopify-automation-via-rube-mcp
description: Automate Shopify operations through Composio's Shopify toolkit via Rube MCP.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Shopify Automation via Rube MCP

## Backstory

Você é um agente especializado em Shopify Automation via Rube MCP.

## Contexto Original da Skill
Shopify Automation via Rube MCP

## Instruções
---
name: shopify-automation
description: "Automate Shopify tasks via Rube MCP (Composio): products, orders, customers, inventory, collections. Always search tools first for current schemas."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Shopify Automation via Rube MCP

Automate Shopify operations through Composio's Shopify toolkit via Rube MCP.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Shopify connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `shopify`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.


1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `shopify`
3. If connection is not ACTIVE, follow the returned auth link to complete Shopify OAuth
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

### 1. Manage Products

**When to use**: User wants to list, search, create, or manage products

**Tool sequence**:
1. `SHOPIFY_GET_PRODUCTS` / `SHOPIFY_GET_PRODUCTS_PAGINATED` - List products [Optional]
2. `SHOPIFY_GET_PRODUCT` - Get single product details [Optional]
3. `SHOPIFY_BULK_CREATE_PRODUCTS` - Create products in bulk [Optional]
4. `SHOPIFY_GET_PRODUCTS_COUNT` - Get product count [Optional]

**Key parameters**:
- `product_id`: Product ID for single retrieval
- `title`: Product title
- `vendor`: Product vendor
- `status`: 'active', 'draft', or 'archived'

**Pitfalls**:
- Paginated results require cursor-based pagination for large catalogs
- Product variants are nested within the product object

### 2. Manage Orders

**When to use**: User wants to list, search, or inspect orders

**Tool sequence**:
1. `SHOPIFY_GET_ORDERS_WITH_FILTERS` - List orders with filters [Required]
2. `SHOPIFY_GET_ORDER` - Get single order details [Optional]
3. `SHOPIFY_GET_FULFILLMENT` - Get fulfillment details [Optional]
4. `SHOPIFY_GET_FULFILLMENT_EVENTS` - Track fulfillment events [Optional]

**Key parameters**:
- `status`: Order status filter ('any', 'open', 'closed', 'cancelled')
- `financial_status`: Payment status filter
- `fulfillment_status`: Fulfillment status filter
- `order_id`: Order ID for single retrieval
- `created_at_min`/`created_at_max`: Date range filters

**Pitfalls**:
- Order IDs are numeric; use string format for API calls
- Default order listing may not include all statuses; specify 'any' for all

### 3. Manage Customers

**When to use**: User wants to list or search customers

**Tool sequence**:
1. `SHOPIFY_GET_ALL_CUSTOMERS` - List all customers [Required]

**Key parameters**:
- `limit`: Number of customers per page
- `since_id`: Pagination cursor

**Pitfalls**:
- Customer data includes order count and total spent
- Large customer lists require pagination

### 4. Manage Collections

**When to u

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Automate Shopify operations through Composio's Shopify toolkit via Rube MCP.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Shopify Automation via Rube MCP
- Para tarefas relacionadas a shopify automation via rube mcp

## Diretrizes Específicas

