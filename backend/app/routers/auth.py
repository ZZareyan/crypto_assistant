from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.user import Token, UserCreate, UserResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=201)
async def register(
    body: UserCreate,
    session: AsyncSession = Depends(get_session),
) -> UserResponse:
    # TODO: hash password, insert user, return schema
    raise NotImplementedError


@router.post("/token", response_model=Token)
async def login(
    body: UserCreate,
    session: AsyncSession = Depends(get_session),
) -> Token:
    # TODO: verify credentials, issue JWT
    raise NotImplementedError
