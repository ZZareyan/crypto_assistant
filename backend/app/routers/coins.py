from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.coin import CoinDetail, CoinListResponse
from app.services import coingecko

router = APIRouter(prefix="/coins", tags=["coins"])


@router.get("/", response_model=CoinListResponse)
async def list_coins(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, le=250),
    category: str | None = None,
    session: AsyncSession = Depends(get_session),
) -> CoinListResponse:
    return await coingecko.fetch_markets(page=page, per_page=per_page, category=category)


@router.get("/{coin_id}", response_model=CoinDetail)
async def get_coin(
    coin_id: str,
    session: AsyncSession = Depends(get_session),
) -> CoinDetail:
    return await coingecko.fetch_coin_detail(coin_id)
