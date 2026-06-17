import google.generativeai as genai
import chromadb
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
client = chromadb.PersistentClient(path=os.getenv("CHROMA_PERSIST_DIR"))

def chunk(text:str) ->list[str]:
    chunk_size = 500
    overlap = 50
    chunks = []
    for i in range(0 , len(text), chunk_size - overlap):
        chunks.append(text[i:i+chunk_size])
    return chunks
         
def embed_and_store(chunks : list[str], collection_name: str) -> None:
    collection = client.get_or_create_collection(collection_name)
    for i, embed in enumerate(chunks):
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=embed
        )
        vector = result["embedding"]
    collection.add(
    documents=[embed],
    embeddings=[vector],
    ids=[str(i)]
        )



