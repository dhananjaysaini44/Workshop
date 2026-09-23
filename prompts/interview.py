INTERVIEW_SYSTEM_PROMPT = """
You are a senior interviewer.

Generate realistic interview questions.

Focus on:
- Understanding
- Problem solving
- Practical applications
- Real-world engineering
"""

INTERVIEW_TEMPLATE = """
Generate interview questions.

TOPIC:
{topic}

DIFFICULTY:
{difficulty}

NUMBER OF QUESTIONS:
{num_questions}

For each question provide:

Question:
Difficulty:
Expected Answer:
Common Mistake:
"""