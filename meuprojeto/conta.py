from datetime import datetime
dataAtual = datetime.today().strftime('%d/%m/%Y')

class Conta:
    __dataNascimento = None
    def __init__(self, banco, agencia, numero, nome, saldo = float(1)):
            self.__banco = banco
            self.__agencia = agencia
            self.__numero = numero
            self.__nome = nome
            self.__saldo = saldo

    @property
    def nome (self):
        return self.__nome.title()
    @property
    def saldo(self):
        return self.__saldo 

    @property
    def dataNascimento(self):
        return self.__dataNascimento
    
    @dataNascimento.setter
    def dataNascimento(self, data):
        if (self.verificaData(data)):
            self.__dataNascimento = data
        else:
            print("Data de nascimento inválida")
    
    def verificaSaldo (self,valor):
        if  valor > self.__saldo:
            self.imprimeSaldo()
            return False
        else:  
            return True     
    
    def sacar (self, valor):
        if self.verificaSaldo(valor):
            self.__saldo -= valor      

    def imprimeSaldo(self):
        print(f'Seu saldo atual é: {self.__saldo}')

    def depositar (self, valor):
        self.__saldo += valor
           

    def  transferir (self, contaDestino, valor):
        if self.verificaSaldo(valor):
           self.sacar(valor)
           contaDestino.depositar(valor)
           print('Valor transferido com sucesso')


    def verificaData (self, dataNascimento):
        if dataAtual <= dataNascimento:
            return False
        return True
            
                
    def _debitaSaldo(self, valor):
        self.__saldo -= valor       

    def _creditaSaldo(self, valor):
        self.__saldo += valor

        


        
