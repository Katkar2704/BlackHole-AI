# Configuration settings
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
    GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "blackhole_ultra_secret_99")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    DEBUG = os.getenv("ENVIRONMENT") == "development"
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")