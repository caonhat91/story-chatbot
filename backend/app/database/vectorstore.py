from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import time
import random
from typing import List


class RetryingEmbeddings:
    """Wrapper that retries embedding requests with exponential backoff.

    Chroma expects an object exposing `embed_documents`, so this wrapper
    delegates to the real embeddings implementation and retries on errors
    (e.g. quota `RESOURCE_EXHAUSTED` / 429).
    """
    def __init__(self, embeddings, max_retries: int = 3, base_delay: float = 1.0):
        self._emb = embeddings
        self.max_retries = max_retries
        self.base_delay = base_delay

    def embed_documents(self, documents: List[str]):
        attempt = 0
        while True:
            try:
                return self._emb.embed_documents(documents)
            except Exception as e:
                attempt += 1
                if attempt > self.max_retries:
                    raise
                # exponential backoff + jitter
                delay = self.base_delay * (2 ** (attempt - 1))
                delay = delay * (0.5 + random.random() * 0.5)
                time.sleep(delay)


def create_vectorstore(docs, user_id: str = "default"):
    """Create or load a Chroma vectorstore for the provided documents.

    Uses `RetryingEmbeddings` to reduce chance of immediate failures when
    the provider returns a transient quota/rate error.
    """
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    retrying_embeddings = RetryingEmbeddings(embeddings)

    return Chroma.from_documents(
        docs,
        retrying_embeddings,
        collection_name=f"user_{user_id}",
        persist_directory="./chroma_db"
    )
