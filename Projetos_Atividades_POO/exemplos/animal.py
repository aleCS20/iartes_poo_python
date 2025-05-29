class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som genérico"

class Cachoro(Animal):
    def emitir_som(self):
        return "Au au"

class Gata(Animal):
    def emitir_som(self):
        return "Miau miau"

def chamando_animais(animal:Animal):
    animal.emitir_som()

animais = [Cachoro("Rex"), Gata("Mini"), Animal("Ser")]

for animalx in animais:
    print(f"{animalx.nome} diz : {animalx.emitir_som()}")
    chamando_animais(animalx)
