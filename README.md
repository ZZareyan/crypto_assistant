# Crypto Assistant

A beginner-friendly website that explains everything a newcomer needs to know about cryptocurrency — from first principles to spending their first coins — backed by a live data API and a continuous news crawler.

---

## Site Sections

### 1. What Is Crypto & How Does It Work
Demystifies core concepts without jargon: blockchain, wallets, public/private keys, Proof of Work vs Proof of Stake. Includes a glossary tooltip system for inline term definitions.

### 2. Explore Coins
Live coin table and detail pages powered by the CoinGecko API. Shows price, market cap, 24h change, and a 7-day price chart per coin.

### 3. How to Mine
Covers mineable coins (BTC, LTC, XMR, RVN, ERG, KAS), hardware types (CPU / GPU / ASIC), and an interactive profitability estimator.

### 4. How to Buy
Exchange comparison (Coinbase, Kraken, Binance, Uniswap), step-by-step buying guide, and hot/cold wallet recommendations.

### 5. How to Spend
Crypto debit cards, Lightning Network payments, BitPay merchants, stablecoin transfers, and a Coinmap-powered merchant map.

---

## Architecture

```
┌───────────────────────────────────────────────────────┐
│               Browser                                 │
│       React 19 + Next.js 15 (App Router)              │
│    Tailwind CSS v4 · TanStack Query · Zustand         │
└──────────────────────┬────────────────────────────────┘
                       │ HTTPS / JSON
┌──────────────────────▼────────────────────────────────┐
│            FastAPI (Python 3.12)                      │
│   Pydantic v2 · SQLAlchemy 2 (async) · Alembic        │
│   APScheduler — price sync every 5 min                │
└──────────────────────┬────────────────────────────────┘
                       │ asyncpg
┌──────────────────────▼────────────────────────────────┐
│           PostgreSQL 16 + TimescaleDB                 │
│   price_ticks hypertable · price_hourly aggregate     │
│   news_items (crawler)                                │
└──────────────────────┘
        │                     │
  Redis 7 (cache)     ┌───────────────────────────────┐
                      │    Crawler (Python 3.12)       │
                      │  APScheduler · httpx           │
                      │  59 YouTube searches           │
                      │  55 RSS feeds                  │
                      └───────────────────────────────┘
```

**Services** (all defined in `docker-compose.yml`):

| Service | Port | Description |
|---------|------|-------------|
| `frontend` | 3000 | Next.js dev server |
| `backend` | 8000 | FastAPI + Swagger UI at `/docs` |
| `crawler` | — | Headless news ingestion, no HTTP port |
| `db` | 5432 | PostgreSQL 16 + TimescaleDB |
| `redis` | 6379 | Cache + rate limiting |

---

## Project Structure

```
crypto-assistant/
├── frontend/                    # Next.js 15
│   ├── src/
│   │   ├── app/                 # App Router pages (Server Components by default)
│   │   │   ├── page.tsx         # Landing
│   │   │   ├── what-is-crypto/
│   │   │   ├── explore-coins/[id]/
│   │   │   ├── mining/
│   │   │   ├── how-to-buy/
│   │   │   └── how-to-spend/
│   │   ├── components/
│   │   │   ├── ui/              # shadcn/ui (add via: npx shadcn@latest add <name>)
│   │   │   ├── CoinTable.tsx    # Client Component — TanStack Query
│   │   │   ├── PriceChart.tsx   # Recharts
│   │   │   ├── MiningCalculator.tsx
│   │   │   ├── ExchangeComparison.tsx
│   │   │   ├── MerchantMap.tsx  # next/dynamic wrapper (ssr: false)
│   │   │   ├── LeafletMap.tsx   # Plain Leaflet via useRef (not MapContainer)
│   │   │   ├── GlossaryTooltip.tsx
│   │   │   ├── Nav.tsx
│   │   │   └── Providers.tsx
│   │   ├── lib/
│   │   │   ├── api.ts           # Typed fetch wrappers → FastAPI
│   │   │   ├── queryClient.ts   # TanStack Query singleton
│   │   │   └── utils.ts         # cn() helper
│   │   └── store/
│   │       └── useAppStore.ts   # Zustand
│   ├── eslint.config.mjs
│   ├── next.config.ts
│   ├── postcss.config.mjs       # Tailwind v4
│   ├── tsconfig.json
│   └── Dockerfile
│
├── backend/                     # FastAPI
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py            # pydantic-settings
│   │   ├── database.py          # async SQLAlchemy engine
│   │   ├── models/              # ORM: Coin, PriceTick, Exchange, User
│   │   ├── schemas/             # Pydantic: CoinSummary, CoinDetail, …
│   │   ├── routers/             # coins, prices, mining, exchanges, auth
│   │   ├── services/
│   │   │   ├── coingecko.py     # CoinGecko API client
│   │   │   └── price_sync.py    # APScheduler job
│   │   └── core/
│   │       ├── cache.py         # Redis helpers
│   │       └── security.py      # JWT
│   ├── alembic/
│   ├── tests/
│   ├── pyproject.toml
│   └── Dockerfile
│
├── crawler/                     # News ingestion service
│   ├── app/
│   │   ├── main.py              # asyncio entry point
│   │   ├── scheduler.py         # APScheduler, fires all jobs on startup
│   │   ├── models/
│   │   │   └── news_item.py     # news_items table
│   │   └── sources/
│   │       ├── registry.py      # ← only file to edit when adding sources
│   │       ├── youtube.py       # YouTube Data API v3
│   │       └── rss.py           # feedparser + BeautifulSoup
│   ├── alembic/                 # manages news_items only
│   ├── tests/
│   ├── pyproject.toml
│   └── Dockerfile
│
├── docker-compose.yml
├── .env.example
├── .pre-commit-config.yaml
├── .github/workflows/lint.yml
└── CLAUDE.md                    # development guidance for Claude Code
```

---

## Quick Start

**Prerequisites:** Docker Desktop, Node.js 22, Python 3.12, [`uv`](https://docs.astral.sh/uv/)

```bash
# 1. Clone and configure
git clone https://github.com/yourname/crypto-assistant
cd crypto-assistant
cp .env.example .env
# Edit .env — at minimum set COINGECKO_API_KEY and YOUTUBE_API_KEY

# 2. Run everything
docker compose up --build

# Or run infra only and develop locally:
docker compose up db redis -d

# Backend
cd backend && uv sync && uv run alembic upgrade head
uv run uvicorn app.main:app --reload --port 8000

# Crawler (separate terminal)
cd crawler && uv sync && uv run alembic upgrade head
uv run python -m app.main

# Frontend (separate terminal)
cd frontend && npm install --legacy-peer-deps && npm run dev
```

| URL | Service |
|-----|---------|
| http://localhost:3000 | Frontend |
| http://localhost:8000/docs | Backend Swagger UI |

---

## Environment Variables

| Variable | Service | Description |
|----------|---------|-------------|
| `DATABASE_URL` | backend, crawler | asyncpg connection string |
| `REDIS_URL` | backend | Redis connection string |
| `COINGECKO_API_KEY` | backend | Free key from coingecko.com/en/api |
| `SECRET_KEY` | backend | JWT signing secret |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | backend | JWT TTL (default 60) |
| `YOUTUBE_API_KEY` | crawler | YouTube Data API v3 key from Google Cloud Console |
| `NEXT_PUBLIC_API_URL` | frontend | FastAPI base URL |

---

## Crawler Sources

Defined in `crawler/app/sources/registry.py`. Current coverage:

- **59 YouTube searches** — 3 pinned channels (Coin Bureau, Altcoin Daily, Into The Cryptoverse), 13 topic searches, 22 L1 coins, 7 L2/scaling, 9 emerging coins, 5 memecoins
- **55 RSS feeds** — 22 high-frequency news outlets (CoinDesk, CoinTelegraph, Decrypt, The Block…), 7 analysis/research (Messari, Milk Road, Glassnode…), protocol blogs (Ethereum Foundation, Vitalik Buterin, Solana, Chainlink…), exchange blogs, mainstream finance

To add a source, append a `YoutubeSearchSource` or `RSSSource` to the relevant list in `registry.py` — no other changes required.

---

## Development

See `CLAUDE.md` for commands, architecture decisions, and code style rules.

**Pre-commit hooks** (runs Ruff, Mypy, Prettier, ESLint, tsc on every commit):
```bash
pre-commit install
```

**CI** runs the same checks on every push via `.github/workflows/lint.yml`.

---

## Notes for Beginners

- Crypto is volatile. Never invest more than you can afford to lose.
- Not your keys, not your coins — if you don't control your wallet's seed phrase, you don't truly own the funds.
- Always verify wallet addresses before sending. Transactions are irreversible.
- Check your local tax laws. Buying, selling, mining, and spending crypto are all taxable events in most jurisdictions.
