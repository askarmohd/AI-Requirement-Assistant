from fastapi import FastAPI
import logging
from app.core.logging import setup_logging
from app.api.routes.health import router as health_router

setup_logging()
logger = logging.getLogger(__name__)
logger.info("AI Requirement Assistant starting")
app = FastAPI(
    title="AI Requirement Assistant",
    version="1.0.0"
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)