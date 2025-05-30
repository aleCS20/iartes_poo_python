class Produto:
    def __init__(self, nome, validade, qtde):
        self.nome = nome
        self.__validade = validade
        self._qtde = qtde

    @property
    def validade(self):
        return self.__validade

    @validade.setter
    def validade(self, nova_validade):
        # Exemplo simples sem validação real de data
        if isinstance(nova_validade, str):
            self.__validade = nova_validade

    def entrada_produto(self, qtde):
        if qtde > 0:
            self._qtde += qtde

    def saida_produto(self, qtde):
        if qtde <= self._qtde:
            self._qtde -= qtde
            return True
        return False
