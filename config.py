# app/config.py

from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    # .env file located outside app directory
    # ENV_NAME="Development"
    # BASE_URL="http://127.0.0.1:8000"
    # DB_URL="sqlite:///./shortener.db"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
