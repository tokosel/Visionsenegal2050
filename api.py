from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.retrieval.retriever import Retriever
from src.llm.model_config import Model

app = FastAPI()

# Définition du modèle pour recevoir les requêtes
class QueryRequest(BaseModel):
    question: str

@app.post("/api")
def query_model(request: QueryRequest):
    """Endpoint pour récupérer une réponse basée sur la question de l'utilisateur."""
    
    question = request.question
    retriever = Retriever(db_path="data/vector_store/chroma_db")
    
    # Récupérer les documents pertinents
    documents = retriever.retrieve_documents(question)

    # Aplatir la liste de documents si nécessaire
    if isinstance(documents, list):
        documents = [item for sublist in documents for item in (sublist if isinstance(sublist, list) else [sublist])]

    # Joindre les documents en une seule chaîne pour le contexte
    context = "\n".join(documents)

    # Générer la réponse avec Gemini
    response = Model.generate_response(context, question)

    if not response:
        raise HTTPException(status_code=500, detail="Erreur dans la génération de réponse.")

    return {"question": question, "response": response}

