from pydantic import BaseModel, Field

class QuizQuestion(BaseModel):
    question: str = Field(
        description="Quiz question"
    )

    options: list[str] = Field(
        description="Four answer choices"
    )

    correct_answer: str = Field(
        description="Correct answer"
    )

    explanation: str = Field(
        description="Explanation of the answer"
    )

class Quiz(BaseModel):
    quiz: list[QuizQuestion]