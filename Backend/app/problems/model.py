import random
import math


# Classe base utilizada para compartilhar as regras de dificuldade para a soma e subtração
class BaseProblem:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def difficult_level(self):
        if self.difficulty == "easy":
            return 0, 100

        elif self.difficulty == "medium":
            return 101, 1000

        elif self.difficulty == "hard":
            return 1001, 99999

        raise ValueError("Invalid difficulty")


# Gera problemas de soma
class SumProblem(BaseProblem):

    def generate(self):

        first_value, last_value = self.difficult_level()

        x = random.randint(first_value, last_value)
        y = random.randint(first_value, last_value)

        return {
            "problem_type": "sum",
            "difficulty": self.difficulty,
            "payload": {
                "x": x,
                "y": y
            }
        }


# Gera problemas de subtração
class SubProblem(BaseProblem):

    def generate(self):

        first_value, last_value = self.difficult_level()

        x = random.randint(first_value, last_value)
        y = random.randint(first_value, last_value)

        return {
            "problem_type": "subtraction",
            "difficulty": self.difficulty,
            "payload": {
                "x": x,
                "y": y
            }
        }


# Gera problemas de multiplicação
class MulProblem(BaseProblem):

    def generate(self):

        first_value, last_value = self.difficult_level()

        x = random.randint(first_value, last_value)
        y = random.randint(first_value, last_value)

        return {
            "problem_type": "multiplication",
            "difficulty": self.difficulty,
            "payload": {
                "x": x,
                "y": y
            }
        }


# Gera problemas de divisão
class DivProblem(BaseProblem):

    def generate(self):

        # No nível fácil as divisões SEMPRE possuem resultado inteiro
        if self.difficulty == "easy":

            while True:

                y = random.randint(2, 10)

                quotient = random.randint(1, 10)

                # Aqui a lógica é invertida, adquirindo primeiro o dividendo, ou seja, eu obtenho primeiro o resultado da conta para depois gerar ela, garantindo assim que nunca exista uma divisão nula, por exemplo: 5 / 0
                x = y * quotient

                if x > y:

                    return {
                        "problem_type": "division",
                        "difficulty": self.difficulty,
                        "payload": {
                            "x": x,
                            "y": y
                        }
                    }

        # Aqui segue a lógica anterior, porém há 40% de chance de divisões com resultados em números decimais de até 1 casa decimal
        elif self.difficulty == "medium":

            while True:

                y = random.randint(2, 50)

                if random.random() < 0.6:

                    quotient = random.randint(2, 50)

                    x = y * quotient

                else:

                    x = random.randint(10, 1000)

                    # Evita que o ramo decimal gere uma divisão inteira
                    if x % y == 0:
                        continue

                if x > y:

                    return {
                        "problem_type": "division",
                        "difficulty": self.difficulty,
                        "payload": {
                            "x": x,
                            "y": y
                        }
                    }

        # Aqui os números decimais podem ter até 2 casas.
        elif self.difficulty == "hard":

            while True:

                y = random.randint(3, 100)

                integer_of_result = random.randint(5, 50)

                decimal_part = round(
                    random.uniform(0.11, 0.99),
                    2
                )

                quotient = integer_of_result + decimal_part

                x = y * quotient

                # Garante que o dividendo seja um número inteiro
                if not float(x).is_integer():
                    continue

                x = int(x)

                if x > y:

                    return {
                        "problem_type": "division",
                        "difficulty": self.difficulty,
                        "payload": {
                            "x": x,
                            "y": y
                        }
                    }

        raise ValueError("Invalid difficulty")


# Gera problemas de sequência de Fibonacci. Cada nível equivale a um tamanho de sequência que vai de x valor até y valor. Isso faz com que a dificuldade seja dinâmica e não repetitiva ainda nos mesmos níveis.
class FibonacciProblem(BaseProblem):

    def generate(self):

        if self.difficulty == "easy":
            sequence_size = random.randint(1, 10)

        elif self.difficulty == "medium":
            sequence_size = random.randint(10, 20)

        elif self.difficulty == "hard":
            sequence_size = random.randint(21, 30)

        else:
            raise ValueError("Invalid difficulty")

        sequence = [0, 1]

        # Cada novo elemento é obtido pela soma dos dois anteriores. Poderia ter utilizado o x, y = y, x + y porém é menos legível
        while len(sequence) < sequence_size:

            sequence.append(
                sequence[-1] + sequence[-2]
            )

        answer = sequence[-1]

        # Substitui o último elemento da sequência por um "?" que será substituído pela resposta do usuário
        sequence[-1] = "?"

        return {
            "problem_type": "fibonacci",
            "difficulty": self.difficulty,
            "payload": {
                "sequence": sequence
            }
        }


# Gera problemas de máximo divisor comum
class MDCProblem(BaseProblem):

    def generate(self):

        if self.difficulty == "easy":

            x = random.randint(10, 30)
            y = random.randint(10, 30)

            return {
                "problem_type": "mdc",
                "difficulty": self.difficulty,
                "payload": {
                    "values": [x, y]
                }
            }

        elif self.difficulty == "medium":

            x = random.randint(30, 100)
            y = random.randint(30, 100)

            return {
                "problem_type": "mdc",
                "difficulty": self.difficulty,
                "payload": {
                    "values": [x, y]
                }
            }

        elif self.difficulty == "hard":

            x = random.randint(50, 200)
            y = random.randint(50, 200)
            z = random.randint(50, 200)

            return {
                "problem_type": "mdc",
                "difficulty": self.difficulty,
                "payload": {
                    "values": [x, y, z]
                }
            }

        raise ValueError("Invalid difficulty")


# Gera problemas de mínimo múltiplo comum
class MMCProblem(BaseProblem):

    def generate(self):

        if self.difficulty == "easy":

            x = random.randint(2, 15)
            y = random.randint(2, 15)

            return {
                "problem_type": "mmc",
                "difficulty": self.difficulty,
                "payload": {
                    "values": [x, y]
                }
            }

        elif self.difficulty == "medium":

            x = random.randint(10, 40)
            y = random.randint(10, 40)

            return {
                "problem_type": "mmc",
                "difficulty": self.difficulty,
                "payload": {
                    "values": [x, y]
                }
            }

        elif self.difficulty == "hard":

            x = random.randint(20, 60)
            y = random.randint(20, 60)
            z = random.randint(20, 60)

            return {
                "problem_type": "mmc",
                "difficulty": self.difficulty,
                "payload": {
                    "values": [x, y, z]
                }
            }

        raise ValueError("Invalid difficulty")
    