from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.ai.services.chat import AIService
from app.schemas.chat import ChatRequest

router = APIRouter()

@router.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    return AIService().stream_chat(req)
