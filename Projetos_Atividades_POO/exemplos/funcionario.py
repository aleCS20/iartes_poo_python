class Funcionario:
    def __init__(self, salario):
        self.__salario = salario

    def __calcular_bonus(self):
        return self.__salario * 0.10

    def aumentar_salario(self, percentual):
        if percentual > 0:
            aumento = self.__salario * (percentual / 100)
            self.__salario += aumento
            print(f"O salário aumentado em {percentual}% : "
                  f"Salario com Aumento: R$ {self.__salario:.2f}")
        else:
            print("Percentual inválido!")

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        if valor > 0:
            self.__salario = valor
        else:
            print("Salario não pode ser negativo!")

    def exibir_bonus(self):
        bonus = self.__calcular_bonus()
        print(f"Bonus salarial: R$ {bonus:.2f}")

funcionario = Funcionario(5000)

print(f"Salario atual: R$ {funcionario.salario:.2f}")

funcionario.exibir_bonus()
funcionario.aumentar_salario(15)
funcionario.salario = -100
funcionario.salario = 6000

print(f"Salario atualizado: R$ {funcionario.salario:.2f}")


