from celery.utils.log import get_task_logger

from app.services.twilio_service import TwilioVoiceClient
from app.workers.celery_app import celery_app

logger = get_task_logger(__name__)


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 3})
def dial_lead_task(self, lead_id: int, phone_number: str, twiml_url: str) -> dict:
    client = TwilioVoiceClient()
    sid = client.create_outbound_call(to_phone=phone_number, twiml_url=twiml_url)
    logger.info("Dial initiated", extra={"lead_id": lead_id, "call_sid": sid})
    return {"lead_id": lead_id, "call_sid": sid}
