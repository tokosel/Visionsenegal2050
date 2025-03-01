import os
import openai

openai.api_key = os.getenv("DEEPSEEK_API_KEY")

class Model:
    @staticmethod
    def generate_response(prompt):
        """Utilise DeepSeek pour générer une réponse."""
        response = openai.ChatCompletion.create(
            model="deepseek-r1:671b",
            messages=[{"role": "system", "content": "Réponds en te basant uniquement sur les documents fournis."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
