import httpx

from app.config import settings
from app.schemas.coin import CoinDetail, CoinListResponse, CoinSummary

_BASE = "https://api.coingecko.com/api/v3"


def _headers() -> dict[str, str]:
    if settings.coingecko_api_key:
        return {"x-cg-demo-api-key": settings.coingecko_api_key}
    return {}


async def fetch_markets(
    page: int = 1,
    per_page: int = 50,
    category: str | None = None,
) -> CoinListResponse:
    params: dict[str, str | int] = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": page,
        "sparkline": "false",
    }
    if category:
        params["category"] = category

    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{_BASE}/coins/markets", params=params, headers=_headers())
        resp.raise_for_status()

    items = [
        CoinSummary(
            id=c["id"],
            symbol=c["symbol"],
            name=c["name"],
            image_url=c.get("image"),
            price_usd=c.get("current_price"),
            market_cap=c.get("market_cap"),
            change_24h=c.get("price_change_percentage_24h"),
            is_mineable=False,
        )
        for c in resp.json()
    ]
    return CoinListResponse(items=items, total=len(items), page=page, per_page=per_page)


async def fetch_coin_detail(coin_id: str) -> CoinDetail:
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{_BASE}/coins/{coin_id}", headers=_headers())
        resp.raise_for_status()

    c = resp.json()
    market = c.get("market_data", {})
    return CoinDetail(
        id=c["id"],
        symbol=c["symbol"],
        name=c["name"],
        image_url=c.get("image", {}).get("large"),
        price_usd=market.get("current_price", {}).get("usd"),
        market_cap=market.get("market_cap", {}).get("usd"),
        change_24h=market.get("price_change_percentage_24h"),
        is_mineable=False,
        category=None,
        algorithm=c.get("hashing_algorithm"),
    )
