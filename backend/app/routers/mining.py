from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.coin import CoinSummary

router = APIRouter(prefix="/mining", tags=["mining"])


@router.get("/coins", response_model=list[CoinSummary])
async def list_mineable_coins(
    session: AsyncSession = Depends(get_session),
) -> list[CoinSummary]:
    # TODO: query coins WHERE is_mineable = true
    raise NotImplementedError
