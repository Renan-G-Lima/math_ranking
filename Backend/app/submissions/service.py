# valida a submissão garantindo a veracidade dos valores e operador recebido
def validate_submission(data):
    try:
        x = int(data.get("x"))
        y = int(data.get("y"))
        answer = float(data.get("answer"))
        operation = data.get("operation")

    except (ValueError, TypeError):
        return {
            "is_correct": False,
            "correct_answer": None,
            "difficulty": None,
            "error": "Invalid input",
        }
    
    # Recebe o JSON que até o momento é uma string e torna ele em uma operação executável
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        """
        Até aqui a divisão continua quebrando o código quando chamada
        """
        "/": lambda x, y: round(x / y, 2),
    }

    # valida se o operador recebido é válido
    if not (operation_func := operations.get(data.get("operation"))):
        return {
            "is_correct": False,
            "correct_answer": None,
            "difficulty": None,
            "error": "Invalid operation",
        }

    correct_answer = operation_func(x, y)

    if operation == "/":
        is_correct = round(answer, 2) == correct_answer
    # aqui ainda será criada uma condicional para validar a integridade
    # ainda não compreendi como utilizar eficientemente a função built-in isinstance (validação do tipo dos valores)
    #
    else:
        is_correct = answer == correct_answer


    return {
        "is_correct": is_correct,
        "correct_answer": correct_answer if not is_correct else None,
        "difficulty": data.get("difficulty", "unknown"),
        "error": None,
    }
