# AdvanceCred IVR - Enterprise AI Voice Calling Platform

Enterprise-grade IVR backend with FastAPI, Twilio webhook support, SQLAlchemy persistence, JWT RBAC + tenant scoping, Celery dialer workers, and a professional square-edge HTML/CSS/JS dashboard starter.

## Implemented modules
- **Persistence:** SQLAlchemy models and session handling.
- **Migrations:** Alembic config + initial migration.
- **RBAC/Auth:** JWT login with role checks (`admin`, `human_agent`, `ai_agent`).
- **Tenant Scoping:** `X-Tenant-ID` middleware enforcement for protected APIs.
- **Telephony Webhooks:** Twilio status callback + media transcript ingestion stubs.
- **Async Dialer:** Celery task with retry backoff for outbound dialing.
- **Enterprise UI Starter:** Minimal square-edge dashboard and lead table.

## API highlights
- `POST /api/v1/auth/login`
- `POST /api/v1/admin/leads/bulk-import`
- `GET /api/v1/admin/transcripts/{call_sid}`
- `GET /api/v1/admin/dashboard`
- `GET /api/v1/agent/my-leads`
- `PATCH /api/v1/agent/lead/{lead_id}`
- `GET /api/v1/ai-agent/human-pool`
- `POST /api/v1/webhooks/twilio/status`
- `POST /api/v1/webhooks/twilio/media`

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- `http://127.0.0.1:8000/` (enterprise UI)
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/health`

## Migration commands
```bash
alembic upgrade head
```

## Worker commands
```bash
celery -A app.workers.celery_app.celery_app worker --loglevel=info
```
