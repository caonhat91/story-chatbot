from pydantic import BaseModel

class ChatRequest(BaseModel):
    sessionId: str
    question: str
    provider: str = "openai"   # openai | gemini
    model: str = "gpt-4o-mini"
