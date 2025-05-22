from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers.prompt_router import route_prompt

app = FastAPI()

# ✅ Allow requests from frontend (localhost:5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/prompt")
async def handle_prompt(request: Request):
    data = await request.json()
    return await route_prompt(data)
