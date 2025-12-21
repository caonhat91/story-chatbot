from langchain_core.chat_history import InMemoryChatMessageHistory

# session_id -> history
_SESSION_STORE: dict[str, InMemoryChatMessageHistory] = {}

def get_session_history(session_id: str):
    """ Retrieve or create chat message history for a given session ID. """
    if session_id not in _SESSION_STORE:
        _SESSION_STORE[session_id] = InMemoryChatMessageHistory()
    return _SESSION_STORE[session_id]
