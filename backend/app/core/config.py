# backend/app/core/config.py

from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    # Add other config variables as needed:
    GCS_BUCKET_NAME: str = ""
    EMAIL_SENDER: str = ""

    class Config:
        env_file = ".env"  # Load variables from .env file

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
