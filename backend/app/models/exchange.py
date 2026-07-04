import uuid

from sqlalchemy import ARRAY, Boolean, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Exchange(Base):
    __tablename__ = "exchanges"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(Text, nullable=False)
    url: Mapped[str | None] = mapped_column(Text)
    has_fiat_onramp: Mapped[bool | None] = mapped_column(Boolean)
    kyc_required: Mapped[bool | None] = mapped_column(Boolean)
    supported_coins: Mapped[list[str] | None] = mapped_column(ARRAY(Text))
    fee_pct: Mapped[float | None] = mapped_column(Numeric(5, 4))
