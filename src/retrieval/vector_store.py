import os
os.environ["SQLITE_EXPERIMENTAL"] = "1"  # Permet d'utiliser une version récente si disponible
import chromadb

class VectorStore:
    def __init__(self, db_path):
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_collection("senegal_policies")

    def search(self, query, k=5):
        """Recherche les documents les plus pertinents."""
        results = self.collection.query(query_texts=[query], n_results=k)
        return results["documents"]
