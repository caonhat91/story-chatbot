from langchain_openai import ChatOpenAI
from app.core.config import OPENAI_API_KEY, OPENAI_MODEL
from .base import LLMProvider

class OpenAILLM(LLMProvider):

    def get_llm(self):
        return ChatOpenAI(
            api_key=OPENAI_API_KEY,
            model=OPENAI_MODEL,
            streaming=True,
            temperature=0.7,
        )