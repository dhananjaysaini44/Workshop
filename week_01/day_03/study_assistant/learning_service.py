from prompts.study_assistant_template import (
    STUDY_ASSISTANT_SYSTEM_PROMPT,
    LEARNING_TEMPLATE
)
from schemas.learning import LearningResponse
from gemini_connect import client
from google.genai import types

def learn_topic(topic: str):

    prompt = LEARNING_TEMPLATE.format(
        topic = topic
    )

    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents = prompt,
        config = types.GenerateContentConfig(
            system_instruction = STUDY_ASSISTANT_SYSTEM_PROMPT,
            response_mime_type = "application/json",
            response_schema = LearningResponse
        )
    )
    
    return response.parsed