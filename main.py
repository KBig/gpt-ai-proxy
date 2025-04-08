from fastapi import FastAPI, Request
import httpx
import os
from fastapi.responses import PlainTextResponse

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_URL = "https://api.openai.com/v1/chat/completions"

@app.post("/chat")
async def proxy_to_openai(req: Request):
    body = await req.json()

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(OPENAI_URL, headers=headers, json={
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": body["prompt"]}],
            "temperature": 0.7,
            "max_tokens": 1500
        })

        gpt_reply = response.json()
        content = gpt_reply["choices"][0]["message"]["content"]
        return PlainTextResponse(content)
