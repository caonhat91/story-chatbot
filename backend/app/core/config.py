import os
from dotenv import load_dotenv

env = os.getenv("ENV", "local")

load_dotenv(f".env.{env}")

if os.path.exists(".env.local"):
    load_dotenv(".env.local", override=True)

DATA_PATH = os.getenv("DATA_PATH")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT", "story-chatbot")