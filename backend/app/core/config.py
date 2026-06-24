from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Requirement Assistant"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()