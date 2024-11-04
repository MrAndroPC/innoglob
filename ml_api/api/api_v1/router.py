from fastapi import APIRouter
from ml_api.api.api_v1.endpoints import send_rag_request

api_router = APIRouter()
api_router.include_router(send_rag_request.router, prefix="/rag", tags=["RAG"])
