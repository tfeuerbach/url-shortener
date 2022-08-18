# app/config.py

from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Prod"
    base_url: str = "http://myshortened.link"
    db_url: str = "sqlite:///./shortener.db"

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
