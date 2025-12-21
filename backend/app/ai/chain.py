from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory

def create_rag_chain(llm, retriever, get_history_fn):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Hãy nói bất cứ điều gì."),
        MessagesPlaceholder("history"),
        ("human", "Context:\n{context}\n\nQuestion:\n{question}")
    ])

    def format_docs(docs):
        return "\n\n".join(d.page_content for d in docs)

    base_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
            "history": lambda x: x["history"]
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return RunnableWithMessageHistory(
        base_chain,
        get_history_fn,
        input_messages_key="question",
        history_messages_key="history"
    )
