from fastapi.testclient import TestClient

from app.main import app
from app.services.ai_orchestrator import AIAgentOrchestrator, AIAgentPolicy


def test_health() -> None:
    client = TestClient(app)
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_ui_loads() -> None:
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
    assert 'Enterprise IVR Dashboard' in response.text


def test_orchestrator_prompt() -> None:
    prompt = AIAgentOrchestrator().build_system_prompt(
        AIAgentPolicy(
            role_prompt='Sales assistant',
            language='hi-IN',
            forbidden_topics=['guaranteed returns'],
            transfer_triggers=['user asks for human'],
        )
    )
    assert 'Sales assistant' in prompt
    assert 'hi-IN' in prompt
