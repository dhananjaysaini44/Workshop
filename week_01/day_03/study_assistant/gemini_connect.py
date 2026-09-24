from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
from google.genai.errors import ServerError, APIError
import time

load_dotenv()

api_key_gemini = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key_gemini)

model_fallback = [os.getenv("GEMINI_MODEL", "gemini-3.7-flash")
                , "gemini-3.6-flash"
                , "gemini-3.5-flash"]

def generate_content(prompt: str, system_instruction: str, response_schema: str):
    
    last_exception = None

    for model_name in model_fallback:
        max_tries = 3
        delay = 2

        for attempt in range(max_tries):

            try:
                response = client.generate_content(
                    model = model_name,
                    contents = prompt,
                    config = types.GenerateContentConfig(
                        system_instruction = system_instruction,
                        response_mime_type = "application/json",
                        response_schema = response_schema
                    )
                )
                return response.parsed
                
            except (ServerError, APIError) as e:
                last_exception = e
                if hasattr(e, "code") and e.code in (503, 500, 429):
                    print(f"Attempt {attempt+1}/{max_tries} Model {model_name} Busy/Unavailable... retrying in {delay}")

                    time.sleep(delay)
                    delay *= 2
                
                else:
                    break
            
            raise last_exception or RuntimeError("Failed to load all the Gemini models")