import unittest
from produto import Produto

class TestProduto(unittest.TestCase):
    def setUp(self):
        self.produto = Produto("Café", "2025/12/31", 10)

    def test_valor_inicial(self):
        self.assertEqual(self.produto._qtde, 10)

    def test_saida_valida(self):
        self.assertTrue(self.produto.saida_produto(5))
        self.assertEqual(self.produto._qtde, 5)

    def test_validade_setter(self):
        self.produto.validade = "2026/01/01"
        self.assertEqual(self.produto.validade, "2026/01/01")

if __name__ == "__main__":
    unittest.main()
