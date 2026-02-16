from fastapi import APIRouter

from app.models.schemas import AgentAvailability, LeadUpdate

router = APIRouter(prefix="/agent", tags=["human-agent"])


@router.get("/my-leads")
def my_leads() -> list[dict]:
    """List only leads assigned to authenticated human agent."""
    return []


@router.patch("/lead/{lead_id}")
def update_lead(lead_id: str, payload: LeadUpdate) -> dict:
    """Update lead status and optional comment by assigned agent."""
    return {"lead_id": lead_id, "status": payload.status, "comment": payload.comment}


@router.get("/availability", response_model=AgentAvailability)
def my_availability() -> AgentAvailability:
    """Current availability used by AI/human transfer orchestration."""
    return AgentAvailability(
        agent_id="agent-placeholder",
        status="available",
        active_calls=0,
        max_concurrent_calls=1,
    )
