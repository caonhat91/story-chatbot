from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import json
from ..database.loader import load_documents
from ..database.vectorstore import create_vectorstore
from ..ai.retriever import get_retriever
from ..ai.chain import create_rag_chain
from ..database.memory import get_session_history
from ..ai.core.factory import get_llm_engine

router = APIRouter()

docs = load_documents("data/vo-luyen-dinh-phong_chapters.json")
vectorstore = create_vectorstore(docs)
retriever = get_retriever(vectorstore)

class ChatRequest(BaseModel):
    provider: str = "gemini"
    question: str
    sessionId: str

@router.post("/chat/stream")
async def chat_stream(
    req: ChatRequest,
):
    llm = get_llm_engine(provider=req.provider, streaming=True).get_model()
    rag_chain = create_rag_chain(
        llm,
        retriever,
        get_session_history
    )

    async def event_generator():
        async for chunk in rag_chain.astream(
            {"question": req.question},
            config={
                "configurable": {"session_id": req.sessionId},
                "tags": ["story", "stream"],
                "metadata": {
                    "session_id": req.sessionId,
                    "api": "chat/stream"
                }
            }
        ):
            yield f"data: {json.dumps({'token': chunk})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
