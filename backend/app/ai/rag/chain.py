from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from app.ai.llm.openai import OpenAILLM
from app.ai.prompts.chat_prompt import get_chat_prompt_template

def build_rag_chain(llm, retriever):

    def format_docs(docs):
        return "\n\n".join(d.page_content for d in docs)

    pick_question = RunnableLambda(lambda x: x["question"])

    prompt = get_chat_prompt_template()

    return (
        {
            "context": pick_question | retriever | format_docs,
            "question": lambda x: x["question"],
            "chat_history": lambda x: x.get("chat_history", ""),
        }
        | prompt
        | llm
    )
