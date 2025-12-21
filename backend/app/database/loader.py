import json
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_documents(path: str):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    docs = [
        Document(
            page_content=item["content"],
            metadata={
                "chapter": item["title"]
            }
        )
        for item in data
    ]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=150
    )

    return splitter.split_documents(docs)
