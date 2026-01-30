from fastapi import APIRouter, Depends
from core.config import Settings
from dependencies.elastic import get_elastic_client
from services.elastic_service import ElasticService
from services.health_service import HealthService
from schemas.service_status import ServiceStatus

router = APIRouter()

def get_health_service():
    client = get_elastic_client()
    elastic_service = ElasticService(client, Settings.ELASTIC_INDEX)
    return HealthService(elastic_service)

@router.post("/add")
def add_status(payload: ServiceStatus, health_service: HealthService = Depends(get_health_service)):
    elastic_service = health_service.elastic_service
    elastic_service.index_document(payload.dict())
    return {"message": "Document indexed successfully"}

@router.get("/healthcheck")
def get_app_status(health_service: HealthService = Depends(get_health_service)):
    return health_service.get_application_status()

@router.get("/healthcheck/{service_name}")
def get_service_status(service_name: str,health_service: HealthService = Depends(get_health_service)):
    return health_service.get_service_status(service_name)
