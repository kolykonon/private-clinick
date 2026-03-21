from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone


class IDMixin:
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )


class TimeStampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=func.now()
    )


class ContactsMixin:
    email: Mapped[str] = mapped_column(String(100), nullable=True, unique=True)
    phone: Mapped[str] = mapped_column(String(100), nullable=True, unique=True)
