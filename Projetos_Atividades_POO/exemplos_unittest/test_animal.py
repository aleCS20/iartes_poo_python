import unittest

from Projetos_Atividades_POO.exemplos_unittest.animal import Animal

class TestAnimal(unittest.TestCase):

    # Teste de comportamento esperado
    def test_emitir_som_com_energia_suficiente(self):
        animal = Animal("Cachorro", energia=50)
        resultado = animal.emitir_som()
        self.assertEqual(resultado, "Cachorro emite um som!")

    # Teste de alteração de estado interno
    def test_alteracao_estado_energia_apos_emitir_som(self):
        animal = Animal("Gato", energia=100)
        energia_antes = animal.get_energia()
        animal.emitir_som()
        energia_depois = animal.get_energia()
        self.assertEqual(energia_depois, energia_antes - 10)

    # Teste de encapsulamento via propriedade
    def test_encapsulamento_nome_com_setter_valido(self):
        animal = Animal("Passaro")
        animal.nome = "Papagaio"
        self.assertEqual(animal.nome, "Papagaio")

    # Teste de encapsulamento: setter inválido
    def test_setter_nome_invalido(self):
        animal = Animal("Pombo")
        with self.assertRaises(ValueError):
            animal.nome = ""

if __name__ == "__main__":
    unittest.main()