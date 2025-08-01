import os
from pathlib import Path
from dotenv import load_dotenv
try:
    from pydantic_settings import BaseSettings
except ImportError:  # fall back for pydantic<2
    from pydantic import BaseSettings

# Load .env file
load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str | None = None
    WEBHOOK_URL: str | None = None
    DEBUG: bool = False
    RATE_LIMIT: str = "5/minute"
    LOG_LEVEL: str = "INFO"
    SGF_OUTPUT_DIR: Path = Path("sgf_output")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
settings.SGF_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
