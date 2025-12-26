from langchain_openai import OpenAIEmbeddings
from app.core.config import OPENAI_API_KEY
from .base import EmbeddingProvider

class OpenAIEmbedding(EmbeddingProvider):
    def get_embedding(self):
        return OpenAIEmbeddings(api_key=OPENAI_API_KEY)
