from dotenv import load_dotenv
from qdrant_client import QdrantClient
import os

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_CLUSTER_ENDPOINT"),
    api_key=os.getenv("QDRANT_API_KEY")
)

info = client.get_collection("enterprise_rag")

print("Collection:", "enterprise_rag")
print("Status:", info.status)
print("Collection details:")
print(info.model_dump())