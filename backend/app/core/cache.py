import json
from typing import Any

import redis.asyncio as aioredis

from app.config import settings

_client: aioredis.Redis[str] | None = None


def get_client() -> aioredis.Redis[str]:
    global _client
    if _client is None:
        _client = aioredis.from_url(settings.redis_url, decode_responses=True)
    return _client


async def get(key: str) -> Any:
    raw = await get_client().get(key)
    return json.loads(raw) if raw else None


async def set(key: str, value: Any, ttl: int) -> None:
    await get_client().setex(key, ttl, json.dumps(value))
