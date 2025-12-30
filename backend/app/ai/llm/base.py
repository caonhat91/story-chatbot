from abc import ABC, abstractmethod
from langchain_core.language_models.chat_models import BaseChatModel

class LLMProvider(ABC):
    @abstractmethod
    def get_llm(self, model: str | None = None) -> BaseChatModel:
        pass