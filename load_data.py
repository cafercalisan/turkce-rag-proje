import os
from langchain import hub
import os
from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader, PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import PGVector
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import re

os.environ["GOOGLE_API_KEY"] = "AIzaSyAUUVD99_AFxmOXyRB99wPVN6ZctbSh7c8"


file_name = os.listdir("data")

# prompt = hub.pull("rlm/rag-prompt")

load_dotenv()

bolunmus_dokuman = []

def metin_önişleme(documents):
    for i in range(len(documents)):
        documents[i].page_content = re.sub(r'\.{2,}', '.', documents[i].page_content)
        documents[i].page_content = documents[i].page_content.replace("\n"," ")
        documents[i].page_content = re.sub(r'\s{3,}', " ",documents[i].page_content)
    return documents


loader = PDFMinerLoader("data/" + file_name[0])
data = loader.load()
data = metin_önişleme(data)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024,chunk_overlap=200 , length_function = len)
docs = text_splitter.split_documents(data)
for k in range(len(docs)):
    bolunmus_dokuman.append(docs[k])


embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
# model_kwargs = {"device": "cpu"}
# encode_kwargs = {"normalize_embeddings": True}
#
# hf = HuggingFaceBgeEmbeddings(
#      model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
# )

CONNECTION_STRING = "postgresql+psycopg2://postgres:root@localhost:5432/vector_db"
COLLECTION_NAME = f'{file_name[0]}'


db = PGVector.from_documents(
    embedding=embeddings,
    documents=bolunmus_dokuman,
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING
)

similar = db.similarity_search_with_score("What did the president say about Russia", k=5)
