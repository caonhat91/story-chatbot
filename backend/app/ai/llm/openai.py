from langchain_openai import ChatOpenAI
from app.core.config import OPENAI_API_KEY, OPENAI_MODEL
from .base import LLMProvider

class OpenAILLM(LLMProvider):

    def get_llm(self, model: str | None = None) -> ChatOpenAI:
        return ChatOpenAI(
            api_key=OPENAI_API_KEY,
            model=model or OPENAI_MODEL,
            streaming=True,
            temperature=0.7,
        )