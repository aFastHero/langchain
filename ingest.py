import os
import dotenv
import weaviate
# from langchain.vectorstores.weaviate import Weaviate
# from langchain.vectorstores import Weaviate

dotenv.load_dotenv()

weaviate_url = os.getenv("WEAVIATE_URL")  # Replace w/ your endpoint
weaviate_api_key = os.getenv("WEAVIATE_API_KEY")  # Replace w/ your Weaviate API Key
openai_api_key = os.getenv("OPENAI_API_KEY")  # Replace w/ your OpenAI API Key

auth = weaviate.auth.AuthApiKey(
    api_key=weaviate_api_key
)

# Instantiate the client with the auth config
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=auth
)


from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import BSHTMLLoader
from langchain.retrievers.weaviate_hybrid_search import WeaviateHybridSearchRetriever
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.schema import Document

# Instantiate the retriever
retriever = WeaviateHybridSearchRetriever(
    client=client,
    index_name = "LangChain",
    text_key = "text",
)

# Define a query
# query = "<Enter query here>"

# Add documents to the retriever
loader = BSHTMLLoader(file_path="python.langchain.com/en/latest")
raw_docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    overlap_size=200,
)
docs = text_splitter.split_documents(raw_docs)
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Add documents to the retriever
ids = retriever.add_documents(docs)

print(ids)