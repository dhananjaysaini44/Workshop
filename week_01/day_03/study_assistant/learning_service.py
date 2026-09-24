from prompts.study_assistant_template import (
    STUDY_ASSISTANT_SYSTEM_PROMPT,
    LEARNING_TEMPLATE
)
from schemas.learning import LearningResponse
from gemini_connect import generate_content

def learn_topic(topic: str):

    prompt = LEARNING_TEMPLATE.format(
        topic = topic
    )

    return generate_content(
        prompt = prompt, 
        system_instruction = STUDY_ASSISTANT_SYSTEM_PROMPT, 
        response_schema = LearningResponse
    )