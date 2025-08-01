import pandas as pd
from embedding_utils import model
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "inventory.csv")

def get_inventory():
    return pd.read_csv(DATA_PATH)

def embed_inventory(df):
    descs = df["description"].astype(str).tolist()
    return model.encode(descs)

def find_similar_items(query_emb, top_k=3):
    df = get_inventory()
    item_embeddings = embed_inventory(df)
    sims = cosine_similarity([query_emb], item_embeddings)[0]
    top_idx = sims.argsort()[-top_k:][::-1]
    results = df.iloc[top_idx].to_dict(orient="records")
    for r in results:
        r["status"] = "Low" if int(r["stock"]) < 5 else "OK"
    return results
