# Chatbot Intelligent avec RAG et LangChain

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
├── ingestion/                         # Scripts pour l'ingestion des documents
│   ├── chunker.py                     # Segmentation des documents
│   ├── document_loader.py             # Chargement des documents PDF
│   ├── indexer.py                     # Création de l'index vectoriel
│   └── text_processor.py              # Nettoyage et préparation du texte
│
├── .env                               # Variables d'environnement
├── .gitignore
├── api.py                             # Exposition avec FASTAPI
├── app.py                             # Application Streamlit principale
├── model_config.py                    # Configuration du LLM choisi
├── pipeline.py                        # Lancement du processus d'ingestion des données
├── README.md                          # Documentation du projet
├── requirements.txt                   # Dépendances du projet
├── retriever.py                       # Logique de recherche et récupération
└── vector_store.py                    # Interface avec ChromaDB
```

## Fonctionnalités
- Réponses aux questions sur les nouvelles politiques publiques sénégalaises
- Interface conversationnelle intuitive
- Base de connaissances spécialisée sur le Sénégal
- Discussion par thème

## Installation
1. Cloner le dépôt :
```bash
git clone https://github.com/tokosel/Visionsenegal2050.git
cd Visionsenegal2050

# On peut aussi dézipper le fichier zippé directement
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
streamlit run app.py
```

3. Accéder à l'interface via le navigateur :
```
http://localhost:8501
```

4. Utilisation de l'API:
```bash
# Lancement de l'API
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
#Test de l'API
http://localhost:8000/docs
```

## Auteur
### [Abdoulaye SALL](https://www.linkedin.com/in/abdoulayesall/) M2 SID UADB 2024-2025