
from pydantic import BaseModel, Field
from typing import Optional

class StatusResponse(BaseModel):
    service_name: Optional[str] = Field(
        None, description="Name of the service.", example="httpd"
    )
    status: str = Field(
        ..., description="Status of the service.", example="UP"
    )

class ApplicationStatusResponse(BaseModel):
    application_status: str = Field(
        ..., description="Overall application status.", example="UP"
    )
