from random import choice

from fastapi import FastAPI

app = FastAPI(title="Random Joke API")

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the developer go broke? Because he used up all his cache.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why did Python live on land? Because it was above C-level.",
    "I told my computer I needed a break, and it said: 'No problem, I'll go to sleep.'",
]


@app.get("/joke")
def get_random_joke() -> dict[str, str]:
    return {"joke": choice(JOKES)}