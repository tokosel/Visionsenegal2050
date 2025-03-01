import sys
import os

# Ajouter le répertoire racine du projet (où se trouve "src") au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
from src.retrieval.retriever import Retriever
from src.llm.model_config import Model  # On importe Model pour utiliser la méthode generate_response

st.title("Senegal Policy Bot")

# Entrée de la question de l'utilisateur
query = st.text_input("Posez une question sur les politiques publiques sénégalaises")

if query:
    # Récupérer les documents à partir de la base de données vectorielle
    retriever = Retriever(db_path="data/vector_store/chroma_db")
    documents = retriever.retrieve_documents(query)

    # Vérifier si documents est une liste de listes et les aplatir si nécessaire
    if isinstance(documents, list):
        documents = [item for sublist in documents for item in sublist]

    # Joindre les documents dans une seule chaîne de texte
    context = "\n".join(documents)

    # Utiliser le modèle Gemini pour générer une réponse
    response = Model.generate_response(context, query)  # Appel de generate_response dans model_config.py
    
    # Afficher la réponse générée dans l'application Streamlit
    st.write(response)
