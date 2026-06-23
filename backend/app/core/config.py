from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Requirement Assistant"

    # Use model_config instead of class Config in Pydantic v2
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()