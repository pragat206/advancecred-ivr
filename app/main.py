from fastapi import FastAPI

from app.api.routes import admin, ai_agent, human_agent
from app.core.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(admin.router, prefix=settings.api_v1_prefix)
app.include_router(human_agent.router, prefix=settings.api_v1_prefix)
app.include_router(ai_agent.router, prefix=settings.api_v1_prefix)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": settings.app_name}
