# AdvanceCred IVR - Enterprise AI Voice Calling Platform

This repository now contains a production-oriented FastAPI starter and architecture blueprint for the enterprise IVR system you described.

## Included in this starter
- FastAPI service with role-based route groups:
  - Admin endpoints (bulk lead import, transcript fetch, dashboard KPI)
  - Human agent endpoints (my leads, status update, availability)
  - AI agent endpoints (policy config + transfer pool)
- Twilio service abstraction for outbound and call transfer.
- AI orchestrator abstraction for building policy-guarded prompts.
- Detailed architecture and deployment guidance in `docs/architecture.md`.

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open:
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/health`

## Next implementation milestones
1. Add persistence models (SQLAlchemy) + Alembic migrations.
2. Add RBAC auth and tenant scoping middleware.
3. Build Twilio webhook handlers (status callbacks + media streams).
4. Implement async dialer workers and retry strategies.
5. Add React/Next.js enterprise UI with square-edge design system.
