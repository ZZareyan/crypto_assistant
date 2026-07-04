from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class BaseCrawler(ABC):
    @abstractmethod
    async def crawl(self, session: AsyncSession) -> int:
        """Fetch items from source, upsert to DB, return count of newly inserted rows."""
        ...
