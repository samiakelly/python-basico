#classe utilizaçao de herença da primeira classe conta.

from datetime import datetime
from conta import Conta
dataAtual = datetime.today().strftime('%d/%m/%Y')

class ContaCorrente(Conta):
    _dataNascimento = None
    def __init__(self, banco, agencia, numero, nome, limite = float(1), saldo = float(1)):
            super().__init__(banco, agencia, numero, nome, saldo)
            self.__limite = limite
    
    
    def verificaSaldo(self, valor):
        valor_a_verficar = self.saldo + self.__limite
        if valor > valor_a_verficar:
            return False
        return True 

    def sacar (self, valor):
        if self.verificaSaldo(valor):
           super().sacar(valor)
           self.tarifar()
        else:
            print("Saldo insuficiente!")

    def tarifar (self):
       self._debitaSaldo(0.10)        

            

    
                
           
        
