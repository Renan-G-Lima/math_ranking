import random

# Cria a classe para gerar problemas de soma
class CreatorSumProblem:
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

    def sum_generator(self):
        first_value, last_value = self.difficult_level()

        x = random.randint(first_value, last_value)
        y = random.randint(first_value, last_value)

        return {
            "operation": "+",
            "x": x,
            "y": y,
            "difficulty": self.difficulty,
        }

    def sub_generator(self):
        first_value, last_value = self.difficult_level()

        x = random.randint(first_value, last_value)
        y = random.randint(first_value, last_value)

        return {
            "operation": "-",
            "x": x,
            "y": y,
            "difficulty": self.difficulty,
        }
    
    def mul_generator(self):
         first_value, last_value = self.difficult_level()

         x = random.randint(first_value, last_value)
         y = random.randint(first_value, last_value)

         return {
                "operation": "*",
                "x": x,
                "y": y,
                "difficulty": self.difficulty,
         }
    
    def div_generator(self):
         # No nível fácil, as divisões são simples onde todos os resultados são inteiros
        if self.difficulty == "easy":
            y = random.randint(2, 10)
            quotient = random.randint(1, 10)

            # Para garantir que o valor de X seja sempre maior/igual a Y estamos atribuindo a X o valor randômico de Y * Q (quociente), com isso sabemos o resultado antes mesmo do cálculo existir de verdade.
            x = y * quotient

            # Se o valor de X for igual a Y ou maior que 1000, geramos um novo problema
            if x <= y or x > 1000:
                return self.div_generator()

            return {
                "operation": "/",
                "x": x,
                "y": y,
                "difficulty": self.difficulty,
            }
         # Os valores máximos sobem até 50 elevando a dificuldade
        elif self.difficulty == "medium":
            y = random.randint(2, 50)

            # O nível médio na verdade é dado por tudo o que estava no nível easy + 40% de probabilidade de ter divisões onde o resultado é um valor decimal
            if random.random() < 0.6:
                quotient = random.randint(2, 50)
                x = y * quotient
            else:
                x = random.randint(10, 1000)

                if x %  y == 0:
                    return self.div_generator()

            if x <= y or x > 1000:
                return self.div_generator()

            return {
                "operation": "/",
                "x": x,
                "y": y,
                "difficulty": self.difficulty,
            }

        
            # No nível hard os valores sobem até 100 e resultados podem ter até 2 casas decimais após a vírgula

            """
            não esta funcionando corretamente ainda
            """
        
        elif self.difficulty == "hard":
            y = random.randint(3, 100)

            # Recebe a parte inteira do resultado
            integer_of_result = random.randint(5, 50)
            # recebe a parte fracionada que fica entre 0.11 e 0.99
            decimal_part = round(random.uniform(0.11, 0.99), 2)

            # Somamos as duas e atribuímos ao Quociente, definindo assim o resultado da divisão para construir a conta
            quotient = integer_of_result + decimal_part

            # Antes que a conta exista realmente, já obtemos o valor de X nesse ponto para poder controlar a dificuldade real do calculo
            x = y * quotient

            # Garante que X é um valor inteiro
            if not float(x).is_integer():
                return self.div_generator()
            
            x = int(x)

            if x <= y or x > 1000:
                return self.div_generator()

            return {
                "operation": "/",
                "x": x,
                "y": y,
                "difficulty": self.difficulty,
            }
        
        else:
            raise ValueError("Invalid difficulty")
        
        """
        Necessário alterar o submission pois o mesmo vai quebrar por não estar preparado para aceitar valores float
        """