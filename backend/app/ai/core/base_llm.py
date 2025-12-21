from abc import ABC, abstractmethod
from langchain_core.runnables import Runnable

class BaseLLMEngine(ABC):

    def __init__(self, streaming=False):
        self.streaming = streaming

    @abstractmethod
    def get_model(self) -> Runnable:
        """
        Must return a LangChain Runnable
        """
        pass
