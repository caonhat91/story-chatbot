from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from langchain_core.messages import HumanMessage, AIMessage

from app.ai.factory.llm_factory import get_llm
from app.ai.factory.embedding_factory import get_embedding
from app.ai.rag.chain import build_rag_chain
from app.data.vectorstore import get_vectorstore

from app.ai.rag.memory import get_memory
from app.schemas.chat import ChatRequest

router = APIRouter()

@router.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    llm = get_llm(req.provider)
    vectorstore = get_vectorstore(get_embedding(req.provider))
    retriever = vectorstore.as_retriever(k=5)
    rag_chain = build_rag_chain(llm, retriever)

    memory = get_memory(req.sessionId)
    memory.add_message(HumanMessage(content=req.question))

    chat_history = "\n".join(
        f"{m.type.upper()}: {m.content}" for m in memory.messages
    )

    async def event_generator():
        answer = ""
        async for chunk in rag_chain.astream({
            "question": req.question,
            "chat_history": chat_history,
        }):
            if chunk.content:
                answer += chunk.content
                yield chunk.content
        memory.add_message(AIMessage(content=answer))

    return StreamingResponse(event_generator(), media_type="text/event-stream")

