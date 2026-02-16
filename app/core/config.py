from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AdvanceCred IVR"
    environment: str = "dev"
    api_v1_prefix: str = "/api/v1"

    postgres_dsn: str = "postgresql+psycopg2://ivr:ivr@localhost:5432/ivr"
    redis_url: str = "redis://localhost:6379/0"

    jwt_secret: str = "change-me"
    jwt_algo: str = "HS256"
    access_token_minutes: int = 30

    twilio_account_sid: str = ""
    twilio_auth_token: str = ""
    twilio_number: str = ""

    openai_api_key: str = ""
    openai_realtime_model: str = "gpt-4o-realtime-preview"
    openai_stt_model: str = "gpt-4o-mini-transcribe"
    openai_tts_model: str = "gpt-4o-mini-tts"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
