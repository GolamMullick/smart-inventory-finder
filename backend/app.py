from fastapi import FastAPI, Query
from embedding_utils import embed_query
from search import find_similar_items, get_inventory
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Node-RED/frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_item(q: str):
    emb = embed_query(q)
    results = find_similar_items(emb)
    return results

@app.get("/status")
def get_status():
    """Return a summary: True if any item is low in stock."""
    df = get_inventory()
    low_stock = df[df['stock'] < 5]
    return {"low_stock": len(low_stock) > 0, "count": len(low_stock)}

@app.get("/inventory")
def inventory():
    df = get_inventory()
    return df.to_dict(orient="records")
