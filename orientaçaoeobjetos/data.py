#criar a propriedade dataNascimento
#e verificar se a dataNascimento não é igual ao dio atual
from datetime import datetime
dataAtual = datetime.today().strftime('%d/%m/%Y')


class Data:
    def __init__(self,dataNascimento ):
       self.__dataNascimento = dataNascimento
    
    def verificaData (self):
        if dataAtual >= self.__dataNascimento:
            print('Data de nascimento não pode ser ingual ou maior que a data atual.')
        else:
           print('Data salva com sucesso.')    
            

       