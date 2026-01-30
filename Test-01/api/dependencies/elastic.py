from elasticsearch import Elasticsearch
from core.config import settings

def get_elastic_client():
    return Elasticsearch(settings.ELASTIC_HOST)
