from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, nome: str):
        self._nome = nome
        self._ativo = False

    @property
    def nome(self):
        return self._nome

    def ativar(self):
        self._ativo = True

    def desativar(self):
        self._ativo = False

    def esta_ativo(self):
        return self._ativo

    @abstractmethod
    def operacao(self):
        pass


class SensorTemperatura(Dispositivo):
    def __init__(self, nome: str, temperatura: float = 25.0):
        super().__init__(nome)
        self._temperatura = temperatura

    def operacao(self):
        if not self._ativo:
            return "Sensor desligado"
        return f"{self.nome} mede {self._temperatura}°C"

    def set_temperatura(self, valor: float):
        self._temperatura = valor

    def get_temperatura(self):
        return self._temperatura


class AtuadorLuz(Dispositivo):
    def __init__(self, nome: str):
        super().__init__(nome)
        self._intensidade = 0  # 0 a 100%

    def operacao(self):
        if not self._ativo:
            return "Luz desligada"
        return f"{self.nome} acesa em {self._intensidade}% de intensidade"

    def ajustar_intensidade(self, valor: int):
        if 0 <= valor <= 100:
            self._intensidade = valor
        else:
            raise ValueError("Intensidade fora do intervalo permitido (0–100)")

    def get_intensidade(self):
        return self._intensidade
