from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ELASTIC_HOST: str = "http://localhost:9200"
    ELASTIC_INDEX: str = "rbcapp-status"

    class Config:
        env_file = ".env"

settings = Settings()
