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
from langchain.document_loaders import ReadTheDocsLoader
from langchain.retrievers.weaviate_hybrid_search import WeaviateHybridSearchRetriever
from langchain.vectorstores import Weaviate
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
# loader = ReadTheDocsLoader("python.langchain.com/en/latest", features="html.parser")
loader = BSHTMLLoader("python.langchain.com/en/latest/")
raw_docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
docs = text_splitter.split_documents(raw_docs)

added = retriever.add_documents(docs)

vectorstore = Weaviate(client, "LangChain", "text")

# Instantiate the embeddings
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

embedding = vectorstore.from_documents(docs, embeddings)

# Add documents to the retriever
# added = vectorstore.from_documents(docs, embeddings)


print("Done!")
