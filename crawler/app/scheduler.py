import logging
from datetime import datetime, timezone

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.database import AsyncSessionLocal
from app.sources.registry import RSS_FEEDS, YOUTUBE_SEARCHES
from app.sources.rss import RSSCrawler
from app.sources.youtube import YoutubeSearchCrawler

logger = logging.getLogger(__name__)


def _make_job(crawler_cls: type, source: object) -> object:
    async def run() -> None:
        async with AsyncSessionLocal() as session:
            try:
                count = await crawler_cls(source).crawl(session)  # type: ignore[call-arg]
                logger.info("[%s] %d new items saved", getattr(source, "name", "?"), count)
            except Exception:
                logger.exception("[%s] crawl failed", getattr(source, "name", "?"))

    return run


def build_scheduler() -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler()
    now = datetime.now(timezone.utc)

    for src in RSS_FEEDS:
        scheduler.add_job(
            _make_job(RSSCrawler, src),
            trigger="interval",
            minutes=src.interval_minutes,
            id=f"rss.{src.name}",
            next_run_time=now,  # run immediately on startup
        )

    for src in YOUTUBE_SEARCHES:
        scheduler.add_job(
            _make_job(YoutubeSearchCrawler, src),
            trigger="interval",
            minutes=src.interval_minutes,
            id=f"yt.{src.name}",
            next_run_time=now,
        )

    return scheduler
