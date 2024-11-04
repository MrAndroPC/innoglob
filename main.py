from fastapi import FastAPI
from ml_api.api.api_v1.router import api_router
from ml_api.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix="/api/v1")
