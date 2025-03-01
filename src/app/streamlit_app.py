import sys
import os
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
from src.retrieval.retriever import Retriever
from src.llm.model_config import Model

# Charger l'image du Sénégal
image = Image.open('src/app/vsn2050.jpg')

# Configuration de la page Streamlit
st.set_page_config(page_title="Senegal BOT", page_icon="🇸🇳", layout="wide")
st.title("Les Nouvelles Politiques Publiques Sénégalaises")
st.markdown(f"Ce chatbot spécialisé est conçu pour fournir des informations précises sur les nouvelles politiques publiques du Sénégal .")
# Disposition de l'image et du thème côte à côte
col1, col2 = st.columns([2, 4])

with col1:
    st.image(image, width=300)

with col2:
    # Sélectionner le thème de discussion
    theme = st.selectbox(
        "Choisissez un thème de discussion",
        ["Souveraineté Economique", "Technologique Numérique", "Justice sociale"]
    )
    st.subheader(f"Vous avez choisi le thème : {theme}")

# Liste de mots-clés pour chaque thème
keywords = {
    "Souveraineté Economique": ["économie", "vision","souveraineté", "ressources", "industries", "indépendance économique"],
    "Technologique Numérique": ["technologie", "numérique", "digital", "innovation", "internet", "technologique"],
    "Justice sociale": ["justice", "égalité", "droits humains", "discrimination", "justice sociale", "inégalité"]
}

# Champ de saisie pour la question
question = st.text_input(" ", key="question_input", placeholder="Entrez ici votre question ...")

# Fonction pour vérifier si la question est liée au thème
def is_question_relevant(question, theme):
    # Convertir la question en minuscule pour une comparaison non sensible à la casse
    question = question.lower()
    # Vérifier si un mot-clé du thème est présent dans la question
    for keyword in keywords.get(theme, []):
        if keyword.lower() in question:
            return True
    return False

# Initialiser un espace pour la réponse
response = None

# Vérifier si une question a été posée et si elle est liée au thème choisi
if st.button("Soumettre") and question:
    if not is_question_relevant(question, theme):
        st.warning("Veuillez poser une question en lien avec le thème choisi.")
    else:
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
        response = Model.generate_response(context, question)

# Affichage de la réponse
if response:
    st.markdown(f"🤖 {response}")
