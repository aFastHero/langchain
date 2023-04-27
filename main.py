import os
import dotenv
import weaviate
import openai
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


from langchain.vectorstores import Weaviate
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

loader = Weaviate(client, "LangChain", "text")

# Define a query
query = "What is LangChain?"

# Get relevant documents
relevant_docs = retriever.get_relevant_documents(query)

# docs = vectorstore.similarity_search_by_vector()

# Delete all classes and objects from the schema
# client.schema.delete_all()

print(relevant_docs)