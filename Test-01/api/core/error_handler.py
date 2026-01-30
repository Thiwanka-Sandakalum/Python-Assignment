from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from elastic_transport import ConnectionError
from core.exceptions import ServiceNotFoundException
import logging

logger = logging.getLogger(__name__)

def register_exception_handlers(app):
    @app.exception_handler(ServiceNotFoundException)
    async def service_not_found_handler(request: Request, exc: ServiceNotFoundException):
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": f"Service '{exc.service_name}' not found",
                "data": None
            }
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "message": "Validation error",
                "data": exc.errors()
            }
        )

    @app.exception_handler(ConnectionError)
    async def elastic_exception_handler(request: Request, exc: ConnectionError):
        logger.error(f"Elasticsearch connection error: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Elasticsearch connection error",
                "data": None
            }
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled error: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal Server Error",
                "data": None
            }
        )
