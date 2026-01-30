
from core.exceptions import ServiceNotFoundException

class HealthService:
    def __init__(self, elastic_service):
        self.elastic_service = elastic_service

    def get_service_status(self, service_name: str):
        result = self.elastic_service.get_latest_service(service_name)
        if not result:
            raise ServiceNotFoundException(service_name)
        return {
            "success": True,
            "message": "Service status retrieved",
            "data": {
                "service_name": service_name,
                "status": result["service_status"]
            }
        }

    def get_application_status(self):
        services = ["httpd", "rabbitmq", "postgresql"]
        for service in services:
            result = self.elastic_service.get_latest_service(service)
            if not result or result["service_status"] == "DOWN":
                return {
                    "success": True,
                    "message": "Application is DOWN",
                    "data": {"application_status": "DOWN"}
                }
        return {
            "success": True,
            "message": "Application is UP",
            "data": {"application_status": "UP"}
        }
