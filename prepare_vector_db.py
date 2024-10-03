import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.embeddings import OllamaEmbeddings
from utilities.settings import settings
from dotenv import load_dotenv

load_dotenv()

# Embedding model
embedding_model = OllamaEmbeddings(
    base_url=os.getenv("MODEL_BASE_URL"),
    model=os.getenv("MODEL_NAME"),
)


# embeddings
def load_pdf_to_vector_db():
    # Load data
    loader = DirectoryLoader(settings("pdf_path"), glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    # Split the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    # Store the data to vector db
    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local(settings("vector_db_path"))

    return db


load_pdf_to_vector_db()
