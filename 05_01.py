import os
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = ChatOpenAI(
    model='o4-mini-2025-04-16'
)

pdf_path = 'laptop_manual.pdf'
loader = PyPDFLoader(pdf_path)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    length_function=len
)

chunks = text_splitter.split_documents(
    documents=docs,
)

embedding = OpenAIEmbeddings()

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    collection_name='laptop_manual',
)

retriever = vector_store.as_retriever()

result = retriever.invoke('Qual é o tamanho do disco rígido?')

print(result)