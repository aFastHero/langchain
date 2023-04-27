import os
import dotenv
import weaviate

dotenv.load_dotenv()

weaviate_url = os.getenv("WEAVIATE_URL")
weaviate_api_key = os.getenv("WEAVIATE_API_KEY")

auth = weaviate.AuthApiKey(api_key=weaviate_api_key)

client = weaviate.Client(url=weaviate_url, auth_client_secret=auth)

# Create a new class
schema = client.schema.get()

print(schema)
