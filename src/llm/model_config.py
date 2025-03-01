import os
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
# Configuration de l'API Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Utilisation de votre clé API Gemini

class Model:
    @staticmethod
    def generate_response(context, query):
        """Utilise Gemini pour générer une réponse basée sur le contexte et la question"""
        
        prompt = f"""Tu es un expert en politiques publiques sénégalaises. 
        Réponds à la question suivante en utilisant le contexte fourni :

        Contexte : {context}

        Question : {query}

        Réponse :"""

        model = genai.GenerativeModel("gemini-1.5-flash-8b-exp-0827")  # Spécifiez le modèle Gemini à utiliser
        response = model.generate_content(prompt)
        return response.text
