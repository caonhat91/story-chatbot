from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import GEMINI_API_KEY
from .base import LLMProvider

class GeminiLLM(LLMProvider):

    def build(self):
        return ChatGoogleGenerativeAI(
            google_api_key=GEMINI_API_KEY,
            model=GEMINI_MODEL,
            streaming=True,
        )
