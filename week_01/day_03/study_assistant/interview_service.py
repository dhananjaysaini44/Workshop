from prompts.study_assistant_template import (
    STUDY_ASSISTANT_SYSTEM_PROMPT,
    INTERVIEW_TEMPLATE
)
from schemas.interview import InterviewSet
from gemini_connect import generate_content

def interview_topic(topic: str):

    prompt = INTERVIEW_TEMPLATE.format(
        topic = topic
    )

    return generate_content(
        prompt = prompt, 
        system_instruction = STUDY_ASSISTANT_SYSTEM_PROMPT, 
        response_schema = InterviewSet
    )