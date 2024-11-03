from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "innoglob ml api"
    VECTOR_DATABASE_URL: str = "localhost:5432"

    class Config:
        env_file = ".env"

settings = Settings()
