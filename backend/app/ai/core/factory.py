from .gemini import GeminiEngine
from .base_llm import BaseLLMEngine

def get_llm_engine(provider: str, streaming=False) -> BaseLLMEngine:
    if provider == "gemini":
        return GeminiEngine(streaming=streaming)
    else:
        raise ValueError(f"Unsupported AI provider: {provider}")
