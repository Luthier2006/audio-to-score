from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    APP_NAME: str = "Audio To Score"
    DEBUG: bool = True

    API_PREFIX: str = "/api"

    STORAGE_PATH: Path = BASE_DIR / "storage"
    UPLOADS_PATH: Path = STORAGE_PATH / "uploads"
    STEMS_PATH: Path = STORAGE_PATH / "stems"
    SEGMENTS_PATH: Path = STORAGE_PATH / "segments"
    SCORES_PATH: Path = STORAGE_PATH / "scores"
    EXPORTS_PATH: Path = STORAGE_PATH / "exports"

    REDIS_URL: str = "redis://redis:6379/0"

    class Config:
        env_file = ".env"


settings = Settings()

# garante que todas as pastas existam
for path in [
    settings.UPLOADS_PATH,
    settings.STEMS_PATH,
    settings.SEGMENTS_PATH,
    settings.SCORES_PATH,
    settings.EXPORTS_PATH
]:
    path.mkdir(parents=True, exist_ok=True)
