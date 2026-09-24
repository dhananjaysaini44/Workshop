from prompts.study_assistant_template import (
    STUDY_ASSISTANT_SYSTEM_PROMPT,
    FLASHCARD_TEMPLATE
)
from schemas.flashcards import FlashcardDeck
from gemini_connect import generate_content

def flashcard_topic(topic: str):

    prompt = FLASHCARD_TEMPLATE.format(
        topic = topic
    )

    return generate_content(
        prompt = prompt, 
        system_instruction = STUDY_ASSISTANT_SYSTEM_PROMPT, 
        response_schema = FlashcardDeck
    )