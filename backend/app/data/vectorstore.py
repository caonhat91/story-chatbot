from langchain_community.vectorstores import Chroma
from app.core.config import DATA_PATH
from app.data.loader import load_story_docs
from langchain_core.embeddings import Embeddings

_vectorstore_cache: dict[str, Chroma] = {}


def get_vectorstore(embedding: Embeddings) -> Chroma:
    """
    Vectorstore is created once per embedding type
    """
    key = embedding.__class__.__name__

    if key not in _vectorstore_cache:
        _vectorstore_cache[key] = Chroma.from_documents(
            documents=load_story_docs(DATA_PATH),
            embedding=embedding,
            persist_directory=f"./chroma_db/{key}",
        )

    return _vectorstore_cache[key]
