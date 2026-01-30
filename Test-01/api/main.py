
from fastapi import FastAPI
from routes.health_routes import router
from core.error_handler import register_exception_handlers


app = FastAPI(
    title="RBC App Monitoring Service",
    version="1.0.0"
)

register_exception_handlers(app)

app.include_router(router)
