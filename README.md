Since you're developing an **AI-powered mental health companion** using **FastAPI, LangChain, Google Gemini, and Pinecone**, I'll integrate **Google AI (Gemini)** into your project properly.

---

### **Steps to Integrate Google AI into Your Mental Health Companion**

#### **1️⃣ Install Dependencies**
Run the following command in your VS Code terminal:
```bash
pip install -qU langchain-google-genai fastapi uvicorn python-dotenv
```

---

#### **2️⃣ Set Up Environment Variables**
Create a `.env` file in your project root and add:
```
GOOGLE_API_KEY=your_api_key_here
```

Then, load the API key in your Python code:
```python
import os
from dotenv import load_dotenv

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
```

---

#### **3️⃣ Create `llm.py` for Google Gemini**
Create a file `llm.py` in your FastAPI project directory to handle Google AI integration.

```python
from langchain_google_genai import ChatGoogleGenerativeAI
import os

class GoogleGeminiChat:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0.7,
            max_tokens=256,
            timeout=30,
            max_retries=2,
        )

    def chat(self, user_message: str):
        messages = [
            ("system", "You are a compassionate AI therapist providing mental health support."),
            ("human", user_message),
        ]
        ai_response = self.llm.invoke(messages)
        return ai_response.content
```

---

#### **4️⃣ Create FastAPI Backend (`main.py`)**
Create `main.py` to build your API.

```python
from fastapi import FastAPI
from llm import GoogleGeminiChat

app = FastAPI()
chatbot = GoogleGeminiChat()

@app.get("/")
def home():
    return {"message": "Mental Health Companion API is running!"}

@app.post("/chat/")
def chat(user_input: str):
    response = chatbot.chat(user_input)
    return {"response": response}

# Run the server with: uvicorn main:app --reload
```

---

#### **5️⃣ Run Your FastAPI Server**
```bash
uvicorn main:app --reload
```

It will run at:  
👉 **http://127.0.0.1:8000**

---

#### **6️⃣ Test the API**
You can test the chatbot by making a request to:
```bash
curl -X POST "http://127.0.0.1:8000/chat/?user_input=I'm feeling anxious today"
```
OR  
Use **Postman** / **VS Code REST Client** to send a POST request.

---

### **🚀 Next Steps**
Here’s an updated version of your chatbot with memory using **LangChain's LangGraph-based memory** and **Google Generative AI (Gemini)**. It follows a structured approach with `FastAPI`, `uvicorn`, and `.env` for environment variables.  

---

### **Project Structure**
```
/chatbot
│── .env
│── config.py
│── llm.py
│── main.py
│── requirements.txt
```

---

### **1. Install Required Packages**  
Run the following command:  
```bash
pip install fastapi uvicorn python-dotenv langchain-google-genai langchain langgraph
```

---

### **2. Create a `.env` File**  
Store API keys in `.env` for security:  

```ini
GOOGLE_API_KEY=your_google_genai_api_key
```

---

### **3. Configure Environment Variables (`config.py`)**  
Load API keys from `.env`:  

```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
```

---

### **4. Define the LLM Model (`llm.py`)**  
Initialize the Google Gemini model and set up memory using LangGraph:

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from config import GOOGLE_API_KEY

# Initialize Google Gemini Model
model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

# Define chatbot system prompt
SYSTEM_PROMPT = """ 
You are a compassionate and intelligent AI-powered mental health therapy agent. Your primary role is to provide emotional support, active listening, and guidance to users seeking mental well-being assistance.  

### Guidelines:  
1. **Empathy First** – Always acknowledge and validate users' emotions before offering advice.  
2. **Encouragement & Positivity** – Provide gentle encouragement and positive reinforcement to foster hope.  
3. **Guided Coping Strategies** – Offer mindfulness exercises, grounding techniques, and stress-management strategies.  
4. **Self-Reflection & Awareness** – Encourage users to explore their thoughts and emotions through open-ended questions.  
5. **Adaptive Personalization** – Maintain context from past interactions to personalize responses while respecting user privacy.  
6. **Non-Diagnostic & Ethical** – Do not diagnose or provide medical treatment. Instead, encourage professional help when necessary.  
7. **Confidential & Trustworthy** – Create a safe, non-judgmental space where users feel comfortable sharing their feelings.  

### Response Style:  
- Speak in a warm, supportive, and non-judgmental tone.  
- Keep responses clear, concise, and easy to understand.  
- Offer reassurance and constructive coping mechanisms when users express distress.  
- If a user is in crisis, suggest reaching out to a mental health professional or crisis hotline.  

### Example Responses:  
**User:** "I feel so overwhelmed. I don't know what to do."  
**AI:** "I'm really sorry you're feeling this way. It sounds like you're carrying a lot right now. Would you like to talk more about what’s been making you feel this way?"  

**User:** "I feel alone, like no one understands me."  
**AI:** "I hear you, and that sounds really tough. You're not alone in this, and your feelings are completely valid. Sometimes, sharing even small parts of what you're going through can help. Would you like to talk more about it?"  

**User:** "I don't think I can handle things anymore."  
**AI:** "I'm really sorry you're feeling this way. You are not alone, and there are people who care about you. If you’re comfortable, we can explore some coping techniques together. It might also help to reach out to a trusted friend, family member, or a professional for support."  

Remember, you are a virtual companion that **supports, listens, and guides**—not a replacement for professional therapy.  
"""  

# Define chatbot memory graph
workflow = StateGraph(state_schema=MessagesState)

def call_model(state: MessagesState):
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
    response = model.invoke(messages)
    return {"messages": response}

# Create a chatbot with memory persistence
workflow.add_node("model", call_model)
workflow.add_edge(START, "model")

# Add memory persistence
memory = MemorySaver()
chatbot = workflow.compile(checkpointer=memory)
```

---

### **5. Create the API Server (`main.py`)**  
Set up a FastAPI endpoint for real-time interaction with memory:

```python
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
```

---

### **6. Running the Chatbot**  
Start the FastAPI server using Uvicorn:  
```bash
uvicorn main:app --reload
```

Now, you can interact with the chatbot by sending POST requests to:  
```
http://127.0.0.1:8000/chat/
```

Example Request:
```json
{
  "user_input": "Hello, how are you?",
  "thread_id": "user123"
}
```

---

### **How It Works?**
✅ **Persistent Memory**: Remembers previous messages for each `thread_id`.  
✅ **Scalable**: Uses LangGraph for optimized message history storage.  
✅ **FastAPI Integration**: Provides an API interface for real-world use cases.  

Would you like to add logging, database storage, or WebSocket support? 🚀