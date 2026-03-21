from typing import List

from sqlalchemy import DECIMAL, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base
from src.models.mixins import ContactsMixin, IDMixin, TimeStampMixin


class Position(Base, IDMixin):
    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    doctor: Mapped["Doctor"] = relationship(back_populates="position")


class Doctor(Base, IDMixin, TimeStampMixin, ContactsMixin):
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    post: Mapped[int] = mapped_column(
        ForeignKey("positions.id", ondelete="SET NULL"), unique=True, nullable=True
    )
    position: Mapped["Position"] = relationship(back_populates="doctor")
    services: Mapped[List["Service"]] = relationship(back_populates="doctor")


class Specialization(Base, IDMixin):
    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)


class Service(Base, IDMixin):
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    price: Mapped[float] = mapped_column(DECIMAL(8, 2), nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"))
    doctor: Mapped["Doctor"] = relationship(back_populates="services")
