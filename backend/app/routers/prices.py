from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.price import PriceHistoryResponse

router = APIRouter(prefix="/prices", tags=["prices"])


@router.get("/{coin_id}/history", response_model=PriceHistoryResponse)
async def get_price_history(
    coin_id: str,
    days: int = Query(7, ge=1, le=365),
    session: AsyncSession = Depends(get_session),
) -> PriceHistoryResponse:
    # TODO: query price_hourly continuous aggregate
    raise NotImplementedError
