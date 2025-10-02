from threading import settrace

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    SENDER_EMAIL :str

    SENDER_PASSWORD :str

    SMTP_SERVER :str

    SMTP_PORT :str

    class Config:
        env_file = ".env"


settings = Settings()
