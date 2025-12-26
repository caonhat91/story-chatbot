from abc import ABC, abstractmethod
from langchain_core.embeddings import Embeddings

class EmbeddingProvider(ABC):
    @abstractmethod
    def get_embedding(self) -> Embeddings:
        pass