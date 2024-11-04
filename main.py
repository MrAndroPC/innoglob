from fastapi import FastAPI
from ml_api.api.api_v1.router import api_router
from ml_api.core.config import settings
from ml_api.api.api_v1.endpoints.send_rag_request import mock_find_similar_embeddings

print(mock_find_similar_embeddings("блабла"))
app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix="/api/v1")
