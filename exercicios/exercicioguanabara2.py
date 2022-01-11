#faça um programa que leia nome e peso de varias pessoas guardandao tudo em uma lista no final mostra.
#quandtas pessoas foram cadastradas e uma listagem com as pessoas mais pesadas uma listagem com pessoas 
# mais leves.
informaçao = [[],[]]
opçao = 's'
while 's' == opçao:
     nome = str(input('Nome: '))
     peso = float(input('Peso: '))
     opçao = input('Deseja continuar? s/n ')
     informaçao[0].append(nome)
     informaçao[1].append(peso)

  
print(informaçao)

listaDePacientes = [['Fernando Noronha','M', 44, 1.80, 90, 'A+'], ['Gilberto Cruz','M', 60, 1.60, 100, 'O-']]

def CadastroDePaciente ():
    nome = str(input('Nome do paciente: '))
    sexo = str(input('Informe o sexo do paciente: '))
    idade = int(input('Idade do paciente: '))
    altura = float(input('Informe a altura do paciente: '))
    peso = float(input('Informe o peso do paciente: '))
    tipoSanguineo = str('Informe o tipo sanguineo do paciente: ')
    listaDePacientes.append([nome,sexo,idade, altura, peso, tipoSanguineo])
    print(listaDePacientes)

CadastroDePaciente ()    


