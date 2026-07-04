import asyncio
import logging

from app.scheduler import build_scheduler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
)
logger = logging.getLogger(__name__)


async def main() -> None:
    scheduler = build_scheduler()
    scheduler.start()
    logger.info("Crawler started — %d jobs scheduled", len(scheduler.get_jobs()))
    try:
        while True:
            await asyncio.sleep(3600)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        scheduler.shutdown()
        logger.info("Crawler stopped")


if __name__ == "__main__":
    asyncio.run(main())
