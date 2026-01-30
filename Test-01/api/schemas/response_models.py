from pydantic import BaseModel
from typing import Optional

class StatusResponse(BaseModel):
    service_name: Optional[str]
    status: str

class ApplicationStatusResponse(BaseModel):
    application_status: str
