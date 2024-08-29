from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DECIMAL, TIMESTAMP, String, func

from bet_library.common_utils import generate_uuid
from bet_maker.src.models.base import BaseModel


class Bet(BaseModel):
    # UUID гарантирует, что для каждой ставки будет уникальный идентификатор, сложный для предсказания и атаки.
    # Хотя вероятность коллизии (дублирования) UUID крайне мала, система должна обрабатывать такие ошибки и
    # генерировать новый UUID до тех пор, пока не будет найден уникальный идентификатор.
    # Важно отметить, что такие случаи являются крайне редкими.
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda x: generate_uuid())
    event_id: Mapped[str] = mapped_column()
    amount: Mapped[float] = mapped_column(DECIMAL(10, 2))
    status: Mapped[str] = mapped_column(String(20), default="pending")
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
