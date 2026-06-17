import google.generativeai as genai
import os 
import chromadb


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
client = chromadb.PersistentClient(path=os.getenv("CHROMA_PERSIST_DIR"))

def retrieve (query : str,collection_name : str, top_k: int=5) -> list[str]:
    collection = client.get_or_create_collection(collection_name)
    result = genai.embed_content(
            model= "models/text-embedding-004",
            content = query
        )
    vector = result["embedding"]
    results = collection.query(
            query_embeddings = [vector],
            n_results = top_k
        )
    return results["documents"][0]