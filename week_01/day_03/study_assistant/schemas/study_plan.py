from pydantic import BaseModel

class StudyPhase(BaseModel):
    phase: str
    objective: str
    topics: list[str]
    exercises: list[str]

class StudyPlan(BaseModel):
    topic: str
    duration: str
    phases: list[StudyPhase]