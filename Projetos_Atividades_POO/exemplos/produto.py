from datetime import datetime

class Produto:
    def __init__(self, nome, valido, qtde):
        self.nome = nome
        self.__validade = valido
        self._qtde = qtde

    def __validar_data(self, data_str, formato="%Y/%m/%d"):
        try:
            data = datetime.strptime(data_str, formato)
            return True
        except ValueError:
            return False

    @property
    def validade(self):
        return self.__validade

    @validade.setter
    def validade(self, validade):
        if self.__validar_data(validade):
            self.__validade = validade
            return True
        return False

    def get_qtde(self):
        return self._qtde

    def entrada_produto(self, qtde):
        if qtde > 0:
            self._qtde += qtde

    def saida_produto(self, qtde):
        if qtde <= self._qtde:
            self._qtde -= qtde
            return True
        return False

produto = Produto("Leite", "2025/09/30", 10)
produto.validade = "2025/12/31"
print(produto.validade)
