from app.ai.embeddings.openai import OpenAIEmbedding
from app.ai.embeddings.gemini import GeminiEmbedding

def get_embedding(provider: str):
    provider = provider.lower()

    if provider == "openai":
        return OpenAIEmbedding().get_embedding()

    if provider == "gemini":
        return GeminiEmbedding().get_embedding()

    raise ValueError(f"Unsupported embedding provider: {provider}")
