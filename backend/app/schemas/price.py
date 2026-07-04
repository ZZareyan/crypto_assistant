from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class PriceTickSchema(BaseModel):
    recorded_at: datetime
    price_usd: Decimal | None
    market_cap: int | None
    volume_24h: int | None
    change_24h: Decimal | None

    model_config = {"from_attributes": True}


class PriceHistoryResponse(BaseModel):
    coin_id: str
    ticks: list[PriceTickSchema]
