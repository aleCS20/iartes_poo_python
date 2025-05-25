class Animal:
    def __init__(self, nome):
        self._nome = nome

    def emitir_som(self):
        return "Som genérico"

    def get_nome(self):
        return self._nome

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"

class Gata(Animal):
    def emitir_som(self):
        return "Miau"
