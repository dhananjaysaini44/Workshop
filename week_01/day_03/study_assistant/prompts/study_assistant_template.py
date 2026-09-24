"""
Study Assistant Prompt Templates

Purpose:
- Learning
- Flashcards
- Quiz Generation
- Interview Preparation
- Revision Notes
- Future RAG Integration

NOTE:
Output schemas are defined separately in:

schemas/
├── flashcards.py
├── quiz.py
├── interview.py
└── learning.py
"""

# ============================================================
# SYSTEM PROMPT
# ============================================================

STUDY_ASSISTANT_SYSTEM_PROMPT = """
You are an expert teacher, tutor, mentor, and subject matter expert.

Your goal is to help students achieve deep understanding
rather than memorization.

Teaching Principles:

1. Explain concepts from first principles.
2. Prioritize intuition before technical details.
3. Use practical examples whenever possible.
4. Connect theory to real-world applications.
5. Highlight misconceptions and common mistakes.
6. Encourage critical thinking.
7. Adapt explanations to the subject matter.
8. Be accurate, educational, and objective.

When teaching:

- Start with intuition.
- Explain the concept.
- Explain how it works.
- Discuss applications.
- Discuss limitations.
- Encourage deeper thinking.

Use Bloom's Taxonomy whenever appropriate:

1. Remember
2. Understand
3. Apply
4. Analyze
5. Evaluate
6. Create
"""

# ============================================================
# LEARNING TEMPLATE
# ============================================================

LEARNING_TEMPLATE = """
TOPIC:

{topic}

TASK:

Teach this topic thoroughly using Bloom's Taxonomy.

OUTPUT FORMAT:

# Remember

- Important definitions
- Key terminology
- Important facts

# Understand

- Intuitive explanation
- Core concepts
- Why it matters

# Apply

- Practical examples
- Real-world usage
- Sample scenarios

# Analyze

- Compare with related concepts
- Tradeoffs
- Strengths and weaknesses

# Evaluate

- When should this be used?
- When should it not be used?
- Alternative approaches

# Create

- Projects
- Exercises
- Experiments
- Ideas for further exploration

# Key Takeaways

Summarize the most important points.

# Interview Questions

Generate 5 interview questions with answers.
"""

# ============================================================
# FLASHCARD TEMPLATE
# ============================================================

FLASHCARD_TEMPLATE = """
TOPIC:

{topic}

TASK:

Generate flashcards using Bloom's Taxonomy.

Coverage Requirements:

REMEMBER
- Definitions
- Terminology
- Important facts

UNDERSTAND
- Conceptual understanding
- Explanations
- Relationships

APPLY
- Practical usage
- Examples
- Problem solving

ANALYZE
- Comparisons
- Tradeoffs
- Patterns

EVALUATE
- Decision making
- Judgement
- Best practices

CREATE
- Design ideas
- Improvements
- New applications

Return data according to the Flashcard schema.
"""

# ============================================================
# QUIZ TEMPLATE
# ============================================================

QUIZ_TEMPLATE = """
TOPIC:

{topic}

TASK:

Generate a quiz using Bloom's Taxonomy.

Question Distribution:

Remember:
2 questions

Understand:
2 questions

Apply:
2 questions

Analyze:
2 questions

Evaluate:
1 question

Create:
1 question

Requirements:

- Multiple choice questions
- Four options each
- One correct answer
- Detailed explanation

Return data according to the Quiz schema.
"""

# ============================================================
# INTERVIEW TEMPLATE
# ============================================================

INTERVIEW_TEMPLATE = """
TOPIC:

{topic}

TASK:

Generate interview questions using Bloom's Taxonomy.

Question Distribution:

Remember:
2 questions

Understand:
2 questions

Apply:
2 questions

Analyze:
2 questions

Evaluate:
1 question

Create:
1 question

For each question include:

- Question
- Expected answer
- Common mistake

Return data according to the Interview schema.
"""

# ============================================================
# REVISION TEMPLATE
# ============================================================

REVISION_TEMPLATE = """
TOPIC:

{topic}

TASK:

Create a high-quality revision sheet.

Include:

# Remember
Definitions and facts

# Understand
Core concepts

# Apply
Examples and use cases

# Analyze
Comparisons and tradeoffs

# Evaluate
Strengths and weaknesses

# Create
Project ideas and exercises

Requirements:

- Concise
- Revision focused
- Exam friendly
- Well structured
"""

# ============================================================
# STUDY PLAN TEMPLATE
# ============================================================

STUDY_PLAN_TEMPLATE = """
TOPIC:

{topic}

TIME AVAILABLE:

{time_available}

TASK:

Create a study plan.

Include:

1. Learning sequence
2. Important concepts
3. Practice exercises
4. Revision schedule
5. Self-assessment checkpoints

Use Bloom's Taxonomy to progressively
increase understanding.
"""

# ============================================================
# FUTURE RAG TEMPLATE
# ============================================================

RAG_TEMPLATE = """
CONTEXT:

{context}

QUESTION:

{question}

INSTRUCTIONS:

- Use ONLY the provided context.
- Do not invent information.
- If information is unavailable, clearly state that.

OUTPUT FORMAT:

# Answer

# Supporting Evidence

# Related Concepts

# Suggested Follow-Up Questions
"""