from app.ai.llm.openai import OpenAILLM
from app.ai.llm.gemini import GeminiLLM

def get_llm(provider: str):
    provider = provider.lower()

    if provider == "openai":
        return OpenAILLM().get_llm()

    if provider == "gemini":
        return GeminiLLM().get_llm()

    raise ValueError(f"Unsupported LLM provider: {provider}")
