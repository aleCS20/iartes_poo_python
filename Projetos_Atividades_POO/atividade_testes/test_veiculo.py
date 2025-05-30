import unittest
from Veiculo import Veiculo, Carro, Moto

class TestVeiculo(unittest.TestCase):

    def setUp(self):
        self.carro = Carro("Chevrolet", "Cruze", 4)
        self.moto = Moto("Honda", "CB550", 650)

    # teste 1---> para verificar se o metodo ligar_motor esta de acordo com a saida
    def test_ligar_motor(self):
        self.assertEqual(self.carro.ligar_motor(), "O motor do carro está ligado agora"
                                                   " (VRUM) (VRUM)")
        self.assertEqual(self.moto.ligar_motor(), "O motor da moto está ligado agora"
                                                  " (VRAAPP) (VRAAPP)")

    # teste 2---> para verificar se as características e comportamentos estao sendo alterados
    def test_descrever_modelo(self):
        descricao_carro = self.carro.descrever_modelo()
        descricao_moto = self.moto.descrever_modelo()
        self.assertIn("Chevrolet", descricao_carro)
        self.assertIn("Cruze", descricao_carro)
        self.assertIn("Honda", descricao_moto)
        self.assertIn("CB550", descricao_moto)

    # teste 3---> verificando o encampsulamento e controle dos atributos
    def test_get_modelo(self):
        self.assertEqual(self.carro.get_modelo(), "Cruze")
        self.assertEqual(self.moto.get_modelo(), "CB550")

    # teste 4---> teste do metodo tipo_combustivel
    def test_tipo_combustivel(self):
        self.assertEqual(self.carro.tipo_combustivel(), "Gasolina ou Etanol")
        self.assertEqual(self.moto.tipo_combustivel(), "Gasolina comum ou aditivada")

if __name__ == '__main__':
    unittest.main()