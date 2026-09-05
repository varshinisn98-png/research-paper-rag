import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN was not found in .env")

client = InferenceClient(
    api_key=HF_TOKEN
)


def generate_answer(question, context):

    prompt = f"""
You are a research paper assistant.

Answer the question using ONLY the information in the context below.

If the answer is not available in the context, say:
"The answer is not available in the provided research paper."

Context:
{context}

Question:
{question}

Give a clear and concise answer.
"""

    response = client.chat_completion(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content