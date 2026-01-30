from services.interfaces import IElasticService
from core.exceptions import ServiceNotFoundException
from schemas.response_models import StatusResponse, ApplicationStatusResponse

class HealthService:
    def __init__(self, elastic_service: IElasticService):
        self.elastic_service = elastic_service

    def add_status(self, payload):
        self.elastic_service.index_document(payload.dict())
        return StatusResponse(
            service_name=payload.service_name,
            status=payload.service_status
        )

    def get_service_status(self, service_name: str):
        result = self.elastic_service.get_latest_service(service_name)
        if not result:
            raise ServiceNotFoundException(service_name)
        return StatusResponse(
            service_name=service_name,
            status=result["service_status"]
        )

    def get_application_status(self):
        services = ["httpd", "rabbitmq", "postgresql"]
        for service in services:
            result = self.elastic_service.get_latest_service(service)
            if not result or result["service_status"] == "DOWN":
                return ApplicationStatusResponse(application_status="DOWN")
        return ApplicationStatusResponse(application_status="UP")
