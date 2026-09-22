from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    env: str = "development"
    database_url: str = "sqlite:///./data/mednexus.db"
    cors_origins: str = "*"
    model_cache_dir: str = "./ml_artifacts"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
ENGINE_VERSION = "3.0.0"
