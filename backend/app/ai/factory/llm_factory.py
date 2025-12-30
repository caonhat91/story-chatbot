from app.ai.llm.openai import OpenAILLM
from app.ai.llm.gemini import GeminiLLM

def get_llm(provider: str, model: str | None = None):
    provider = provider.lower()

    if provider == "openai":
        return OpenAILLM().get_llm(model=model)

    if provider == "gemini":
        return GeminiLLM().get_llm(model=model)

    raise ValueError(f"Unsupported LLM provider: {provider}")
