from prompts.study_assistant_template import (
    STUDY_ASSISTANT_SYSTEM_PROMPT,
    QUIZ_TEMPLATE
)
from schemas.quiz import Quiz
from gemini_connect import client
from google.genai import types

def quiz_topic(topic: str):

    prompt = QUIZ_TEMPLATE.format(
        topic = topic
    )

    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents = prompt,
        config = types.GenerateContentConfig(
            system_instruction = STUDY_ASSISTANT_SYSTEM_PROMPT,
            response_mime_type = "application/json",
            response_schema = Quiz
        )
    )
    
    return response.parsed