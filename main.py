from fastapi import FastAPI
from pydantic import BaseModel
from llm import chatbot
from langchain_core.messages import HumanMessage

app = FastAPI()

class ChatRequest(BaseModel):
    user_input: str
    thread_id: str  # Unique ID for each conversation session

@app.post("/chat/")
async def chat(request: ChatRequest):
    """Handles chatbot conversation requests"""
    response = chatbot.invoke(
        {"messages": [HumanMessage(content=request.user_input)]},
        config={"configurable": {"thread_id": request.thread_id}}
    )
    return {"response": response["messages"][-1].content}

@app.get("/")
async def home():
    return {"message": "AI Chatbot with Memory is Running!"}
