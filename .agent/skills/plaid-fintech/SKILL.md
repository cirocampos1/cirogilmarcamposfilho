---
name: plaid-fintech
description: Expert patterns for Plaid API integration including Link token flows, transactions sync, identity verification, Auth for ACH, balance checks, webhook handling, and fintech compliance best practices.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Plaid Fintech

## Backstory

Você é um agente especializado em Plaid Fintech.

## Contexto Original da Skill
Plaid Fintech

## Instruções
---
name: plaid-fintech
description: Expert patterns for Plaid API integration including Link token
  flows, transactions sync, identity verification, Auth for ACH, balance checks,
  webhook handling, and fintech compliance best practices.
risk: unknown
source: vibeship-spawner-skills (Apache 2.0)
date_added: 2026-02-27
---

# Plaid Fintech

Expert patterns for Plaid API integration including Link token flows,
transactions sync, identity verification, Auth for ACH, balance checks,
webhook handling, and fintech compliance best practices.

## Patterns

### Link Token Creation and Exchange

Create a link_token for Plaid Link, exchange public_token for access_token.
Link tokens are short-lived, one-time use. Access tokens don't expire but
may need updating when users change passwords.

// server.ts - Link token creation endpoint
import { Configuration, PlaidApi, PlaidEnvironments, Products, CountryCode } from 'plaid';

const configuration = new Configuration({
  basePath: PlaidEnvironments[process.env.PLAID_ENV || 'sandbox'],
  baseOptions: {
    headers: {
      'PLAID-CLIENT-ID': process.env.PLAID_CLIENT_ID,
      'PLAID-SECRET': process.env.PLAID_SECRET,
    },
  },
});

const plaidClient = new PlaidApi(configuration);

// Create link token for new user
app.post('/api/plaid/create-link-token', async (req, res) => {
  const { userId } = req.body;

  try {
    const response = await plaidClient.linkTokenCreate({
      user: {
        client_user_id: userId,  // Your internal user ID
      },
      client_name: 'My Finance App',
      products: [Products.Transactions],
      country_codes: [CountryCode.Us],
      language: 'en',
      webhook: 'https://yourapp.com/api/plaid/webhooks',
      // Request 180 days for recurring transactions
      transactions: {
        days_requested: 180,
      },
    });

    res.json({ link_token: response.data.link_token });
  } catch (error) {
    console.error('Link token creation failed:', error);
    res.status(500).json({ error: 'Failed to create link token' });
  }
});

// Exchange public token for access token
app.post('/api/plaid/exchange-token', async (req, res) => {
  const { publicToken, userId } = req.body;

  try {
    // Exchange for permanent access token
    const exchangeResponse = await plaidClient.itemPublicTokenExchange({
      public_token: publicToken,
    });

    const { access_token, item_id } = exchangeResponse.data;

    // Store securely - access_token doesn't expire!
    await db.plaidItem.create({
      data: {
        userId,
        itemId: item_id,
        accessToken: await encrypt(access_token),  // Encrypt at rest
        status: 'ACTIVE',
        products: ['transactions'],
      },
    });

    // Trigger initial transaction sync
    await initiateTransactionSync(item_id, access_token);

    res.json({ success: true, itemId: item_id });
  } catch (error) {
    console.error('Token exchange failed:', error);
    res.status(500).json({ error: 'Failed to exchange token' });
  }
});

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Expert patterns for Plaid API integration including Link token flows, transactions sync, identity verification, Auth for ACH, balance checks, webhook handling, and fintech compliance best practices.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Plaid Fintech
- Para tarefas relacionadas a plaid fintech

## Diretrizes Específicas

