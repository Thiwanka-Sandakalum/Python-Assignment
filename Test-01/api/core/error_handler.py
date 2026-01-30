from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from elastic_transport import ConnectionError
from core.exceptions import ServiceNotFoundException
from core.logging_config import logger
import uuid

def get_request_id(request: Request):
    return request.headers.get("X-Request-ID") or str(uuid.uuid4())

def register_exception_handlers(app):
    @app.middleware("http")
    async def add_request_id_header(request: Request, call_next):
        request_id = get_request_id(request)
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response

    @app.exception_handler(ServiceNotFoundException)
    async def service_not_found_handler(request: Request, exc: ServiceNotFoundException):
        request_id = get_request_id(request)
        logger.error(f"Service not found: {exc.service_name}", extra={"request_id": request_id})
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": f"Service '{exc.service_name}' not found",
                "data": None,
                "request_id": request_id
            }
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        request_id = get_request_id(request)
        logger.warning(f"Validation error: {exc.errors()}", extra={"request_id": request_id})
        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "message": "Validation error",
                "data": exc.errors(),
                "request_id": request_id
            }
        )

    @app.exception_handler(ConnectionError)
    async def elastic_exception_handler(request: Request, exc: ConnectionError):
        request_id = get_request_id(request)
        logger.error(f"Elasticsearch connection error: {str(exc)}", extra={"request_id": request_id})
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Elasticsearch connection error",
                "data": None,
                "request_id": request_id
            }
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        request_id = get_request_id(request)
        logger.error(f"Unhandled error: {str(exc)}", extra={"request_id": request_id})
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal Server Error",
                "data": None,
                "request_id": request_id
            }
        )
