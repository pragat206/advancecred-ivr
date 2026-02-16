from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.auth.dependencies import CurrentUser, require_role
from app.db.models import Call, Lead, LeadStatus, Role, Transcript, User
from app.db.session import get_db
from app.models.schemas import DashboardKPI, LeadCreate, TranscriptEntry

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/leads/bulk-import")
def bulk_import_leads(
    payload: list[LeadCreate],
    db: Session = Depends(get_db),
    current: CurrentUser = Depends(require_role("admin")),
) -> dict:
    created = 0
    for item in payload:
        lead = Lead(
            tenant_id=current.tenant_id,
            full_name=item.full_name,
            phone_number=item.phone_number,
            source=item.source,
            assigned_human_id=item.assigned_to_id if item.assigned_to_type.value == "human" else None,
            assigned_ai_id=item.assigned_to_id if item.assigned_to_type.value == "ai" else None,
        )
        db.add(lead)
        created += 1
    db.commit()
    return {"accepted": created, "status": "imported"}


@router.get("/transcripts/{call_id}", response_model=list[TranscriptEntry])
def get_call_transcript(
    call_id: str,
    db: Session = Depends(get_db),
    current: CurrentUser = Depends(require_role("admin")),
) -> list[TranscriptEntry]:
    call = db.query(Call).filter(Call.twilio_call_sid == call_id, Call.tenant_id == current.tenant_id).first()
    if not call:
        return []
    rows = db.query(Transcript).filter(Transcript.call_id == call.id).order_by(Transcript.timestamp.asc()).all()
    return [
        TranscriptEntry(call_id=call_id, speaker=row.speaker, utterance=row.utterance, timestamp=row.timestamp)
        for row in rows
    ]


@router.get("/dashboard", response_model=DashboardKPI)
def admin_dashboard(
    db: Session = Depends(get_db),
    current: CurrentUser = Depends(require_role("admin")),
) -> DashboardKPI:
    total_calls = db.query(func.count(Call.id)).filter(Call.tenant_id == current.tenant_id).scalar() or 0
    connected_calls = (
        db.query(func.count(Call.id))
        .filter(Call.tenant_id == current.tenant_id, Call.status.in_(["in-progress", "completed"]))
        .scalar()
        or 0
    )
    converted_calls = (
        db.query(func.count(Lead.id)).filter(Lead.tenant_id == current.tenant_id, Lead.status == LeadStatus.converted).scalar() or 0
    )
    avg_duration = (
        db.query(func.avg(Call.duration_seconds)).filter(Call.tenant_id == current.tenant_id).scalar() or 0.0
    )

    return DashboardKPI(
        date=datetime.utcnow(),
        total_calls=int(total_calls),
        connected_calls=int(connected_calls),
        converted_calls=int(converted_calls),
        avg_duration_seconds=float(avg_duration),
    )


@router.get("/agents/availability")
def agent_availability(
    db: Session = Depends(get_db),
    current: CurrentUser = Depends(require_role("admin")),
) -> list[dict]:
    agents = (
        db.query(User)
        .filter(User.tenant_id == current.tenant_id, User.role.in_([Role.human_agent, Role.ai_agent]))
        .all()
    )
    return [{"id": a.id, "email": a.email, "role": a.role.value, "max_concurrent_calls": a.max_concurrent_calls} for a in agents]
