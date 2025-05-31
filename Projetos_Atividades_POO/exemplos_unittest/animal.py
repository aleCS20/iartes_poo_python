
class Animal:
    def __init__(self, nome: str, energia: int = 100):
        self._nome = nome
        self._energia = energia

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self._nome = novo_nome
        else:
            raise ValueError("Nome inválido...")

    def emitir_som(self):
        if self._energia >= 10:
            self._energia -= 10
            return f"{self._nome} emite um som!"
        return f"{self._nome} esta sem energia!"

    def alimentar(self, quantidade: int):
        if quantidade > 0:
            self._energia += quantidade

    def get_energia(self):
        return self._energia
