import logging

from fastapi import FastAPI

from good_advice_backend.views import router as base_router

logger = logging.getLogger(__name__)


def get_app() -> FastAPI:
    """Creates a new instance of the FastAPI application."""
    logger.info("Starting FastAPI application...")
    app = FastAPI()
    app.include_router(base_router)
    return app
