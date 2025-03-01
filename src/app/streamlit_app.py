import sys
import os
from PIL import Image

# Ajouter le répertoire racine du projet (où se trouve "src") au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
from src.retrieval.retriever import Retriever
from src.llm.model_config import Model

# Charger l'image du Sénégal
image = Image.open('src/app/vsn2050.jpg')  # Remplacez par le chemin de l'image du Sénégal

# Configuration de la page Streamlit
st.set_page_config(page_title="Senegal Bot", page_icon="🇸🇳", layout="wide")
st.title("Les Nouvelles Politiques Publiques Sénégalaises")
# Disposition de l'image et du thème côte à côte
col1, col2 = st.columns([2, 3])  # col1 prendra 1 part de l'espace, col2 prendra 2 parts

with col1:
    st.image(image, width=300)  # Largeur ajustée

with col2:
    # Sélectionner le thème de discussion
    theme = st.selectbox(
        "Choisissez un thème de discussion",
        ["Souveraineté Economique","Technologique Numérique", "Justice sociale"]
    )
    st.subheader(f"Vous avez choisi le thème : {theme}")

# Titre et champ de saisie pour la question


question = st.text_input("", key="question_input",placeholder="Entrez ici votre question ...")

# Initialiser un espace pour la réponse
response = None

# Vérifier si une réponse est déjà stockée dans la session
if 'response' in st.session_state:
    response = st.session_state.response

# Bouton pour poser la question
if st.button("Soumettre") and question:
    # Utilisation du Retriever pour récupérer les documents en fonction de la question
    retriever = Retriever(db_path="data/vector_store/chroma_db")
    documents = retriever.retrieve_documents(question)
    
    # Aplatir la liste de documents si nécessaire
    if isinstance(documents, list):
        # Si des sous-listes existent, les aplatir
        documents = [item for sublist in documents for item in (sublist if isinstance(sublist, list) else [sublist])]

    # Joindre les documents dans une seule chaîne de caractères
    context = "\n".join(documents)

    # Utilisation du modèle Gemini pour générer la réponse
    response = Model.generate_response(context, question)  # Passer context ET question à generate_response

    # Sauvegarder la réponse dans la session
    st.session_state.response = response

# Affichage de la réponse (si une réponse est générée)
if response:
    st.subheader("Réponse :")
    st.write(f"**Question :** {question}")
    st.write(f"**Réponse :** {response}")
