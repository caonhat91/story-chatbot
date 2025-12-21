from langchain_google_genai import ChatGoogleGenerativeAI
from .base_llm import BaseLLMEngine
from .config import GOOGLE_API_KEY

class GeminiEngine(BaseLLMEngine):

    def __init__(self, streaming=False):
        super().__init__(streaming=streaming)

    def get_model(self):
        """Initialize and return a Google Gemini LLM instance."""
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=GOOGLE_API_KEY,
            streaming=self.streaming,
            temperature=0.7,
            max_output_tokens=512
        )