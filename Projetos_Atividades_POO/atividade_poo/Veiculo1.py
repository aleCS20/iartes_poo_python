# Classe base
class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca          # Atributo protegido (encapsulamento)
        self._modelo = modelo        # Atributo protegido

    def descrever(self):
        return f"{self._marca} {self._modelo}"

    def ligar_motor(self):
        return "O motor está ligado (genérico)"

# Subclasse Carro herdando de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas        # Atributo protegido

    def ligar_motor(self):  # sobrescrita de método (polimorfismo)
        return "O motor do carro está ligado. VRUM VRUM!"

    def descrever(self):  # sobrescrita de método (opcional, mostra herança + polimorfismo)
        return f"Carro: {self._marca} {self._modelo}, {self._portas} portas"

# Subclasse Moto herdando de Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self._cilindradas = cilindradas  # Atributo protegido

    def ligar_motor(self):  # sobrescrita de método
        return "O motor da moto está ligado. VRAAAAP!"

    def descrever(self):
        return f"Moto: {self._marca} {self._modelo}, {self._cilindradas}cc"

# Demonstração de polimorfismo
veiculos = [
    Carro("Toyota", "Corolla", 4),
    Moto("Honda", "CB500", 500)
]

# Executando os métodos em loop
for veiculo in veiculos:
    print(veiculo.descrever())
    print(veiculo.ligar_motor())
