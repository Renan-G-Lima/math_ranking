import random
from .model import problems_mock

def spitter_of_sums():
    problems = problems_mock[0]
    value_x = random.randint(0, 9)
    value_y = random.randint(0, 9)
    question = problems["question"].format(value_x, value_y)

    return {
        "id": problems["id"],
        "question": question,
        "difficulty": problems["difficulty"],
        "x": value_x,
        "y": value_y
    }
