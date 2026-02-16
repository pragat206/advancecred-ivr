"""AI orchestration primitives for IVR voice agents."""

from dataclasses import dataclass


@dataclass
class AIAgentPolicy:
    role_prompt: str
    language: str
    forbidden_topics: list[str]
    transfer_triggers: list[str]


class AIAgentOrchestrator:
    """Thin service abstraction to connect STT/TTS + realtime LLM loop + transfer logic."""

    def build_system_prompt(self, policy: AIAgentPolicy) -> str:
        guardrails = "\n".join(f"- Do not say: {item}" for item in policy.forbidden_topics)
        triggers = ", ".join(policy.transfer_triggers)
        return (
            f"Role: {policy.role_prompt}\n"
            f"Primary language: {policy.language}\n"
            f"Guardrails:\n{guardrails}\n"
            f"Transfer when: {triggers}"
        )
