from langchain_community.vectorstores import PGVector
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate
from langchain.chains import  ConversationalRetrievalChain ,RetrievalQA
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyAUUVD99_AFxmOXyRB99wPVN6ZctbSh7c8"

chain_type="stuff" #  map_reduce, refine , map-rerank # Detaylar için https://towardsdatascience.com/4-ways-of-question-answering-in-langchain-188c6707cc5a
search_type = "similarity" #'similarity', 'similarity_score_threshold', 'mmr' detaylar için #https://medium.com/tech-that-works/maximal-marginal-relevance-to-rerank-results-in-unsupervised-keyphrase-extraction-22d95015c7c5
prompt_template = """
    1- Aşağıdaki bağlamları kullanarak soruyu yanıtlayın.
    2- Sağlanan bağlamdan en ayrıntılı şekilde soruyu yanıtlayın.
    3- Cevap sağlanan bağlamda yoksa, "Üzgünüm cevabı bulamadım..." demelisiniz.
    4- Cevap sağlanan bağlamda varsa, daha detaylı ve açıklanır şekilde cevap ver.
    5- Yanıt Türkçe olmalıdır.
    Context:\n {context}\n
    Question: \n{question}\n
  """


file_name = os.listdir("data")



embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")


# model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
# model_kwargs = {"device": "cpu"}
# encode_kwargs = {"normalize_embeddings": True}
#
# hf = HuggingFaceBgeEmbeddings(
#      model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
# )

CONNECTION_STRING = "postgresql+psycopg2://postgres:root@localhost:5432/vector_db"
COLLECTION_NAME = input("Your document: ")




store = PGVector(
    connection_string=CONNECTION_STRING,
    embedding_function=embeddings,
    collection_name=COLLECTION_NAME,
)



retriever = store.as_retriever(search_type=search_type, search_kwargs={"k": 5})
llm = Ollama(model="gemma2", temperature=0.2)

prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])

retrievalQA = RetrievalQA.from_llm(llm=llm, retriever=retriever,prompt=prompt)



is_chat_open = True
while is_chat_open:
    _prompt = input("\nYour question: ")
    if _prompt == "exit":
        is_chat_open = False
    else:
        print(retrievalQA.run(_prompt))