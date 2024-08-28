from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DECIMAL, TIMESTAMP, String, func

from bet_library.common_utils import generate_uuid
from line_provider.src.models.base import BaseModel

class Bet(BaseModel):
    id: Mapped[str] = mapped_column(String, primary_key=True, default=generate_uuid())
    event_id: Mapped[str] = mapped_column(String)
    amount: Mapped[float] = mapped_column(DECIMAL(10, 2))
    status: Mapped[str] = mapped_column(String(20), default="pending")
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

    # Add foreign key relationship if needed
    # event = relationship("Event", back_populates="bets")
