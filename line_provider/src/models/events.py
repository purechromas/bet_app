import uuid

from enum import Enum
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DECIMAL, TIMESTAMP, String, func

from bet_library.common_utils import generate_uuid

from line_provider.src.models.base import BaseModel


class EventStatus(Enum):
    UNFINISHED = "unfinished"
    TEAM1_WON = "team1_won"
    TEAM2_WON = "team2_won"


class Event(BaseModel):
    id: Mapped[str] = mapped_column(String, primary_key=True, default=generate_uuid())
    event_name: Mapped[str] = mapped_column(String(255), nullable=False)
    odds: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    status: Mapped[EventStatus] = mapped_column(Enum(EventStatus), default=EventStatus.UNFINISHED)
    finish_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
