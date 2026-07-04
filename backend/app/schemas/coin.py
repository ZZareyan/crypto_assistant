from pydantic import BaseModel


class CoinSummary(BaseModel):
    id: str
    symbol: str
    name: str
    image_url: str | None
    price_usd: float | None
    market_cap: int | None
    change_24h: float | None
    is_mineable: bool

    model_config = {"from_attributes": True}


class CoinDetail(CoinSummary):
    category: str | None
    algorithm: str | None


class CoinListResponse(BaseModel):
    items: list[CoinSummary]
    total: int
    page: int
    per_page: int
