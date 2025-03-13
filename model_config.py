import os
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
# Configuration de l'API Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class Model:
    @staticmethod
    def generate_response(context, query):
        """Utilise Gemini pour générer une réponse basée sur le contexte et la question"""
        
        prompt = f"""Tu es un assistant spécialisé dans les politiques publiques du Sénégal, 
                    particulièrement celles mises en place par le Président Bassirou Diomaye Faye 
                    et son Premier Ministre Ousmane Sonko.

                    Utilisez les informations suivantes pour répondre à la question de l'utilisateur.
                    Si tu ne trouvez pas l'information dans les passages fournis, indique-le clairement
                    sans inventer de réponse :

        Contexte : {context}

        Question : {query}

        Réponse :"""

        model = genai.GenerativeModel("gemini-1.5-flash-8b-exp-0827")
        response = model.generate_content(prompt)
        return response.text
