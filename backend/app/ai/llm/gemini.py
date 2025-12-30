from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import GEMINI_API_KEY
from .base import LLMProvider

class GeminiLLM(LLMProvider):

    def get_llm(self, model: str | None = None) -> ChatGoogleGenerativeAI:
        return ChatGoogleGenerativeAI(
            google_api_key=GEMINI_API_KEY,
            model=model or GEMINI_MODEL,
            streaming=True,
        )
