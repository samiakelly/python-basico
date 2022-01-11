from internacao import Internacao
from paciente import Paciente
from medico import Medico


paciente1 = Paciente('Samia Kelly', 'F', 23, 1.69, 62.30, 'not', 2008435502)
paciente2 = Paciente('Pedro Henrrique', 'M', 23, 1.78, 73.23, ' A+', 90876456)
medico1 = Medico('João Raimundo', 'M', 45, 1.68, 65.45,'A+','sala de cima', True, 20987, 134098765)
intenacao = Internacao(paciente1, medico1, 208, '22/10/2021')
internacoes = []
internacoes.append(intenacao)

paciente1.alta(internacoes)



