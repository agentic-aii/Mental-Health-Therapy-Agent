from fastapi import FastAPI
from pydantic import BaseModel
from llm import GoogleGeminiChat

# Initialize FastAPI
app = FastAPI()
chat_model = GoogleGeminiChat()

# Request model
class ChatRequest(BaseModel):
    message: str

# Endpoint for AI chat
@app.post("/chat")
async def chat(request: ChatRequest):
    response = chat_model.chat(request.message)
    return {"response": response}
