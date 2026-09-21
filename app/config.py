from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "MEDNEXUS AI"
    env: str = "development"
    database_url: str = "sqlite:///./data/mednexus.db"
    llm_enabled: bool = False
    llm_api_key: str | None = None
    llm_model: str | None = None
    cors_origins: str = "http://localhost:8000"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
