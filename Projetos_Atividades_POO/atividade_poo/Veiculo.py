#Aplicando Conceitos de POO em Python
#ALESSANDRO BARBOSA de OLIVEIRA

## ================ Classe base Superclasse ==================================== ##
class Veiculo:
    def __init__(self, marca, modelo):
        # encampsulamento (protegido e privado)
        self._marca = marca
        self.__modelo = modelo

    def descrever_modelo(self):
        return f"{self._marca} : {self.__modelo}"

    def ligar_motor(self):
        return "O motor está ligando agora e funcionando (genérico)"

    # metodo a ser sobrescrito pelas subclasses  com o uso de polimorfismo
    def tipo_combustivel(self):
        return "Tipo de combustível genérico"

    def get_modelo(self):
        return self.__modelo

# ======================================================================= #
## ================ Classe herdeira sublasses ============================ ##
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        # encapsulamento (protegido)
        self._portas = portas

    # sobrescrita de metodo com o uso de polimorfismo
    def ligar_motor(self):
        return "O motor do carro está ligado agora (VRUM) (VRUM)"

    # sobrescrita de metodo com o uso de herança e polimorfismo
    def descrever_modelo(self):
        return f"Carro: {self._marca} Modelo: {self.get_modelo()} Portas: {self._portas}"

    # sobrescrita de metodo com o uso de polimorfismo
    def tipo_combustivel(self):
        return "Gasolina ou Etanol"

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        # encapsulamento (protegido)
        self._cilindradas = cilindradas

    # sobrescrita de metodo com o uso de polimorfismo
    def ligar_motor(self):
        return "O motor da moto está ligado agora (VRAAPP) (VRAAPP)"

    # sobrescrita de metodo com o uso de herança e polimorfismo
    def descrever_modelo(self):
        return f"Moto: {self._marca} Modelo: {self.get_modelo()} Cilindradas: {self._cilindradas} cc"

    # sobrescrita de metodo com o uso de polimorfismo
    def tipo_combustivel(self):
        return "Gasolina comum ou aditivada"

# ======================================================================= #

# Lista de veículos com dois carros e duas motos para instanciar
veiculos = [
    Carro("Chevrolet", "Cruze", 4),
    Moto("Honda", "CB550", 500),
    Carro("Volkswagen", "Golf", 4),
    Moto("Yamaha", "MT-03", 321)
]

# Execução dos métodos com polimorfismo
print("*************** Veículos cadastrados *********************")
for veiculo in veiculos:
    print(veiculo.descrever_modelo())
    print(veiculo.ligar_motor())
    print(f"Combustível: {veiculo.tipo_combustivel()}")
    print("*" * 50)
# ======================================================================= #
