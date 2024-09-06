from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Blog Post API Project"
    admin_email: str = "admin@example.com"
    database_url: str = "sqlite://db.sqlite3"

    class Config:
        env_file = ".env"

settings = Settings()
