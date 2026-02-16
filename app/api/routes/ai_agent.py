from fastapi import APIRouter

from app.models.schemas import AgentAvailability

router = APIRouter(prefix="/ai-agent", tags=["ai-agent"])


@router.get("/config/{agent_id}")
def get_agent_config(agent_id: str) -> dict:
    """Prompt, guardrails, language, and escalation policy for AI voice agent."""
    return {
        "agent_id": agent_id,
        "language": "en-IN",
        "do_not_say": ["guaranteed returns", "false urgency"],
        "goal": "qualify lead and book callback",
        "transfer_policy": "transfer on request or high intent",
    }


@router.get("/human-pool", response_model=list[AgentAvailability])
def transfer_pool() -> list[AgentAvailability]:
    """Online human agents that can accept transferred calls."""
    return []
