from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY  # Import API key

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
            ("system", "You are a helpful AI therapist providing mental health support."),
            ("human", user_message),
        ]
        ai_response = self.llm.invoke(messages)
        return ai_response.content
