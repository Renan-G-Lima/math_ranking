from .model import (
    SumProblem,
    SubProblem,
    MulProblem,
    DivProblem,
    FibonacciProblem,
    MDCProblem,
    MMCProblem
)


def generate_problem(problem_type, difficulty):
    try:

        problems = {
            "sum": SumProblem,
            "sub": SubProblem,
            "mul": MulProblem,
            "div": DivProblem,
            "fibonacci": FibonacciProblem,
            "mdc": MDCProblem,
            "mmc": MMCProblem,
        }

        selected_problem = problems.get(problem_type)

        if not selected_problem:
            raise ValueError("Invalid problem type")

        problem = selected_problem(difficulty)

        return problem.generate()

    except ValueError as error:

        return {
            "problem_type": None,
            "difficulty": None,
            "payload": None,
            "error": str(error),
        }
