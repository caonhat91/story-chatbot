# Story Chatbot
```text
Yêu cầu:

- Tạo một chatbot có khả năng trả lời các câu hỏi về truyện chữ, tóm tắt nhân vật, tính cách, các thông tin liên quan tới nhân vật.
- Chatbot cần truy xuất thông tin từ tài liệu nội bộ (JSON).
- Tích hợp khả năng phản hồi theo ngữ cảnh hội thoại.

Công nghệ sử dụng:
- LangChain (Document Loaders, Retrieval, Conversational Chain) - LangSmith (Quản lý và giám sát quá trình phát triển)
- Gemini
- BE: Python + UV
- FE: Vue3 + tanstack

Output:
- Source code hoàn chỉnh
- Readme chi tiết giới thiệu về project + hướng dẫn chạy.
```

## 1. Kiến trúc tổng thể

```text
story-chatbot/
├── backend/
│   ├── app/
│   │   ├── main.py                # FastAPI entry
│   │   ├── api/
│   │   │   └── chat.py            # /chat/stream
│   │   ├── core/
│   │   │   ├── config.py          # env, settings
│   │   │   └── logging.py
│   │   ├── ai/
│   │   │   ├── factory/
│   │   │   │   ├── llm_factory.py
│   │   │   │   └── embedding_factory.py
│   │   │   ├── llm/
│   │   │   │   ├── base.py        # LLM interface
│   │   │   │   ├── openai.py
│   │   │   │   └── gemini.py
│   │   │   ├── embeddings/
│   │   │   │   ├── base.py
│   │   │   │   ├── openai.py
│   │   │   │   └── gemini.py
│   │   │   ├── rag/
│   │   │   │   ├── chain.py       # LCEL chain
│   │   │   │   └── memory.py
│   │   ├── data/
│   │   │   ├── loader.py          # JSON → Document
│   │   │   └── vectorstore.py     # Chroma / FAISS
│   │   └── schemas/
│   │       └── chat.py            # Pydantic models
│   ├── data/
│   │   └── vo-luyen-dinh-phong_chapters.json
│   ├── .env
│   └── pyproject.toml
│
├── frontend/
│   ├── e2e/                       # End to end testing
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   │   └── chat.ts
│   │   ├── assets/
│   │   ├── components/
│   │   │   └── ChatUI.vue
│   │   ├── directives/
│   │   │   └── v-focus-slash.ts
│   │   ├── router/
│   │   │   └── index.ts
│   │   └── views/
│   │   │   └── HomeView.vue
│   │   └── App.vue
│   │   └── main.ts
│   ├── .env
│   ├── vite.config.ts
│   ├── package.json
│   └── README.md
│
└── README.md
```

## 2. Running
- `backend/README.md`
- `frontend/README.md`