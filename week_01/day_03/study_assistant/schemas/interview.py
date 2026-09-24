from pydantic import BaseModel, Field

class InterviewQuestion(BaseModel):
    question: str = Field(
        description="Interview question"
    )

    expected_answer: str = Field(
        description="Ideal interview answer"
    )

    common_mistake: str = Field(
        description="Common mistake candidates make"
    )

class InterviewSet(BaseModel):
    interview_questions: list[InterviewQuestion]