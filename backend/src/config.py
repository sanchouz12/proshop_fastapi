from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_ignore_empty=True, env_file_encoding="utf-8")

    ENVIRONMENT: Literal["dev", "prod"] = "dev"
