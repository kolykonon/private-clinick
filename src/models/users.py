from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base
from src.models.mixins import ContactsMixin, IDMixin, TimeStampMixin


class User(Base, IDMixin, ContactsMixin, TimeStampMixin):
    is_active: Mapped[bool] = mapped_column(default=True, server_default=True)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default=False)
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("profiles.id", ondelete="SET NULL")
    )
    profile: Mapped["Profile"] = relationship("user")


class Profile(Base, IDMixin, TimeStampMixin):
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    adress: Mapped[str] = mapped_column(String(200), nullable=False)
    birth_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    insurance_policy: Mapped[int] = mapped_column(unique=True, nullable=False)
