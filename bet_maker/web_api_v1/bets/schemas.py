from pydantic import BaseModel, Field


class CreateBetIn(BaseModel):
    event_id: str
    amount: float = Field(
        gt=0,
        description="Amount must be a positive number with two decimal places",
    )


class CreateBetOut(BaseModel):
    bet_id: str


class BetOut(BaseModel):
    bet_id: str
    event_id: str
    amount: float
    status: str
    created_at: str
