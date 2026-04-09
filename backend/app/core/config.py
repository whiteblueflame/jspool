from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "jspool"
    api_v1_prefix: str = "/api/v1"
    debug: bool = False

    database_url: str = (
        "mysql+pymysql://jspool:jspool@127.0.0.1:3306/jspool?charset=utf8mb4"
    )

    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"

    @property
    def cors_origin_list(self) -> List[str]:
        return [x.strip() for x in self.cors_origins.split(",") if x.strip()]


@lru_cache()
def get_settings() -> Settings:
    return Settings()
