from pydantic import EmailStr
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):

    PROJECT_NAME: str = "Private clinick"
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")

    REDIS_USER: str = os.getenv("REDIS_USER")
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD")
    REDIS_HOST: str = os.getenv("REDIS_HOST")
    REDIS_PORT: str = os.getenv("REDIS_PORT")

    REDIS_MAX_CONNECTIONS: int = 10
    CACHE_TTL = 300

    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str
    SMTP_PASSWORD: str
    EMAIL_FROM: EmailStr

    RATE_LIMIT_CALLS: int = 10
    RATE_LIMIT_PERIOD: int = 60

    def get_postgres_url(self) -> str:
        return f"postgresql+asyncpg:// \
            {self.POSTGRES_USER}:{self.POSTGRES_PASSWORD} \
            @{self.POSTGRES_HOST}:{self.POSTGRES_PORT} \
            /{self.POSTGRES_DB}"

    def get_redis_url(self) -> str:
        return f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD} \
        @{self.REDIS_HOST}:{self.REDIS_PORT}/0"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
