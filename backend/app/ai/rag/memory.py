from langchain_core.chat_history import InMemoryChatMessageHistory

_memory_store: dict[str, InMemoryChatMessageHistory] = {}

def get_memory(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in _memory_store:
        _memory_store[session_id] = InMemoryChatMessageHistory()
    return _memory_store[session_id]