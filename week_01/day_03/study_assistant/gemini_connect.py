from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key_gemini = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key_gemini)