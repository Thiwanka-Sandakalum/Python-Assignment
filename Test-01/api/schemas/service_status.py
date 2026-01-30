from pydantic import BaseModel
from datetime import datetime

class ServiceStatus(BaseModel):
    application_name: str
    service_name: str
    service_status: str
    host_name: str
    timestamp: datetime
