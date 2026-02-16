from fastapi import APIRouter

from app.models.schemas import DashboardKPI, LeadCreate, TranscriptEntry

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/leads/bulk-import")
def bulk_import_leads(payload: list[LeadCreate]) -> dict:
    """Queue a bulk lead import job; persistence is implemented by service layer."""
    return {"accepted": len(payload), "status": "queued"}


@router.get("/transcripts/{call_id}", response_model=list[TranscriptEntry])
def get_call_transcript(call_id: str) -> list[TranscriptEntry]:
    """Get transcript for a human or AI call by call id."""
    return []


@router.get("/dashboard", response_model=DashboardKPI)
def admin_dashboard() -> DashboardKPI:
    """Return holistic metrics for enterprise dashboard cards and charts."""
    from datetime import datetime

    return DashboardKPI(
        date=datetime.utcnow(),
        total_calls=0,
        connected_calls=0,
        converted_calls=0,
        avg_duration_seconds=0,
    )
