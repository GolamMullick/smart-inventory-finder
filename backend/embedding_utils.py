from sentence_transformers import SentenceTransformer

# Use a small, fast model
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_query(text):
    return model.encode([text])[0]
