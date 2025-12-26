from langchain_community.vectorstores import Chroma
from app.core.config import DATA_PATH
from app.data.loader import load_story_docs

def get_vectorstore(embedding=None):
    return Chroma.from_documents(
        documents=load_story_docs(DATA_PATH),
        embedding=embedding,
        persist_directory="./chroma_db",
    )
