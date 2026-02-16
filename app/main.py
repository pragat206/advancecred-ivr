from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes import admin, ai_agent, auth, human_agent
from app.core.config import settings
from app.middleware.tenant import TenantHeaderMiddleware
from app.webhooks import twilio

app = FastAPI(title=settings.app_name)
app.add_middleware(TenantHeaderMiddleware)

app.include_router(auth.router, prefix=settings.api_v1_prefix)
app.include_router(admin.router, prefix=settings.api_v1_prefix)
app.include_router(human_agent.router, prefix=settings.api_v1_prefix)
app.include_router(ai_agent.router, prefix=settings.api_v1_prefix)
app.include_router(twilio.router, prefix=settings.api_v1_prefix)

static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
def ui() -> FileResponse:
    return FileResponse(static_dir / "index.html")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": settings.app_name}
