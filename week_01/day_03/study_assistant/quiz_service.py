from prompts.study_assistant_template import (
    STUDY_ASSISTANT_SYSTEM_PROMPT,
    QUIZ_TEMPLATE
)
from schemas.quiz import Quiz
from gemini_connect import generate_content

def quiz_topic(topic: str):

    prompt = QUIZ_TEMPLATE.format(
        topic = topic
    )

    return generate_content(
        prompt = prompt, 
        system_instruction = STUDY_ASSISTANT_SYSTEM_PROMPT, 
        response_schema = Quiz
    )