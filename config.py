import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("⚠️ GOOGLE_API_KEY is missing. Please set it in the .env file.")
