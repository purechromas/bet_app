from pydantic import BaseModel


class Event(BaseModel):
    id: str
    event_name: str
    odds: float
    status: str
    finish_at: str
    created_at: str
    updated_at: str


class EventsListOut(BaseModel):
    events: list[Event]
