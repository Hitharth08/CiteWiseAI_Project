import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class LLM:

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("Groq API Key not found. Check your .env file.")

        self.client = Groq(api_key=api_key)

    def generate(self, question, context):

        prompt = f"""
You are an AI Research Assistant.

Answer ONLY from the context below.

If the answer is not present, reply:
"I couldn't find this information in the provided documents."

Context:
{context}

Question:
{question}
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content