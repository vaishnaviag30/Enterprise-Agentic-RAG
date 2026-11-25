from dotenv import load_dotenv
from qdrant_client import QdrantClient
from app.services.retrieval.embedding import embed_query
import os

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_CLUSTER_ENDPOINT"),
    api_key=os.getenv("QDRANT_API_KEY")
)

query = "How does Kubernetes recover failed jobs?"

print("Generating query embedding...")

vector = embed_query(query)

print("Embedding dimensions:", len(vector))

print("Searching Qdrant...")

results = client.query_points(
    collection_name="enterprise_rag",
    query=vector,
    limit=3,
    with_payload=True
)

for point in results.points:
    print("\nScore:", point.score)
    print("Source:", point.payload.get("source"))
    print("Text:", point.payload.get("text", "")[:300])