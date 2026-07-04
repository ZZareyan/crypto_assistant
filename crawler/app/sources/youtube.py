import logging
from datetime import datetime, timezone

import httpx
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.models.news_item import NewsItem
from app.sources.base import BaseCrawler
from app.sources.registry import YoutubeSearchSource

logger = logging.getLogger(__name__)

_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"


class YoutubeSearchCrawler(BaseCrawler):
    def __init__(self, source: YoutubeSearchSource) -> None:
        self.source = source

    async def crawl(self, session: AsyncSession) -> int:
        if not settings.youtube_api_key:
            logger.warning("YOUTUBE_API_KEY not set — skipping %s", self.source.name)
            return 0

        items = await self._fetch()
        count = 0

        for item in items:
            video_id: str = item["id"]["videoId"]
            snippet: dict[str, object] = item["snippet"]
            published_raw = str(snippet.get("publishedAt", ""))
            published_at: datetime | None = None
            if published_raw:
                published_at = datetime.fromisoformat(published_raw.replace("Z", "+00:00"))

            thumbnails = snippet.get("thumbnails") or {}
            thumb = (
                (thumbnails.get("high") or thumbnails.get("default") or {}).get("url")  # type: ignore[union-attr]
                if isinstance(thumbnails, dict)
                else None
            )

            stmt = (
                pg_insert(NewsItem)
                .values(
                    source_type="youtube",
                    source_name=self.source.name,
                    external_id=video_id,
                    title=str(snippet.get("title", "")),
                    url=f"https://www.youtube.com/watch?v={video_id}",
                    description=str(snippet.get("description", "")),
                    coin_tags=self.source.coin_tags,
                    thumbnail_url=thumb,
                    author=str(snippet.get("channelTitle", "")),
                    published_at=published_at,
                )
                .on_conflict_do_nothing(constraint="uq_news_item_source_external")
            )
            result = await session.execute(stmt)
            count += result.rowcount

        await session.commit()
        return count

    async def _fetch(self) -> list[dict[str, object]]:
        params: dict[str, str] = {
            "key": settings.youtube_api_key,
            "q": self.source.query,
            "part": "snippet",
            "type": "video",
            "order": "date",
            "maxResults": str(self.source.max_results),
            "publishedAfter": _seven_days_ago(),
        }
        if self.source.channel_id:
            params["channelId"] = self.source.channel_id
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(_SEARCH_URL, params=params)
            resp.raise_for_status()
        data: dict[str, object] = resp.json()
        return list(data.get("items") or [])  # type: ignore[arg-type]


def _seven_days_ago() -> str:
    from datetime import timedelta

    cutoff = datetime.now(timezone.utc) - timedelta(days=7)
    return cutoff.strftime("%Y-%m-%dT%H:%M:%SZ")
