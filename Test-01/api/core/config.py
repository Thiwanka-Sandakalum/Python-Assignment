import os

class Settings:
    ELASTIC_HOST = os.getenv("ELASTIC_HOST", "http://localhost:9200")
    ELASTIC_INDEX = os.getenv("ELASTIC_INDEX", "rbcapp-status")

settings = Settings()
