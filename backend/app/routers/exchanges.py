from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session

router = APIRouter(prefix="/exchanges", tags=["exchanges"])


@router.get("/")
async def list_exchanges(
    session: AsyncSession = Depends(get_session),
) -> list[dict[str, object]]:
    # TODO: query exchanges table
    raise NotImplementedError
