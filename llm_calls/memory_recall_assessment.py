from openai import OpenAI

async def memory_assessment():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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"
    )

    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo-0613",
        messages=[
            {
                "role": "user",
                "content": """Generate a paragraph of approximately 100 words that contains enough information to create six MCQs, such that these 6 MCQs will be asked from the generated paragraph.

The paragraph should contain facts, events, and relationships that can be recalled directly or with slight inference.

There should be 2 easy, 2 medium, and 2 hard multiple-choice questions,all of them shuffled with no sub topics as easy, hard, medium . 

Easy: Direct recall of explicit facts from the paragraph.
Medium: Requires slight inference or understanding of relationships. 
Hard: Requires deeper memory and indirect recall.

Important: The six MCQs must be randomly shuffled in the final output, with no order based on difficulty level.

Each question should have 4 answer choices, one correct answer, and a difficulty level. the difficulty level should be numbers 1 for easy, 3 for medium, 5 for hard. and correct answer should have only the option a,b,c or d not the whole answer.

the response should be in the following json format exactly.
{{
    "paragraph": "generated paragraph",
    "questions": [ 
        {{
            "question": "Your question here",
            "choices": [
                ["A", "Your first choice here"],
                ["B", "Your second choice here"],
                ["C", "Your third choice here"],
                ["D", "Your fourth choice here"]
            ],
            "correct_answer": "Correct choice letter (e.g., 'A')",
            "difficulty": "Choose from: 1,3,5"
        }}
    ]
}}

"""
            }
        ]
    )

    return completion.choices[0].message.content