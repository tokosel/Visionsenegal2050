from src.retrieval.vector_store import VectorStore

class Retriever:
    def __init__(self, db_path):
        self.vector_store = VectorStore(db_path)

    def retrieve_documents(self, query):
        """Récupère les documents pertinents pour la requête."""
        return self.vector_store.search(query)
