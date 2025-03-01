# SENEGAL : JUB JUBAL JUBANTI

## Description
Ce chatbot spécialisé est conçu pour fournir des informations précises sur les nouvelles politiques publiques du Sénégal .

## Structure du Projet
```
senegal_policy_bot/
│
├── data/                              # Dossier pour les données
│   ├── raw/                           # Documents originaux
│   │   ├── agenda_senegal_2050.pdf
│   │   ├── strategie_dev_2025_2029.pdf
│   │   └── new_deal_tech.pdf
│   │
│   ├── processed/                     # Documents prétraités
│   │   ├── chunks/                    # Fichiers texte segmentés
│   │
│   └── vector_store/                  # Base de données vectorielle
│       └── chroma_db/                 # Base ChromaDB
│
├── src/                               # Code source
│   │
│   ├── ingestion/                     # Scripts pour l'ingestion des documents
│   │   ├── document_loader.py         # Chargement des documents PDF
│   │   ├── text_processor.py          # Nettoyage et préparation du texte
│   │   ├── chunker.py                 # Segmentation des documents
│   │   └── indexer.py                 # Création de l'index vectoriel
│   │
│   ├── retrieval/                     # Scripts pour la récupération des informations
│   │   ├── vector_store.py            # Interface avec ChromaDB
│   │   └── retriever.py               # Logique de recherche et récupération
│   │
│   ├── llm/                           # Intégration des modèles de langage
│   │   ├── model_config.py            # Configuration du LLM choisi
│   │
│   └── app/                           # Interface utilisateur
│       └── streamlit_app.py           # Application Streamlit principale
│
├── .env                               # Variables d'environnement
├── requirements.txt                   # Dépendances du projet
├── README.md                          # Documentation du projet
└── pipeline.py                            # Point d'entrée principal
```

## Fonctionnalités
- Réponses aux questions sur les nouvelles politiques publiques sénégalaises
- Interface conversationnelle intuitive
- Base de connaissances spécialisée sur le Sénégal
- Discussion par thème

## Installation
1. Cloner le dépôt :
```bash
git clone https://github.com/votre-username/senegal_policy_bot.git
cd senegal_policy_bot
```

2. Créer un environnement :

```bash
# Avec python
# Création
python -m venv env
# Activation
.\env\Scripts\activate
```

```bash
#Avec Conda
# Création
conda create --name env python==3.10
# Activation
conda activate env
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Configurer les variables d'environnement :
- Créer un fichier `.env`
- Ajouter la clé API Google GEMINI

## Utilisation
1. Lancer le pipeline de l'ingestion des documents :
```bash
python pipeline.py
```
2. Démarrer l'application :
```bash
streamlit run src/app/streamlit_app.py
```

3. Accéder à l'interface via le navigateur :
```
http://localhost:8501
```

4. Utilisation de l'API:
```bash
# Lancement de l'API
uvicorn src.app.api:app --host 0.0.0.0 --port 8000 --reload
#Test de l'API
http://localhost:8000/docs
```

## Auteur
### Abdoulaye SALL M2 SID UADB 2024-2025