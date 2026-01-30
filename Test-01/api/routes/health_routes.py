from fastapi import APIRouter, Depends, status
from core.config import Settings
from dependencies.elastic import get_elastic_client
from services.elastic_service import ElasticService
from services.health_service import HealthService
from schemas.service_status import ServiceStatus
from schemas.response_models import StatusResponse, ApplicationStatusResponse

router = APIRouter()

def get_health_service():
    client = get_elastic_client()
    elastic_service = ElasticService(client, Settings.ELASTIC_INDEX)
    return HealthService(elastic_service)

@router.post(
    "/add",
    status_code=status.HTTP_201_CREATED,
    response_model=StatusResponse,
)
def add_status(
    payload: ServiceStatus = Depends(),
    health_service: HealthService = Depends(get_health_service)
):
    result = health_service.add_status(payload)
    return result

@router.get(
    "/healthcheck",
    response_model=ApplicationStatusResponse,
)
def get_app_status(health_service: HealthService = Depends(get_health_service)):
    return health_service.get_application_status()

@router.get(
    "/healthcheck/{service_name}",
    response_model=StatusResponse,
)
def get_service_status(service_name: str, health_service: HealthService = Depends(get_health_service)):
    return health_service.get_service_status(service_name)
