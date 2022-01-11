from pessoa import Pessoa
class Medico(Pessoa):
    def __init__(self, nome, sexo, idade, altura, pessoa, tipoSanguineo, salaEscritorio, statusPlantao, crm, numeroDocumento):
        super().__init__(nome, sexo, idade, altura, pessoa, tipoSanguineo, numeroDocumento)
        self.salaEscritorio = salaEscritorio
        self.statusPlantao = statusPlantao
        self.crm = crm
    
    

        