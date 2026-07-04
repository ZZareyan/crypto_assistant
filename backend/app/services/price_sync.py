import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.services import coingecko

logger = logging.getLogger(__name__)
scheduler = AsyncIOScheduler()


@scheduler.scheduled_job("interval", minutes=5)
async def sync_top_coins() -> None:
    try:
        await coingecko.fetch_markets(per_page=250)
        logger.info("Price sync completed")
    except Exception:
        logger.exception("Price sync failed")
