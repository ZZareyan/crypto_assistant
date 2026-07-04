import logging
from datetime import datetime, timezone

import feedparser
import httpx
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.news_item import NewsItem
from app.sources.base import BaseCrawler
from app.sources.registry import RSSSource

logger = logging.getLogger(__name__)


class RSSCrawler(BaseCrawler):
    def __init__(self, source: RSSSource) -> None:
        self.source = source

    async def crawl(self, session: AsyncSession) -> int:
        xml = await self._fetch_xml()
        feed = feedparser.parse(xml)
        count = 0

        for entry in feed.entries:
            external_id: str = (
                entry.get("id") or entry.get("link") or entry.get("title") or ""
            )
            if not external_id:
                continue

            published_at: datetime | None = None
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                published_at = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)

            thumbnail_url: str | None = None
            for enc in getattr(entry, "enclosures", []):
                if enc.get("type", "").startswith("image/"):
                    thumbnail_url = enc.get("href")
                    break
            if thumbnail_url is None:
                media = getattr(entry, "media_thumbnail", None)
                if media:
                    thumbnail_url = media[0].get("url")

            stmt = (
                pg_insert(NewsItem)
                .values(
                    source_type="rss",
                    source_name=self.source.name,
                    external_id=external_id,
                    title=entry.get("title", ""),
                    url=entry.get("link", ""),
                    description=_plain_text(entry.get("summary", "")),
                    coin_tags=self.source.coin_tags,
                    thumbnail_url=thumbnail_url,
                    author=entry.get("author"),
                    published_at=published_at,
                )
                .on_conflict_do_nothing(constraint="uq_news_item_source_external")
            )
            result = await session.execute(stmt)
            count += result.rowcount

        await session.commit()
        return count

    async def _fetch_xml(self) -> str:
        async with httpx.AsyncClient(
            timeout=30,
            follow_redirects=True,
            headers={"User-Agent": "crypto-crawler/1.0 (+https://github.com/yourname/crypto-website)"},
        ) as client:
            resp = await client.get(self.source.url)
            resp.raise_for_status()
        return resp.text


def _plain_text(html: str) -> str:
    """Strip HTML tags from feed summaries."""
    from bs4 import BeautifulSoup

    return BeautifulSoup(html, "html.parser").get_text(separator=" ").strip()
