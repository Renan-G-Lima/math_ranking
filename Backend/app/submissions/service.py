
def validate_submissions(data):
    try:
        x = int(data.get("x"))
        y = int(data.get("y"))
        answer = int(data.get("answer"))

    except (ValueError, TypeError):
        return {
            "is_correct": False,
            "correct_answer": None,
            "difficulty": None,
            "error": "Invalid input"

        }
    
    correct_answer = x + y
    is_correct = answer == correct_answer

    return {
        "is_correct": is_correct,
        "correct_answer": correct_answer if not is_correct else None,
        "difficulty": data.get("difficulty", "unknown"),
        "error": None
    }
