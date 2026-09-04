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
You are a research paper question-answering assistant.

Answer the question using ONLY the information provided in the context.

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

if __name__ == "__main__":
    context = """
    The present study was conducted with 120 undergraduate students
    enrolled in three different colleges affiliated to Bangalore University.
    Participants included 60 male and 60 female students aged between
    18 to 22 years, selected through random sampling technique.
    """

    question = "Who participated in the study?"

    answer = generate_answer(question, context)

    print("Question:", question)
    print("Answer:", answer)