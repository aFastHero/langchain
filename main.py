import os
import dotenv
import weaviate
# from langchain.vectorstores.weaviate import Weaviate
from langchain.vectorstores import Weaviate

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

vectorstore = Weaviate(client, "AutoGpt", "text")

query = "What is AutoGPT?"
docs = vectorstore.similarity_search_by_vector()

print(docs.page_content)