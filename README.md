# Crypto Assistant — Beginner's Cryptocurrency Website

A guide for building a beginner-friendly website that explains everything a newcomer needs to know about cryptocurrency — from what it is to how to use it.

---

## Project Overview

This website targets people with zero prior knowledge of cryptocurrency. It is structured as five progressive sections, each building on the last, so a complete beginner can go from "what is Bitcoin?" to confidently buying, mining, and spending crypto.

---

## Site Structure

### 1. What Is Crypto & How Does It Work

**Goal:** Demystify the core concepts without technical jargon.

**Topics to cover:**
- What a cryptocurrency is (digital money with no central authority)
- What a blockchain is — explain it as a shared, tamper-proof ledger
- What a wallet is and what public/private keys mean in plain English
- Why crypto is decentralized and why that matters
- Consensus mechanisms: explain Proof of Work vs Proof of Stake simply
- Common terminology glossary: block, transaction, hash, gas fee, node

**Suggested UI approach:**
- Use animated diagrams to show how a transaction travels through the network
- Step-by-step "how a transaction works" visual walkthrough
- A glossary tooltip system so users can hover unfamiliar terms inline

**Data sources:**
- Static educational content (no live data needed)
- CoinMarketCap Learn, Investopedia, or Bitcoin.org for reference material

---

### 2. What Cryptocurrencies Exist

**Goal:** Show users the full landscape of coins and tokens with live data.

**Topics to cover:**
- Difference between coins (native to their blockchain) and tokens (built on top)
- Categories: Layer 1s, stablecoins, DeFi tokens, memecoins, utility tokens
- How to read a crypto listing: market cap, volume, circulating supply, price

**How to fetch the live list:**

Use the [CoinGecko API](https://www.coingecko.com/en/api) — it is free for up to 10,000 calls/month with no API key required for basic endpoints.

```
GET https://api.coingecko.com/api/v3/coins/markets
  ?vs_currency=usd
  &order=market_cap_desc
  &per_page=100
  &page=1
  &sparkline=false
```

Returns: name, symbol, current price, market cap, 24h change, image, and more.

Alternative free APIs:
- **CoinMarketCap API** (free tier, requires API key): `https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest`
- **Binance Public API** (no key needed for market data): `https://api.binance.com/api/v3/ticker/24hr`
- **Kraken REST API**: `https://api.kraken.com/0/public/Assets`

**Suggested UI approach:**
- Paginated table or card grid with search and filter by category
- Price sparkline charts using Chart.js or Recharts
- "Coin detail" modal/page with a deeper breakdown per asset

---

### 3. How to Mine Certain Cryptocurrencies

**Goal:** Explain what mining is and give practical, hardware-specific guidance per coin.

**Topics to cover:**
- What mining is: solving puzzles to validate transactions and earn rewards
- Why not all coins can be mined (PoS coins like Ethereum post-Merge cannot be mined)
- Hardware types: CPU mining, GPU mining, ASIC mining — pros, cons, and cost
- Mining pools vs solo mining — explain why pools dominate
- Key metrics to understand: hashrate, difficulty, block reward, mining profitability

**Mineable coins to highlight (as of 2025):**

| Coin | Algorithm | Best Hardware |
|------|-----------|---------------|
| Bitcoin (BTC) | SHA-256 | ASIC (e.g., Antminer S21) |
| Litecoin (LTC) | Scrypt | ASIC (e.g., Antminer L9) |
| Monero (XMR) | RandomX | CPU (intentionally ASIC-resistant) |
| Ravencoin (RVN) | KawPow | GPU |
| Ergo (ERG) | Autolykos v2 | GPU |
| Kaspa (KAS) | kHeavyHash | ASIC / GPU |

**Profitability calculators to link:**
- [WhatToMine](https://whattomine.com) — enter your GPU/CPU and electricity cost to see daily profit
- [NiceHash Calculator](https://www.nicehash.com/profitability-calculator)
- [CoinWarz](https://www.coinwarz.com)

**Software to mention per coin:**
- XMRig (Monero CPU mining)
- NiceHash QuickMiner (beginner-friendly GPU mining)
- CGMiner / BFGMiner (Bitcoin ASIC)
- T-Rex Miner, lolMiner (GPU, multiple coins)

**Suggested UI approach:**
- Interactive "pick your hardware" selector that filters the coin table
- Embed or link to WhatToMine with pre-filled parameters
- Step-by-step setup guide per coin with OS-specific instructions (Windows / Linux)

---

### 4. How to Buy Certain Cryptocurrencies

**Goal:** Walk a complete beginner through the safest path from fiat to crypto.

**Topics to cover:**
- Centralized exchanges (CEX) vs decentralized exchanges (DEX) — when to use each
- KYC/AML: why exchanges ask for ID, what to expect
- Order types: market order, limit order, stop-loss
- How to read an order book
- Custody: keeping crypto on an exchange vs moving it to your own wallet
- Security basics: 2FA, phishing awareness, never share your seed phrase

**Major exchanges to cover:**

| Exchange | Best for | Fiat on-ramp | Notable feature |
|----------|----------|-------------|-----------------|
| Coinbase | Absolute beginners | Yes (bank, card) | Very simple UI |
| Kraken | Intermediate users | Yes | Low fees, strong security |
| Binance | All levels | Yes | Largest coin selection |
| Uniswap | DeFi / no KYC | No (crypto only) | DEX, non-custodial |
| Robinhood Crypto | US beginners | Yes | No wallet withdrawal (limited) |

**Step-by-step buying flow to document:**
1. Create account and verify identity (CEX)
2. Deposit fiat via bank transfer or card
3. Search for the coin and choose an order type
4. Confirm purchase and note the transaction fee
5. (Optional) Withdraw to a personal wallet

**Wallet recommendations to include:**
- **Hot wallets (software):** MetaMask (Ethereum/EVM), Exodus (multi-chain), Trust Wallet
- **Cold wallets (hardware):** Ledger Nano X, Trezor Model T — recommended for amounts above ~$500

**Suggested UI approach:**
- Exchange comparison table with filters (beginner-friendly, fees, supported countries)
- Illustrated flow diagram of the buy process
- Security checklist component users can check off

---

### 5. How to Spend Certain Cryptocurrencies

**Goal:** Show users that crypto is a usable currency, not just speculation.

**Topics to cover:**
- Direct payments: merchants and services that accept crypto natively
- Crypto debit cards: convert crypto to fiat at point of sale automatically
- Peer-to-peer transfers: sending crypto to friends and family
- DeFi use cases: lending, borrowing, earning yield
- NFTs and digital purchases
- Tax implications: spending crypto is a taxable event in most jurisdictions — always check local law

**Ways to spend crypto to cover:**

| Method | How it works | Coins accepted |
|--------|-------------|----------------|
| Crypto debit cards | Converts to fiat at checkout | BTC, ETH, many others |
| BitPay merchants | Direct crypto checkout | BTC, ETH, stablecoins |
| Coinbase Commerce | Merchant checkout plugin | Multi-coin |
| Lightning Network | Instant, near-zero fee BTC payments | BTC |
| Stablecoin transfers | Send USDC/USDT like a bank transfer | USDC, USDT, DAI |
| Gift card platforms | Buy gift cards with crypto | BTC, ETH, LTC |

**Crypto debit cards to highlight:**
- Coinbase Card (Visa, US/EU)
- Crypto.com Visa Card (tiered rewards)
- Bitpay Card (US)
- Binance Visa Card (EU)

**Places that accept Bitcoin directly (as of 2025):**
- Newegg, Overstock, Shopify stores (via BitPay plugin)
- Microsoft (Xbox/Windows store credits)
- Whole Foods, Nordstrom (via Flexa/SPEDN)
- Many local businesses — use [Coinmap](https://coinmap.org) to find them

**Suggested UI approach:**
- Interactive map (embed Coinmap) showing local merchants
- Filterable "spend" directory by category (food, tech, travel, online)
- Step-by-step guide for setting up a crypto debit card

---

## Tech Stack

### Full Stack Overview

```
┌─────────────────────────────────────────────────────┐
│                    Browser                          │
│         React 19 + Next.js 15 (App Router)          │
│     Tailwind CSS v4 + shadcn/ui + Framer Motion     │
└────────────────────┬────────────────────────────────┘
                     │ HTTPS / JSON
┌────────────────────▼────────────────────────────────┐
│               FastAPI (Python 3.12)                 │
│    Pydantic v2 · SQLAlchemy 2 (async) · Alembic     │
│    APScheduler — background price sync jobs         │
└────────────────────┬────────────────────────────────┘
                     │ asyncpg
┌────────────────────▼────────────────────────────────┐
│              PostgreSQL 16                          │
│    TimescaleDB extension for price time-series      │
└─────────────────────────────────────────────────────┘
          │                          │
  Redis 7 (cache/rate-limit)   CoinGecko API (external)
```

---

### Frontend

| Concern | Library / Version | Notes |
|---------|------------------|-------|
| Framework | **Next.js 15** (App Router) | Server Components by default; Client Components only where interactivity needed |
| Language | **TypeScript 5** | Strict mode enabled |
| Styling | **Tailwind CSS v4** | CSS-first config, no `tailwind.config.js` needed |
| Component library | **shadcn/ui** | Copy-paste components built on Radix UI primitives |
| Animation | **Framer Motion 11** | Page transitions, animated diagrams in Section 1 |
| Charts | **Recharts 2** | Coin price sparklines and mining profitability graphs |
| Data fetching | **TanStack Query v5** | Server-state management, automatic cache invalidation |
| Forms | **React Hook Form 7 + Zod** | Used in mining calculator and search/filter forms |
| Map | **React-Leaflet 4** | Merchant map in Section 5 |
| Icons | **Lucide React** | Consistent icon set |
| State | **Zustand 5** | Lightweight global state (selected coin, user preferences) |

**Key React patterns used:**

- Server Components fetch data directly from the FastAPI backend at build/request time (no client waterfall)
- `use()` hook with Suspense boundaries for streaming per-section content
- Route groups `(marketing)` vs `(app)` to separate public pages from data-heavy views
- Parallel routes for coin detail side panels without full-page navigation

---

### Backend — FastAPI

**Python version:** 3.12 (use `pyenv` or `.python-version` file to pin)

**Core packages:**

```toml
# pyproject.toml (managed with uv)
[project]
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.115",
    "uvicorn[standard]>=0.32",
    "pydantic>=2.9",
    "pydantic-settings>=2.6",
    "sqlalchemy>=2.0",
    "asyncpg>=0.30",
    "alembic>=1.14",
    "httpx>=0.28",          # async HTTP client for CoinGecko
    "redis>=5.2",           # cache + rate limiting
    "apscheduler>=3.10",    # background sync jobs
    "python-jose[cryptography]>=3.3",  # JWT auth
    "passlib[bcrypt]>=1.7",
    "python-multipart>=0.0.12",
]
```

**Project layout:**

```
backend/
├── app/
│   ├── main.py                  # FastAPI app factory, lifespan hooks
│   ├── config.py                # Pydantic Settings (reads .env)
│   ├── database.py              # Async SQLAlchemy engine + session
│   ├── models/                  # SQLAlchemy ORM models
│   │   ├── coin.py
│   │   ├── price_tick.py        # TimescaleDB hypertable
│   │   ├── exchange.py
│   │   └── user.py
│   ├── schemas/                 # Pydantic v2 request/response schemas
│   │   ├── coin.py
│   │   ├── price.py
│   │   └── user.py
│   ├── routers/                 # One router per domain
│   │   ├── coins.py             # GET /coins, GET /coins/{id}
│   │   ├── prices.py            # GET /prices/{coin_id}/history
│   │   ├── mining.py            # GET /mining/coins, POST /mining/estimate
│   │   ├── exchanges.py         # GET /exchanges
│   │   └── auth.py              # POST /auth/register, /auth/token
│   ├── services/
│   │   ├── coingecko.py         # Async CoinGecko API client (httpx)
│   │   └── price_sync.py        # APScheduler job — syncs prices every 5 min
│   └── core/
│       ├── security.py          # JWT helpers
│       └── cache.py             # Redis helpers
├── alembic/                     # DB migrations
│   ├── env.py
│   └── versions/
├── tests/
│   ├── conftest.py              # pytest-asyncio fixtures, test DB
│   └── routers/
│       ├── test_coins.py
│       └── test_mining.py
├── pyproject.toml
└── Dockerfile
```

**Example router — `routers/coins.py`:**

```python
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.schemas.coin import CoinListResponse, CoinDetail
from app.services import coingecko

router = APIRouter(prefix="/coins", tags=["coins"])

@router.get("/", response_model=CoinListResponse)
async def list_coins(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, le=250),
    category: str | None = None,
    session: AsyncSession = Depends(get_session),
):
    return await coingecko.fetch_markets(page=page, per_page=per_page, category=category)

@router.get("/{coin_id}", response_model=CoinDetail)
async def get_coin(coin_id: str, session: AsyncSession = Depends(get_session)):
    return await coingecko.fetch_coin_detail(coin_id)
```

**API versioning:** all routes live under `/api/v1/` prefix — set in `main.py` via `root_path` or an `APIRouter` prefix.

**OpenAPI docs** are auto-generated by FastAPI and available at `/docs` (Swagger UI) and `/redoc`.

---

### Database — PostgreSQL 16

**Extensions to enable:**
```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";    -- UUID primary keys
CREATE EXTENSION IF NOT EXISTS timescaledb;    -- time-series for price data
CREATE EXTENSION IF NOT EXISTS pg_trgm;        -- fuzzy search on coin names
```

**Core schema:**

```sql
-- Coins master table
CREATE TABLE coins (
    id          TEXT PRIMARY KEY,              -- coingecko slug e.g. "bitcoin"
    symbol      TEXT NOT NULL,
    name        TEXT NOT NULL,
    category    TEXT,
    is_mineable BOOLEAN DEFAULT FALSE,
    algorithm   TEXT,
    image_url   TEXT,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX coins_name_trgm ON coins USING GIN (name gin_trgm_ops);

-- Price ticks — converted to a TimescaleDB hypertable
CREATE TABLE price_ticks (
    coin_id     TEXT        NOT NULL REFERENCES coins(id),
    recorded_at TIMESTAMPTZ NOT NULL,
    price_usd   NUMERIC(20, 8),
    market_cap  BIGINT,
    volume_24h  BIGINT,
    change_24h  NUMERIC(8, 4)
);
SELECT create_hypertable('price_ticks', 'recorded_at');
CREATE INDEX ON price_ticks (coin_id, recorded_at DESC);

-- Continuous aggregate: hourly OHLCV
CREATE MATERIALIZED VIEW price_hourly
WITH (timescaledb.continuous) AS
SELECT
    coin_id,
    time_bucket('1 hour', recorded_at) AS bucket,
    first(price_usd, recorded_at) AS open,
    max(price_usd)                AS high,
    min(price_usd)                AS low,
    last(price_usd, recorded_at)  AS close,
    sum(volume_24h)               AS volume
FROM price_ticks
GROUP BY coin_id, bucket;

-- Exchanges
CREATE TABLE exchanges (
    id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name            TEXT NOT NULL,
    url             TEXT,
    has_fiat_onramp BOOLEAN,
    kyc_required    BOOLEAN,
    supported_coins TEXT[],
    fee_pct         NUMERIC(5, 4)
);

-- Users (optional — for saved watchlists)
CREATE TABLE users (
    id           UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email        TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at   TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE watchlist (
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    coin_id TEXT REFERENCES coins(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, coin_id)
);
```

**Migrations** are managed with Alembic. Each schema change gets its own versioned file:
```bash
alembic revision --autogenerate -m "add watchlist table"
alembic upgrade head
```

---

### Background Jobs — APScheduler

A scheduler runs inside the FastAPI process (no separate worker needed for this scale):

```python
# app/services/price_sync.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

@scheduler.scheduled_job("interval", minutes=5)
async def sync_top_coins():
    coins = await coingecko.fetch_markets(per_page=250)
    async with get_session() as session:
        # upsert price_ticks rows
        ...
```

For heavier workloads, replace APScheduler with **Celery + Redis** or a dedicated **pg_cron** job.

---

### Caching — Redis 7

| What | Strategy | TTL |
|------|----------|-----|
| `/coins` market list | Cache-aside | 5 min |
| `/coins/{id}` detail | Cache-aside | 5 min |
| `/prices/{id}/history` | Cache-aside | 1 hour |
| Rate limiting (CoinGecko) | Sliding window counter | 1 min |

```python
# app/core/cache.py
import redis.asyncio as redis
import json

_client: redis.Redis | None = None

async def get(key: str):
    raw = await _client.get(key)
    return json.loads(raw) if raw else None

async def set(key: str, value, ttl: int):
    await _client.setex(key, ttl, json.dumps(value))
```

---

### Project Folder Structure (Full)

```
crypto-website/
├── frontend/                         # Next.js 15
│   ├── src/
│   │   ├── app/
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx              # Landing
│   │   │   ├── what-is-crypto/
│   │   │   │   └── page.tsx
│   │   │   ├── explore-coins/
│   │   │   │   ├── page.tsx          # Server Component — fetches coin list
│   │   │   │   └── [id]/page.tsx     # Coin detail
│   │   │   ├── mining/
│   │   │   │   └── page.tsx
│   │   │   ├── how-to-buy/
│   │   │   │   └── page.tsx
│   │   │   └── how-to-spend/
│   │   │       └── page.tsx
│   │   ├── components/
│   │   │   ├── ui/                   # shadcn/ui generated components
│   │   │   ├── CoinTable.tsx
│   │   │   ├── PriceChart.tsx
│   │   │   ├── MiningCalculator.tsx
│   │   │   ├── ExchangeComparison.tsx
│   │   │   ├── MerchantMap.tsx
│   │   │   └── GlossaryTooltip.tsx
│   │   ├── lib/
│   │   │   ├── api.ts                # Typed fetch wrappers → FastAPI
│   │   │   └── queryClient.ts        # TanStack Query setup
│   │   └── store/
│   │       └── useAppStore.ts        # Zustand store
│   ├── public/
│   │   └── diagrams/
│   ├── package.json
│   └── next.config.ts
│
├── backend/                          # FastAPI
│   ├── app/  (see layout above)
│   ├── alembic/
│   ├── tests/
│   ├── pyproject.toml
│   └── Dockerfile
│
├── docker-compose.yml                # postgres + redis + backend + frontend
└── .env.example
```

---

### Docker Compose (local dev)

```yaml
# docker-compose.yml
services:
  db:
    image: timescale/timescaledb:latest-pg16
    environment:
      POSTGRES_DB: crypto_assistant
      POSTGRES_USER: crypto
      POSTGRES_PASSWORD: secret
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  backend:
    build: ./backend
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    environment:
      DATABASE_URL: postgresql+asyncpg://crypto:secret@db:5432/crypto_assistant
      REDIS_URL: redis://redis:6379
      COINGECKO_API_KEY: ${COINGECKO_API_KEY}
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis

  frontend:
    build: ./frontend
    command: npm run dev
    environment:
      NEXT_PUBLIC_API_URL: http://localhost:8000/api/v1
    ports:
      - "3000:3000"
    depends_on:
      - backend

volumes:
  pgdata:
```

---

### Getting Started

**Prerequisites:** Docker Desktop, Node.js 22 LTS, Python 3.12, `uv` (Python package manager)

```bash
# 1. Clone and copy env
git clone https://github.com/yourname/crypto-website
cd crypto-website
cp .env.example .env          # fill in COINGECKO_API_KEY

# 2. Start Postgres + Redis
docker compose up db redis -d

# 3. Backend
cd backend
uv sync                        # installs all deps from pyproject.toml
alembic upgrade head           # run all migrations
uv run uvicorn app.main:app --reload --port 8000

# 4. Frontend (separate terminal)
cd frontend
npm install
npm run dev                    # http://localhost:3000

# Or run everything with Docker
docker compose up --build
```

**Backend API explorer:** `http://localhost:8000/docs`

---

### Environment Variables

```ini
# .env.example

# Postgres
DATABASE_URL=postgresql+asyncpg://crypto:secret@localhost:5432/crypto_assistant

# Redis
REDIS_URL=redis://localhost:6379

# CoinGecko (free tier key from coingecko.com/en/api)
COINGECKO_API_KEY=

# JWT auth
SECRET_KEY=change-me-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Next.js
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

---

### Code Style & Linting

Both sides of the stack enforce consistent style automatically. The goal is that CI fails on any style or type error before a PR is merged, so reviewers never have to comment on formatting.

---

#### Python (Backend)

| Tool | Role | Version |
|------|------|---------|
| **Ruff** | Linter + formatter (replaces Flake8, pycodestyle, isort, and most Pylint rules) | `>=0.7` |
| **Pylint** | Deep static analysis — catches logic errors Ruff misses | `>=3.3` |
| **Mypy** | Static type checker | `>=1.13` |
| **pycodestyle** | PEP 8 style checker (used via Ruff's `pycodestyle` rule set `E/W`) | built into Ruff |

Add to `pyproject.toml`:

```toml
[tool.ruff]
target-version = "py312"
line-length = 100

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # Pyflakes (unused imports, undefined names)
    "I",    # isort (import order)
    "N",    # pep8-naming
    "UP",   # pyupgrade (modernise syntax)
    "B",    # flake8-bugbear (common bugs)
    "C4",   # flake8-comprehensions
    "SIM",  # flake8-simplify
    "TCH",  # flake8-type-checking (move imports into TYPE_CHECKING blocks)
]
ignore = ["E501"]  # line length handled by formatter

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[tool.pylint.main]
py-version = "3.12"
jobs = 4

[tool.pylint.messages_control]
disable = [
    "C0114",  # missing-module-docstring
    "C0115",  # missing-class-docstring
    "C0116",  # missing-function-docstring
    "R0903",  # too-few-public-methods (common with Pydantic models)
]

[tool.mypy]
python_version = "3.12"
strict = true
plugins = ["pydantic.mypy"]
ignore_missing_imports = true

[[tool.mypy.overrides]]
module = ["alembic.*", "apscheduler.*"]
ignore_missing_imports = true
```

Add the tools as dev dependencies:

```bash
uv add --dev ruff pylint mypy
```

**Run manually:**

```bash
# Format + auto-fix lint issues
uv run ruff format backend/
uv run ruff check backend/ --fix

# Deep static analysis
uv run pylint backend/app

# Type checking
uv run mypy backend/app
```

**Ruff vs Pylint — when to use each:**
- Ruff runs in milliseconds and covers style + common bugs. Run it on every save.
- Pylint is slower but catches deeper issues: unreachable code, too-complex functions, bad inheritance. Run it in CI.
- Mypy is the authoritative type checker. `strict = true` enforces that every function has annotated parameters and return types.

---

#### JavaScript / TypeScript (Frontend)

| Tool | Role | JS analogue of |
|------|------|---------------|
| **ESLint 9** | Linter — catches bugs, enforces patterns | Pylint / Flake8 |
| **Prettier 3** | Opinionated formatter | Ruff formatter / Black |
| **TypeScript** (`tsc --noEmit`) | Static type checking | Mypy |
| **eslint-plugin-import** | Import order and unused import detection | isort + Flake8 F401 |

**ESLint flat config (`eslint.config.mjs`):**

```js
import js from "@eslint/js";
import tseslint from "typescript-eslint";
import reactPlugin from "eslint-plugin-react";
import reactHooks from "eslint-plugin-react-hooks";
import importPlugin from "eslint-plugin-import";
import prettier from "eslint-config-prettier";

export default tseslint.config(
  js.configs.recommended,
  ...tseslint.configs.strictTypeChecked,   // strictest TS rules
  {
    plugins: {
      react: reactPlugin,
      "react-hooks": reactHooks,
      import: importPlugin,
    },
    rules: {
      "react-hooks/rules-of-hooks": "error",
      "react-hooks/exhaustive-deps": "warn",
      "import/order": ["warn", { "newlines-between": "always" }],
      "import/no-unused-modules": "warn",
      "@typescript-eslint/no-explicit-any": "error",
      "@typescript-eslint/consistent-type-imports": "warn",
    },
    languageOptions: {
      parserOptions: { project: true },
    },
  },
  prettier,  // must be last — disables rules that conflict with Prettier
);
```

**Prettier config (`.prettierrc`):**

```json
{
  "semi": true,
  "singleQuote": false,
  "tabWidth": 2,
  "trailingComma": "all",
  "printWidth": 100,
  "plugins": ["prettier-plugin-tailwindcss"]
}
```

`prettier-plugin-tailwindcss` automatically sorts Tailwind class names — no manual ordering needed.

Install dev dependencies:

```bash
npm install -D eslint typescript-eslint eslint-plugin-react eslint-plugin-react-hooks \
  eslint-plugin-import eslint-config-prettier prettier prettier-plugin-tailwindcss
```

**TypeScript strict config (`tsconfig.json` additions):**

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "exactOptionalPropertyTypes": true
  }
}
```

**Run manually:**

```bash
# Type check (no emit — just errors)
npx tsc --noEmit

# Lint
npx eslint src/

# Format
npx prettier --write src/

# Check formatting without writing (for CI)
npx prettier --check src/
```

---

#### Git Hooks — pre-commit

Use `pre-commit` (Python) to run all checks automatically before every commit, on both sides of the stack.

```bash
pip install pre-commit   # or: uv tool install pre-commit
pre-commit install       # hooks into .git/hooks/pre-commit
```

**`.pre-commit-config.yaml`:**

```yaml
repos:
  # Python
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.7.4
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.13.0
    hooks:
      - id: mypy
        additional_dependencies: [pydantic, sqlalchemy]
        args: [--strict]

  # JavaScript / TypeScript
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.4.2
    hooks:
      - id: prettier
        types_or: [ts, tsx, json, css, markdown]

  - repo: local
    hooks:
      - id: eslint
        name: ESLint
        entry: bash -c 'cd frontend && npx eslint src/ --max-warnings 0'
        language: system
        types: [ts]
        pass_filenames: false

      - id: tsc
        name: TypeScript type check
        entry: bash -c 'cd frontend && npx tsc --noEmit'
        language: system
        pass_filenames: false
```

**Run all hooks manually (without committing):**

```bash
pre-commit run --all-files
```

---

#### CI Integration

Add a GitHub Actions job that runs all checks on every PR:

```yaml
# .github/workflows/lint.yml
name: Lint & Type Check

on: [push, pull_request]

jobs:
  python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv sync --dev
        working-directory: backend
      - run: uv run ruff check backend/app
      - run: uv run ruff format --check backend/app
      - run: uv run pylint backend/app
      - run: uv run mypy backend/app

  frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: frontend/package-lock.json
      - run: npm ci
        working-directory: frontend
      - run: npx tsc --noEmit
        working-directory: frontend
      - run: npx eslint src/ --max-warnings 0
        working-directory: frontend
      - run: npx prettier --check src/
        working-directory: frontend
```

---

### Testing

**Backend (pytest + pytest-asyncio):**
```bash
cd backend
uv run pytest tests/ -v
```

**Frontend (Vitest + React Testing Library):**
```bash
cd frontend
npm run test
```

**End-to-end (Playwright):**
```bash
cd frontend
npx playwright test
```

---

## Notes for Beginners Reading This Site

- Crypto is volatile. Never invest more than you can afford to lose.
- Not your keys, not your coins — if you don't control your wallet's seed phrase, you don't truly own the funds.
- Always verify wallet addresses carefully before sending. Transactions are irreversible.
- Check your local tax laws. In most countries, buying, selling, mining, and spending crypto are all reportable events.
