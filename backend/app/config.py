from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+asyncpg://crypto:secret@localhost:5432/crypto_assistant"
    redis_url: str = "redis://localhost:6379"
    coingecko_api_key: str = ""
    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 60
    cors_origins: list[str] = ["http://localhost:3000"]


settings = Settings()
