import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from groq import Groq

load_dotenv()

app = FastAPI(title="Groq Joke API")


def generate_joke(topic: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Missing GROQ_API_KEY in environment")

    client = Groq()
    model = os.getenv("GROQ_MODEL", "gpt-oss-20b")

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a concise joke writer."},
            {"role": "user", "content": f"Write one short, funny joke about {topic}."},
        ],
        temperature=0.8,
        max_tokens=100,
    )

    joke = completion.choices[0].message.content
    if not joke:
        raise HTTPException(status_code=502, detail="LLM returned an empty joke")

    return joke.strip()


@app.get("/joke")
def get_joke(topic: str = Query(..., min_length=1, description="Topic for the joke")) -> dict[str, str]:
    return {"topic": topic, "joke": generate_joke(topic)}