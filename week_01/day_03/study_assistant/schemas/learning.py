from pydantic import BaseModel

class LearningResponse(BaseModel):
    remember: str
    understand: str
    apply: str
    analyze: str
    evaluate: str
    create: str
    key_takeaways: list[str]
    interview_questions: list[str]