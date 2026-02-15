from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PRODUCTION: bool = False
    GEMINI_API_KEY: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
