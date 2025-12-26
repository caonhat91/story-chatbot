from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.core.config import GEMINI_API_KEY
from .base import EmbeddingProvider

class GeminiEmbedding(EmbeddingProvider):
    def get_embedding(self):
        return GoogleGenerativeAIEmbeddings(google_api_key=GEMINI_API_KEY)

