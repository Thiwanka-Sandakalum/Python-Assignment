
from pydantic import BaseModel, Field
from datetime import datetime

class ServiceStatus(BaseModel):
    application_name: str = Field(..., description="Name of the application.", example="rbcapp1")
    service_name: str = Field(..., description="Name of the service.", example="httpd")
    service_status: str = Field(..., description="Status of the service.", example="UP")
    host_name: str = Field(..., description="Host where the service is running.", example="testhost")
    timestamp: datetime = Field(..., description="Timestamp of the status.", example="2026-01-30T12:00:00Z")
