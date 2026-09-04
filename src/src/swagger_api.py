**👤 MEMBER 8 – SWAGGER API / API DOCUMENTATION**

### 🎯 Your Task

You are responsible for the **Swagger API part** of our Research Paper RAG project.

Your file is:

```text
src/swagger_api.py
```

Your job is to make sure our RAG system can be accessed through an API and tested easily using **Swagger UI**.

### 1. What should happen?

The user should be able to:

```text
Open Swagger UI
      ↓
Enter a question
      ↓
Click Execute
      ↓
RAG pipeline processes the question
      ↓
ChromaDB retrieves relevant chunks
      ↓
LLM generates answer
      ↓
Swagger displays the result
```

### 2. Check the existing `swagger_api.py`

If it is empty or incomplete, use this simple structure:

```python
from fastapi import FastAPI
from pydantic import BaseModel

from src.rag_pipeline import rag_pipeline


app = FastAPI(
    title="Research Paper RAG API",
    description="Question Answering API for a Research Paper using RAG",
    version="1.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Research Paper RAG API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    result = rag_pipeline(
        request.question
    )

    return result
```

### 3. Start the API

From the project root, run:

```bash
python -m uvicorn src.swagger_api:app --reload
```

If our project currently uses `api.py` as the main API file, **do not change it without checking with the team lead first**.

Our current working API may already be:

```text
api.py
```

So the main goal is to make sure `swagger_api.py` and the existing API setup do not conflict.

### 4. Open Swagger UI

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

You should see:

```text
Research Paper RAG API
```

and an endpoint similar to:

```text
POST /ask
```

### 5. Test `/ask`

Click:

```text
POST /ask
→ Try it out
```

Enter:

```json
{
  "question": "Who participated in the study?"
}
```

Click:

```text
Execute
```

The response should contain:

```json
{
  "question": "Who participated in the study?",
  "answer": "...",
  "retrieved_chunks": [...]
}
```

The answer should identify the **20 Polish university students of English philology**.

### 6. Test another question

Try:

```json
{
  "question": "What methodology was used in this research?"
}
```

The response should contain an answer related to the **semi-structured interview**.

### 7. Check API validation

Also test an empty question:

```json
{
  "question": ""
}
```

The API should handle it properly. Don't add complicated validation unless necessary.

### 8. Important

Swagger UI is only the interface for testing our API.

Do NOT put:

* ChromaDB logic
* embedding logic
* PDF extraction logic
* LLM prompt logic

inside `swagger_api.py`.

Those already belong to other modules.

Your job is only to connect the API request to the existing RAG pipeline.

### 9. Do NOT modify other modules

Only work on:

```text
src/swagger_api.py
```

Do NOT modify:

```text
src/pdf_extractor.py
src/chunking.py
src/embeddings.py
src/chromadb_store.py
src/retrieval.py
src/llm.py
src/rag_pipeline.py
main.py
api.py
```

**If `api.py` is currently required for Swagger to work, ask the team lead before changing it.**

### 10. GitHub

After completing the task:

```bash
git add src/swagger_api.py
git commit -m "Connect RAG to Swagger API"
git push
```

Then send in the group:

**"Member 8 task completed – Swagger API tested successfully."**

### 🔗 Your part of the RAG pipeline

```text
User
  ↓
Swagger UI
  ↓
swagger_api.py       ← YOUR TASK
  ↓
rag_pipeline.py
  ↓
retrieval.py
  ↓
ChromaDB
  ↓
Relevant Chunks
  ↓
llm.py
  ↓
Final Answer
  ↓
Swagger Response
```

**Important:** Keep it simple. Swagger UI + FastAPI is enough for our professor's requirement. Do not add a frontend or another API framework.
