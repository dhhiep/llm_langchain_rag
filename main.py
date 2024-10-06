import os
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from dotenv import load_dotenv
from utilities.settings import settings
from langchain_community.embeddings import GPT4AllEmbeddings

load_dotenv()

# Embedding model
embedding_model = GPT4AllEmbeddings(model_file="models/all-MiniLM-L6-v2-f16.gguf")

llm = Ollama(
    base_url=os.getenv("MODEL_BASE_URL"),
    model=os.getenv("MODEL_NAME"),
    temperature=0.01,
    num_predict=2048,
    num_gpu=1,  # The number of GPUs to use. On macOS it defaults to 1 to enable metal support, 0 to disable.
)


def create_prompt(template):
    return PromptTemplate(template=template, input_variables=["context", "question"])


def create_qa_chain(llm, prompt, db):
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 10}),
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt},
        input_key="question",
    )


def main():
    template = """
    Context: {context}
    Question: {question}
    Answer: Sử dụng thông tin sau đây để trả lời câu hỏi. Nếu bạn không biết câu trả lời, hãy nói không biết, đừng cố tạo ra câu trả lời."""

    prompt = create_prompt(template)
    db = FAISS.load_local(
        settings("vector_db_path"),
        embedding_model,
        allow_dangerous_deserialization=True,
    )

    # Using the pipe operator, replacing the deprecated LLMChain
    chain = create_qa_chain(llm, prompt, db)

    questions = [
        "Mã chương ngành đào tạo toán tin là gì?",
        "Chương trình đào tạo ngành toán tin thì đào tạo ở đâu?",
        "Chương trình giảng dạy ngành toán tin, mục tiêu MT1.1 là gì?",
        "Tóm tắt cấu trúc của chương trình đào tạo",
        "Tiêu chuẩn và điều kiện làm thành viên Hội đồng quản trị",
        "Thời hạn xóa kỷ luật cho người lao động là bao lâu?",
    ]

    for question in questions:
        result = chain.invoke({"question": question})
        print("Answer: ", result)


main()
