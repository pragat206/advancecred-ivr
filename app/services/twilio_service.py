from twilio.rest import Client

from app.core.config import settings


class TwilioVoiceClient:
    def __init__(self) -> None:
        self.client = Client(settings.twilio_account_sid, settings.twilio_auth_token)

    def create_outbound_call(self, to_phone: str, twiml_url: str) -> str:
        call = self.client.calls.create(to=to_phone, from_=settings.twilio_number, url=twiml_url)
        return call.sid

    def transfer_call(self, call_sid: str, twiml_url: str) -> None:
        self.client.calls(call_sid).update(url=twiml_url, method="POST")
