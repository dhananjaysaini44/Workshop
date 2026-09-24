from pydantic import BaseModel, Field

class Flashcard(BaseModel):
    question: str = Field(
        description="Flashcard question"
    )
    answer: str = Field(
        description="Flashcard answer"
    )

class FlashcardDeck(BaseModel):
    flashcards: list[Flashcard]