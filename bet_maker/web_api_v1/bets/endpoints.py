from fastapi import APIRouter, Depends, status

from bet_maker.src.schemas.bets import EventsListOut

events_routers = APIRouter(prefix="events", tags=["events"])

async def get_unfinished_events_handler() -> EventsListOut:
    # Dummy implementation - replace with actual logic
    unfinished_events = [
        {
            "id": "1",
            "event_name": "Event A",
            "odds": 1.50,
            "status": "unfinished",
            "finish_at": "2024-08-30T12:00:00Z",
            "created_at": "2024-08-25T12:00:00Z",
            "updated_at": "2024-08-26T12:00:00Z"
        }
    ]
    return EventsListOut(events=unfinished_events)

@events_routers.post("/events/", status_code=status.HTTP_201_CREATED)
async def get_unfinished_events(
        events_list: EventsListOut = Depends(get_unfinished_events_handler)
) -> EventsListOut:
    return await get_unfinished_events_handler()
