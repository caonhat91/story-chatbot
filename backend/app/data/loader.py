import json
from langchain_core.documents import Document

def load_story_docs(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [
        Document(
            page_content=item["content"],
            metadata={
                "chapter": item["title"],
                "url": item["url"]
            }
        )
        for item in data
    ]
