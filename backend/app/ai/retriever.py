def get_retriever(vectorstore, user_id: str):
    return vectorstore.as_retriever(
        search_kwargs={
            "k": 4,
            "filter": {"user_id": user_id}
        }
    )
