from abc import abstractmethod
from pessoa import Pessoa
class Paciente(Pessoa):
    def __init__(self, nome , sexo , idade , altura, peso, tipoSanguineo, numeroDocumento  ):
       super().__init__(nome, sexo, idade, altura, peso , tipoSanguineo, numeroDocumento)
       self.__statusInternacao = False
       self.__statusGravidade = 0
       
    
    @abstractmethod
    def imprimir(pacientes):
        print(f'{"Cadastro de pacientes":^58}')
        print('-'*62)
        print('    Nome        Sexo    idade  Altura   Peso   Tipo sanguineo ')
        for paciente in pacientes:
            print(f'{paciente.nome.ljust(17)} {paciente.sexo.ljust(7)} {paciente.idade:<5} {(paciente.altura):>2.2f} {paciente.peso:>8.2f} {paciente.tipoSanguineo :>10}')
        print('-'*62)
    
    def internar(self, statusGravidade):
        if self.__statusInternacao == True:
            print('O paciente ja está internado') 
            return
        self.__statusGravidade = statusGravidade

    def alta(self, internacoes):
        if self.__statusGravidade > 1: 
            print('Nivel de gravidade do paciente não permite alta.')
            return
        if  not self.__verificaINternacao(internacoes):
            print(f'O paciente {self.nome} não está internado.')
            return      
        else:
            self.__statusInternacao = False
            print(f'Foi dado alta para o paciente {self.nome}')

    def __verificaINternacao(self, internacoes): 
        for internacao in internacoes:
           if internacao.paciente.nome == self.nome:
              return True        

              

   
      
       
        
       