from PIL import Image

import streamlit as st
from retriever import Retriever
from model_config import Model

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Senegal BOT",
    page_icon="🇸🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === SIDEBAR / MENU LATÉRAL ===
with st.sidebar:
    st.title("🇸🇳 Vision Sénégal 2050")
    
    # Logo ou image dans la sidebar
    sidebar_image = Image.open('vsn2050.jpg')
    st.image(sidebar_image, width=250)
    
    st.markdown("---")
    
    # Description du projet
    st.subheader("📝 À propos du projet")
    st.markdown("""
    Ce chatbot utilise l'intelligence artificielle pour rendre accessible les 
    nouvelles politiques publiques du Sénégal. Notre mission est d'informer 
    les citoyens sur les initiatives gouvernementales dans des domaines clés 
    pour l'avenir du pays.
    """)
    
    st.markdown("---")
    
    # Liste des fonctionnalités
    st.subheader("✨ Fonctionnalités")
    features = {
        "💬 Discussion thématique": "Posez des questions sur des thèmes spécifiques",
        "🔍 Recherche contextuelle": "Récupération d'informations précises",
        "📊 Suivi des politiques": "Informations sur les politiques en cours",
        "🌐 Données actualisées": "Base de connaissances mise à jour régulièrement"
    }
    
    for icon_feature, description in features.items():
        st.markdown(f"**{icon_feature}**: {description}")
    
    st.markdown("---")
    
    # Contact ou aide
    st.markdown("Pour toute suggestion, contactez-moi à travers le bouton ci-dessous.")
    if st.button("📧 Me contacter"):
        st.info("Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/abdoulayesall/)")
    
    # Attribution
    st.markdown("---")
    st.caption("© 2025 - Projet Vision Sénégal 2050")

# === CONTENU PRINCIPAL ===
# Titre principal
st.title("JUB JUBAL JUBANTI")
st.markdown("Ce chatbot spécialisé est conçu pour fournir des informations précises sur les nouvelles politiques publiques du Sénégal.")

# Container pour la zone de discussion
chat_container = st.container()

# Sélectionner le thème de discussion avec des émojis
theme_emojis = {
    "Souveraineté Economique": "💰",
    "Technologique Numérique": "💻",
    "Justice sociale": "⚖️"
}

theme = st.selectbox(
    "Choisissez un thème de discussion",
    list(theme_emojis.keys()),
    format_func=lambda x: f"{theme_emojis[x]} {x}"
)

st.subheader(f"Vous avez choisi le thème : {theme_emojis[theme]} {theme}")

# Liste de mots-clés pour chaque thème
keywords = {
    "Souveraineté Economique": ["économie", "vision", "souveraineté", "ressources", "industries", "indépendance économique"],
    "Technologique Numérique": ["technologie", "numérique", "digital", "innovation", "internet", "technologique"],
    "Justice sociale": ["justice", "égalité", "droits humains", "discrimination", "justice sociale", "inégalité"]
}

# Zone interactive de chat
with chat_container:
    # Initialiser l'historique de chat dans la session si ce n'est pas déjà fait
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Afficher l'historique de chat
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"<div style='background-color:#121936;padding:10px;border-radius:5px;margin-bottom:10px;'><strong>👤 Vous:</strong> {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color:#121936;padding:10px;border-radius:5px;margin-bottom:10px;'><strong>🤖 SenegalBot:</strong> {message['content']}</div>", unsafe_allow_html=True)

    # Suggestions de questions basées sur le thème
    theme_suggestions = {
        "Souveraineté Economique": [
            "Quelles sont les politiques pour renforcer la souveraineté économique?",
            "Comment le Sénégal développe-t-il ses industries locales?"
        ],
        "Technologique Numérique": [
            "Quelles initiatives numériques sont en cours au Sénégal?",
            "Comment la technologie est-elle intégrée dans l'administration?"
        ],
        "Justice sociale": [
            "Quelles mesures sont prises pour réduire les inégalités?",
            "Comment le gouvernement améliore-t-il l'accès à l'éducation?"
        ]
    }
    
    # Afficher les suggestions
    if st.session_state.chat_history == []:
        st.markdown("#### 💡 Suggestions de questions:")
        cols = st.columns(2)
        for i, suggestion in enumerate(theme_suggestions[theme]):
            if cols[i % 2].button(suggestion, key=f"suggestion_{i}"):
                st.session_state.question = suggestion

# Fonction pour vérifier si la question est liée au thème
def is_question_relevant(question, theme):
    # Convertir la question en minuscule pour une comparaison non sensible à la casse
    question = question.lower()
    # Vérifier si un mot-clé du thème est présent dans la question
    for keyword in keywords.get(theme, []):
        if keyword.lower() in question:
            return True
    return False

# Champ de saisie pour la question avec mémorisation
if "question" not in st.session_state:
    st.session_state.question = ""

# Interface de saisie de question
question = st.text_input(
    label="Posez votre question",
    value=st.session_state.question,
    key="question_input",
    placeholder=f"Posez une question sur {theme}...",
)

# Mémoriser la question
if question != st.session_state.question:
    st.session_state.question = question

# Traitement de la soumission
if st.button("💬 Envoyer", use_container_width=True) and question:
    # Ajouter la question à l'historique
    st.session_state.chat_history.append({"role": "user", "content": question})
    
    # Vérifier la pertinence
    if not is_question_relevant(question, theme):
        response = f"Votre question ne semble pas être liée au thème '{theme}'. Pourriez-vous reformuler ou choisir une question en lien avec ce thème? Vous pouvez utiliser des mots-clés comme: {', '.join(keywords[theme])}"
        st.session_state.chat_history.append({"role": "assistant", "content": response})
    else:
        # Utilisation du Retriever pour récupérer les documents en fonction de la question
        with st.spinner("🤖 Recherche d'informations en cours..."):
            retriever = Retriever(db_path="data/vector_store/chroma_db")
            documents = retriever.retrieve_documents(question)
            
            # Aplatir la liste de documents si nécessaire
            if isinstance(documents, list):
                # Si des sous-listes existent, les aplatir
                documents = [item for sublist in documents for item in (sublist if isinstance(sublist, list) else [sublist])]

            # Joindre les documents dans une seule chaîne de caractères
            context = "\n".join(documents)

            # Utilisation du modèle pour générer la réponse
            response = Model.generate_response(context, question)
            
            # Ajouter la réponse à l'historique
            st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    # Réinitialiser le champ de question après soumission
    st.session_state.question = ""
    
    # Recharger la page pour afficher le nouveau message
    st.rerun()

# Bouton pour effacer l'historique
if st.session_state.chat_history:
    if st.button("🧹 Effacer l'historique", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()