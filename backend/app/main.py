from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import auth, coins, exchanges, mining, prices
from app.services.price_sync import scheduler


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    scheduler.start()
    yield
    scheduler.shutdown()


app = FastAPI(
    title="Crypto Assistant API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(coins.router, prefix="/api/v1")
app.include_router(prices.router, prefix="/api/v1")
app.include_router(mining.router, prefix="/api/v1")
app.include_router(exchanges.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
