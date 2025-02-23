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
✅ **Integrate RAG (Pinecone) for personalized responses**  
✅ **Enhance responses with psychological frameworks (e.g., CBT, MBTI)**  
✅ **Integrate with Flutter frontend**

Would you like me to add **memory or emotion tracking**? Let me know your next goal! 😊