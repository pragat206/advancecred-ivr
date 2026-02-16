<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import CurrentUser, require_role
from app.db.models import AgentAvailability as AgentAvailabilityModel
from app.db.models import Lead, User
from app.db.session import get_db
from app.models.schemas import AgentAvailability, LeadRead, LeadUpdate
=======
from fastapi import APIRouter

from app.models.schemas import AgentAvailability, LeadUpdate
>>>>>>> origin/main

router = APIRouter(prefix="/agent", tags=["human-agent"])


<<<<<<< HEAD
@router.get("/my-leads", response_model=list[LeadRead])
def my_leads(
    db: Session = Depends(get_db),
    current: CurrentUser = Depends(require_role("human_agent")),
) -> list[LeadRead]:
    leads = db.query(Lead).filter(Lead.tenant_id == current.tenant_id, Lead.assigned_human_id == current.id).all()
    return [
        LeadRead(
            id=lead.id,
            full_name=lead.full_name,
            phone_number=lead.phone_number,
            source=lead.source,
            tags=[],
            status=lead.status,
            comment=lead.comment,
        )
        for lead in leads
    ]


@router.patch("/lead/{lead_id}")
def update_lead(
    lead_id: int,
    payload: LeadUpdate,
    db: Session = Depends(get_db),
    current: CurrentUser = Depends(require_role("human_agent")),
) -> dict:
    lead = db.query(Lead).filter(Lead.id == lead_id, Lead.tenant_id == current.tenant_id).first()
    if not lead or lead.assigned_human_id != current.id:
        raise HTTPException(status_code=404, detail="Lead not found")

    lead.status = payload.status
    lead.comment = payload.comment
    db.commit()
=======
@router.get("/my-leads")
def my_leads() -> list[dict]:
    """List only leads assigned to authenticated human agent."""
    return []


@router.patch("/lead/{lead_id}")
def update_lead(lead_id: str, payload: LeadUpdate) -> dict:
    """Update lead status and optional comment by assigned agent."""
>>>>>>> origin/main
    return {"lead_id": lead_id, "status": payload.status, "comment": payload.comment}


@router.get("/availability", response_model=AgentAvailability)
<<<<<<< HEAD
def my_availability(
    db: Session = Depends(get_db),
    current: CurrentUser = Depends(require_role("human_agent")),
) -> AgentAvailability:
    user = db.query(User).filter(User.id == current.id).first()
    availability = (
        db.query(AgentAvailabilityModel)
        .filter(AgentAvailabilityModel.user_id == current.id, AgentAvailabilityModel.tenant_id == current.tenant_id)
        .first()
    )
    if not availability:
        availability = AgentAvailabilityModel(user_id=current.id, tenant_id=current.tenant_id, status="available", active_calls=0)
        db.add(availability)
        db.commit()
        db.refresh(availability)

    return AgentAvailability(
        agent_id=str(current.id),
        status=availability.status,
        active_calls=availability.active_calls,
        max_concurrent_calls=user.max_concurrent_calls if user else 1,
=======
def my_availability() -> AgentAvailability:
    """Current availability used by AI/human transfer orchestration."""
    return AgentAvailability(
        agent_id="agent-placeholder",
        status="available",
        active_calls=0,
        max_concurrent_calls=1,
>>>>>>> origin/main
    )
