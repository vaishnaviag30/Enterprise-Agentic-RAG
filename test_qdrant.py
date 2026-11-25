
from dotenv import load_dotenv
from qdrant_client import QdrantClient
import os

load_dotenv()

url = os.getenv("QDRANT_CLUSTER_ENDPOINT")
api_key = os.getenv("QDRANT_API_KEY")

if not url or not api_key:
    print("Qdrant configuration is missing!")
    exit()

try:
    print("Connecting to Qdrant Cloud...")

    client = QdrantClient(
        url=url,
        api_key=api_key,
        timeout=20
    )

    collections = client.get_collections()

    print("Connection successful!")
    print("\nAvailable collections:")

    for collection in collections.collections:
        print("-", collection.name)

except Exception as e:
    print("\nConnection failed!")
    print(type(e).__name__, str(e))
