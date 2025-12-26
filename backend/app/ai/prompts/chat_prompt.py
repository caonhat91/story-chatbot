from langchain_core.prompts import ChatPromptTemplate

def get_chat_prompt_template() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages([
        (
            "system", 
            """
            Bạn là trợ lý chuyên phân tích truyện chữ.
            Chỉ sử dụng thông tin từ CONTEXT để trả lời.
            Nếu không có dữ liệu, hãy nói rõ là không tìm thấy.

            Nhiệm vụ:
            - Trả lời câu hỏi về truyện
            - Tóm tắt nhân vật
            - Phân tích tính cách, vai trò
            - Giữ ngữ cảnh hội thoại
            """
        ),
        ("human", "CONTEXT:\n{context}"),
        ("human", "CHAT HISTORY:\n{chat_history}"),
        ("human", "{question}")
    ])
