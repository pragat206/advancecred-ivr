from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import CurrentUser, require_role
from app.db.models import AgentAvailability as AgentAvailabilityModel
from app.db.models import Role, User
from app.db.session import get_db
from app.models.schemas import AgentAvailability

router = APIRouter(prefix="/ai-agent", tags=["ai-agent"])


@router.get("/config/{agent_id}")
def get_agent_config(
    agent_id: int,
    current: CurrentUser = Depends(require_role("admin", "ai_agent")),
) -> dict:
    return {
        "agent_id": agent_id,
        "tenant_id": current.tenant_id,
        "language": "en-IN",
        "do_not_say": ["guaranteed returns", "false urgency"],
        "goal": "qualify lead and book callback",
        "transfer_policy": "transfer on request or high intent",
    }


@router.get("/human-pool", response_model=list[AgentAvailability])
def transfer_pool(
    db: Session = Depends(get_db),
    current: CurrentUser = Depends(require_role("admin", "ai_agent", "human_agent")),
) -> list[AgentAvailability]:
    rows = (
        db.query(AgentAvailabilityModel, User)
        .join(User, User.id == AgentAvailabilityModel.user_id)
        .filter(
            AgentAvailabilityModel.tenant_id == current.tenant_id,
            User.role == Role.human_agent,
            AgentAvailabilityModel.status == "available",
        )
        .all()
    )
    return [
        AgentAvailability(
            agent_id=str(user.id),
            status=availability.status,
            active_calls=availability.active_calls,
            max_concurrent_calls=user.max_concurrent_calls,
        )
        for availability, user in rows
        if availability.active_calls < user.max_concurrent_calls
    ]
