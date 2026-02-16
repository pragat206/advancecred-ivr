from datetime import datetime

from fastapi import APIRouter, Depends, Form, Header
from sqlalchemy.orm import Session

from app.db.models import Call, Transcript
from app.db.session import get_db

router = APIRouter(prefix="/webhooks/twilio", tags=["twilio-webhooks"])


@router.post("/status")
def call_status_callback(
    CallSid: str = Form(...),
    CallStatus: str = Form(...),
    CallDuration: str | None = Form(default=None),
    x_tenant_id: str | None = Header(default=None),
    db: Session = Depends(get_db),
) -> dict:
    call = db.query(Call).filter(Call.twilio_call_sid == CallSid).first()
    if not call:
        call = Call(twilio_call_sid=CallSid, tenant_id=int(x_tenant_id or 1), status=CallStatus)
        db.add(call)
    call.status = CallStatus
    if CallStatus == "in-progress" and call.started_at is None:
        call.started_at = datetime.utcnow()
    if CallStatus in {"completed", "failed", "busy", "no-answer", "canceled"}:
        call.ended_at = datetime.utcnow()
        if CallDuration and CallDuration.isdigit():
            call.duration_seconds = float(CallDuration)
    db.commit()
    return {"ok": True}


@router.post("/media")
def media_stream_event(db: Session = Depends(get_db), payload: dict | None = None) -> dict:
    if payload and payload.get("type") == "transcript":
        call = db.query(Call).filter(Call.twilio_call_sid == payload.get("call_sid")).first()
        if call:
            db.add(
                Transcript(
                    call_id=call.id,
                    speaker=payload.get("speaker", "unknown"),
                    utterance=payload.get("utterance", ""),
                    timestamp=datetime.utcnow(),
                )
            )
            db.commit()
    return {"ok": True}
