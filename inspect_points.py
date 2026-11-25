from dotenv import load_dotenv
from qdrant_client import QdrantClient
import os

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_CLUSTER_ENDPOINT"),
    api_key=os.getenv("QDRANT_API_KEY")
)

result = client.scroll(
    collection_name="enterprise_rag",
    limit=2,
    with_payload=True,
    with_vectors=True
)

points, next_page = result

print("Number of points retrieved:", len(points))

for point in points:
    print("\nPoint ID:", point.id)
    print("Payload:", point.payload)

    if point.vector:
        if isinstance(point.vector, dict):
            for name, vector in point.vector.items():
                print(f"Vector '{name}' dimensions:", len(vector))
        else:
            print("Vector dimensions:", len(point.vector))
    else:
        print("No vector found!")