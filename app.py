from fastapi import FastAPI, Request
from routers.prompt_router import route_prompt

app = FastAPI()

@app.post("/prompt")
async def handle_prompt(request: Request):
    data = await request.json()
    return await route_prompt(data)