from fastapi import FastAPI
from boggle_bot.models import ChatRequest
from dotenv import load_dotenv

import openai
import os

load_dotenv() #this loads from dot env

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: ChatRequest):
    response = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": request.message}]
    )
    return {"response": response.choices[0].message.content}


