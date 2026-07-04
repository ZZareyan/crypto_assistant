from datetime import datetime
from decimal import Decimal

from sqlalchemy import BigInteger, DateTime, ForeignKey, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class PriceTick(Base):
    """TimescaleDB hypertable — partitioned on recorded_at.

    Always include coin_id + recorded_at in WHERE clauses so chunk exclusion applies.
    Query the price_hourly continuous aggregate for chart history, not this table directly.
    """

    __tablename__ = "price_ticks"

    coin_id: Mapped[str] = mapped_column(Text, ForeignKey("coins.id"), primary_key=True)
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)
    price_usd: Mapped[Decimal | None] = mapped_column(Numeric(20, 8))
    market_cap: Mapped[int | None] = mapped_column(BigInteger)
    volume_24h: Mapped[int | None] = mapped_column(BigInteger)
    change_24h: Mapped[Decimal | None] = mapped_column(Numeric(8, 4))
