# AdvanceCred IVR - Enterprise AI Voice Calling Platform

<<<<<<< HEAD
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
=======
This repository now contains a production-oriented FastAPI starter and architecture blueprint for the enterprise IVR system you described.

## Included in this starter
- FastAPI service with role-based route groups:
  - Admin endpoints (bulk lead import, transcript fetch, dashboard KPI)
  - Human agent endpoints (my leads, status update, availability)
  - AI agent endpoints (policy config + transfer pool)
- Twilio service abstraction for outbound and call transfer.
- AI orchestrator abstraction for building policy-guarded prompts.
- Detailed architecture and deployment guidance in `docs/architecture.md`.
>>>>>>> origin/main

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

<<<<<<< HEAD
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
=======
Then open:
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/health`

## Next implementation milestones
1. Add persistence models (SQLAlchemy) + Alembic migrations.
2. Add RBAC auth and tenant scoping middleware.
3. Build Twilio webhook handlers (status callbacks + media streams).
4. Implement async dialer workers and retry strategies.
5. Add React/Next.js enterprise UI with square-edge design system.
>>>>>>> origin/main
