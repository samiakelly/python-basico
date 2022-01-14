#classe utilizaçao de herença da primeira classe conta.

from datetime import datetime
from conta import Conta
dataAtual = datetime.today().strftime('%d/%m/%Y')

class ContaPoupança(Conta):
    _dataNascimento = None
    def __init__(self, banco, agencia, numero, nome, limite = float(1), saldo = float(1)):
            super().__init__(banco, agencia, numero, nome, saldo)
            self.__limite = limite
      

    def depositar(self, valor):
         super().depositar(valor)
         self.render()
         print('Valor depositado com sucesso.')

    def render(self):
        self._creditaSaldo(0.05)     



         