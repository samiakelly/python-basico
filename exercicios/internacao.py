class Internacao:
    def __init__(self, paciente, medico, leito, dataInternacao):
       self.__paciente = paciente
       self.__medico = medico
       self.__leito = leito
       self.__dataInternacao = dataInternacao
       self.__dataAlta = None
       self.__status = True


    @property
    def paciente (self):
        return self.__paciente   