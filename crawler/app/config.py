from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+asyncpg://crypto:secret@localhost:5432/crypto_assistant"
    youtube_api_key: str = ""  # https://console.cloud.google.com — YouTube Data API v3


settings = Settings()
