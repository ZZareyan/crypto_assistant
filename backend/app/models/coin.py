from datetime import datetime

from sqlalchemy import Boolean, DateTime, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Coin(Base):
    __tablename__ = "coins"

    id: Mapped[str] = mapped_column(Text, primary_key=True)  # coingecko slug e.g. "bitcoin"
    symbol: Mapped[str] = mapped_column(Text, nullable=False)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[str | None] = mapped_column(Text)
    is_mineable: Mapped[bool] = mapped_column(Boolean, default=False)
    algorithm: Mapped[str | None] = mapped_column(Text)
    image_url: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
