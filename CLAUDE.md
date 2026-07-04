# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Status

Scaffold is complete. The working endpoints are `/api/v1/coins/` and `/api/v1/coins/{id}` (both proxy CoinGecko live). The following endpoints exist but `raise NotImplementedError` and need to be filled in:
- `GET /api/v1/prices/{coin_id}/history` — query the `price_hourly` TimescaleDB aggregate
- `GET /api/v1/mining/coins` — query `coins WHERE is_mineable = true`
- `GET /api/v1/exchanges/` — query the `exchanges` table
- `POST /api/v1/auth/register` and `POST /api/v1/auth/token`

Redis cache helpers exist in `backend/app/core/cache.py` but are not yet wired into any router. `price_sync.py` calls `coingecko.fetch_markets()` on a 5-min schedule but does not yet persist results to `price_ticks`.

## Stack

- **Frontend:** Next.js 15 (App Router), React 19, TypeScript 5 strict, Tailwind CSS v4
- **Backend:** FastAPI 0.115+, Python 3.12, managed with `uv`
- **Database:** PostgreSQL 16 + TimescaleDB extension + `pg_trgm`
- **Cache:** Redis 7
- **ORM / migrations:** SQLAlchemy 2 (async, asyncpg driver) + Alembic
- **Background jobs:** APScheduler (in-process, asyncio scheduler)

## Commands

All commands assume you are in the relevant subdirectory unless noted.

### Backend (run from `backend/`)

```bash
uv sync                                        # install deps
uv sync --dev                                  # include dev/lint deps
uv run alembic upgrade head                    # run migrations
uv run alembic revision --autogenerate -m "<msg>"
uv run uvicorn app.main:app --reload --port 8000

uv run pytest tests/ -v                        # all tests
uv run pytest tests/routers/test_coins.py -v   # single file
uv run pytest -k "test_name" -v                # single test

uv run ruff check app --fix                    # lint + auto-fix
uv run ruff format app                         # format
uv run pylint app                              # deep static analysis
uv run mypy app                                # type check
```

### Frontend (run from `frontend/`)

```bash
npm install --legacy-peer-deps   # react-leaflet@4 declares React 18 peer dep; flag is required
npm run dev                      # http://localhost:3000
npm run build && npm start

npm run type-check               # tsc --noEmit
npm run lint                     # eslint src/ --max-warnings 0
npm run format                   # prettier --write src/
npm run format:check             # CI check (no write)
npm run test                     # Vitest
npx playwright test              # end-to-end
```

### Full stack (Docker)

```bash
docker compose up db redis -d    # infra only (useful during backend dev)
docker compose up --build        # everything
```

## Architecture

### Backend layout (`backend/app/`)

- `main.py` — FastAPI app factory and lifespan hooks (scheduler start/stop). All routers mounted here under `/api/v1/`.
- `config.py` — `pydantic-settings` reads `.env`; import the singleton `settings` object, never instantiate `Settings` again.
- `database.py` — async SQLAlchemy engine + `get_session` dependency + `Base` declarative base.
- `models/` — ORM models. `models/__init__.py` imports all of them so Alembic autogenerate picks them up.
- `schemas/` — Pydantic v2 request/response schemas, always separate from ORM models.
- `routers/` — one `APIRouter` per domain, prefix set on the router (e.g. `/coins`), global `/api/v1` prefix added in `main.py`.
- `services/coingecko.py` — the only place that calls the CoinGecko API.
- `services/price_sync.py` — APScheduler job; `scheduler` instance imported by `main.py` lifespan.
- `core/cache.py` — Redis `get`/`set` helpers (cache-aside pattern, not yet wired into routers).
- `core/security.py` — `hash_password`, `verify_password`, `create_access_token`.

### Frontend layout (`frontend/src/`)

- `app/` — Next.js App Router. All pages are Server Components by default; add `"use client"` only where browser APIs or hooks are needed.
- `components/ui/` — reserved for shadcn/ui components added via `npx shadcn@latest add <component>`. Do not create files here manually.
- `components/LeafletMap.tsx` — uses plain Leaflet via `useRef` + `useEffect` (not `react-leaflet`'s `MapContainer`). This is intentional: `MapContainer` crashes under React Strict Mode's double-render. The ref guard prevents double-initialisation; the cleanup calls `map.remove()`.
- `components/MerchantMap.tsx` — thin wrapper that loads `LeafletMap` via `next/dynamic` with `ssr: false` (Leaflet accesses `window` at import time).
- `lib/api.ts` — all typed fetch wrappers for the FastAPI backend. Add new endpoint wrappers here.
- `lib/queryClient.ts` — TanStack Query singleton; `staleTime` is set to 5 min to match the backend Redis TTL.
- `lib/utils.ts` — `cn()` helper (clsx + tailwind-merge).
- `store/useAppStore.ts` — Zustand store for lightweight cross-component UI state.

### Key architectural decisions

- **Server Components fetch `api.*` directly** at request time for initial page loads — no client waterfall. Use `"use client"` + TanStack Query only for data that needs to refresh or respond to user input (e.g. `CoinTable`).
- **`price_ticks` is a TimescaleDB hypertable** partitioned on `recorded_at`. Always include both `coin_id` and `recorded_at` in WHERE clauses so chunk exclusion applies. Query the `price_hourly` continuous aggregate for chart data, not the raw table.
- **All API routes are prefixed `/api/v1/`** — the prefix is set in `main.py` via `include_router(..., prefix="/api/v1")`, not in the individual routers.
- **Pydantic schemas and SQLAlchemy models are always separate** — routers return schema instances, never ORM objects.
- **Redis cache-aside** is the pattern for the hot endpoints once wired: TTL 5 min for market data, 1 hour for price history.

## Code Style

### Python

Config in `backend/pyproject.toml`. Ruff is the formatter and primary linter. Pylint is for CI deep analysis. Mypy `strict = true` with the `pydantic.mypy` plugin. Every function must have annotated parameters and return type.

### TypeScript

ESLint 9 flat config (`eslint.config.mjs`), `typescript-eslint` `strictTypeChecked` rules, Prettier for formatting with `prettier-plugin-tailwindcss` for automatic class sorting. `@typescript-eslint/no-explicit-any` is an error. `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` are enabled — array and object indexing returns `T | undefined`.

### Pre-commit

`.pre-commit-config.yaml` runs Ruff, Mypy, Prettier, ESLint, and `tsc` on every commit.
```bash
pre-commit install
```
