from datetime import datetime
from conta import Conta
dataAtual = datetime.today().strftime('%d/%m/%Y')

class ContaPoupança(Conta):
    _dataNascimento = None
    def __init__(self, banco, agencia, numero, nome, saldo = float(1)):
            super().__init__(banco, agencia, numero, nome, saldo)
           
      

    def depositar(self, valor):
         super().depositar(valor)
         self.render()
         print('Valor depositado com sucesso.')

    def render(self):
        self._creditaSaldo(0.05)   

    def imprimir(self): 
        print(f'Banco: {self.banco}\nAgencia: {self.agencia}\nNumero: {self.numero}\nNome: {self.nome}\nSaldo: {self.saldo}')     
        print('->'*15)


         