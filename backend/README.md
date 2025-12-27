# Story Chatbot

Chatbot sample áp dụng LangChain.

## Tính năng

* Trả lời câu hỏi về truyện chữ
* Tóm tắt nhân vật, tính cách
* Nhớ ngữ cảnh hội thoại
* Truy xuất từ tài liệu nội bộ (JSON)

## Tech stack

* Backend & AI Orchestration: Python · FastAPI · LangChain · Gemini (Free Tier)/OpenAI
* Observability & LLM Monitoring: LangSmith
* Chuẩn LCEL
* Chia layer -> Factory Pattern


### 🏗 I. Tổng quan kiến trúc

```text
backend/
├── app/
│   ├── main.py                # FastAPI entry
│   ├── api/
│   │   └── chat.py            # /chat/stream
│   ├── core/
│   │   ├── config.py          # env, settings
│   │   └── logging.py
│   ├── ai/
│   │   ├── factory/
│   │   │   ├── llm_factory.py
│   │   │   └── embedding_factory.py
│   │   ├── llm/
│   │   │   ├── base.py        # LLM interface
│   │   │   ├── openai.py
│   │   │   └── gemini.py
│   │   ├── embeddings/
│   │   │   ├── base.py
│   │   │   ├── openai.py
│   │   │   └── gemini.py
│   │   ├── rag/
│   │   │   ├── chain.py       # LCEL chain
│   │   │   └── memory.py
│   ├── data/
│   │   ├── loader.py          # JSON → Document
│   │   └── vectorstore.py     # Chroma / FAISS
│   └── schemas/
│       └── chat.py            # Pydantic models
├── data/
│   └── vo-luyen-dinh-phong_chapters.json
├── .env
└── pyproject.toml
```

### II. Cài đặt `uv`

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Window

Dưới đây là **cách cài đặt `uv` trên Windows (chuẩn + dễ nhất)** ✅
(áp dụng tốt cho Windows 10 / 11)

---

## Cách 1 (Khuyên dùng): Cài bằng PowerShell (official)

### Bước 1: Mở PowerShell **Run as Administrator**

* Nhấn `Win`
* Gõ **PowerShell**
* Chuột phải → **Run as administrator**

### Bước 2: Chạy lệnh cài đặt

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

⏳ Đợi vài giây là xong.

---

### Bước 3: Kiểm tra

```powershell
uv --version
```

Nếu ra version → 🎉 **OK**

---

## Cách 2: Cài bằng Scoop (nếu bạn dùng Scoop)

```powershell
scoop install uv
```

Kiểm tra:

```powershell
uv --version
```

---

## Cách 3: Cài bằng Cargo (ít dùng, không khuyên)

```powershell
cargo install uv
```

❌ Chỉ dùng nếu bạn đã có Rust sẵn.

---

## Fix lỗi thường gặp trên Windows ⚠️

### 1. `uv` không nhận lệnh (PATH issue)

Chạy:

```powershell
$env:Path
```

Nếu **không có**:

```
C:\Users\<your-user>\.local\bin
```

➡️ Thêm PATH thủ công:

**Control Panel → System → Advanced system settings → Environment Variables**

Thêm:

```
C:\Users\<your-user>\.local\bin
```

👉 Restart PowerShell

---

### 2. Lỗi execution policy

Nếu gặp lỗi kiểu *“running scripts is disabled”*:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```


### Kiểm tra

```bash
uv --version
```


## Chạy nhanh
> Tạo file .env.local từ file .env.
> 
> Thay `GEMINI_API_KEY` | `OPENAI_API_KEY` | `LANGSMITH_API_KEY`

```bash
# Backend
cd backend
uv venv
source .venv/bin/activate

## run once first
uv add fastapi uvicorn langchain langchain-community langchain-core \
        langchain-openai langchain-text-splitters langchain-google-genai \
        chromadb langsmith pydantic python-dotenv

uvicorn app.main:app --reload


# Test API
curl -X POST http://localhost:8000/chat/stream \
  -H "Content-Type: application/json" \
  -d '{
    "sessionId": "test1",
    "question": "xxxxx"
  }'
```

---
