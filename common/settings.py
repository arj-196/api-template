from functools import lru_cache

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings, SecretStr

load_dotenv()


class Settings(BaseSettings):
    # api
    # ---
    api_key: SecretStr = SecretStr("super-secret")

    # db_sql related
    # ---
    db_host: str = "localhost"
    db_port: int = 5491
    db_name: str = "autoplay"
    db_user: str = "postgres"
    db_password: SecretStr = SecretStr("example")
    db_driver: str = "postgresql"

    @property
    def db_url_async(self) -> str:
        """SQLAlchemy database URL"""
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password.get_secret_value()}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def db_url(self) -> str:
        """SQLAlchemy database URL"""
        return f"postgresql://{self.db_user}:{self.db_password.get_secret_value()}@{self.db_host}:{self.db_port}/{self.db_name}"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
