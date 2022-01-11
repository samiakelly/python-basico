import time
listaDePacientes = [['Fernando Noronha','M', 44, 1.80, 90, 'A+'], ['Gilberto Cruz','M', 60, 1.60, 100, 'O-']]

def listaPacienteIndice (listaDePacientes):
    print(f'{"Cadastro de pacientes":^58}')
    print('-'*62)
    print('       Nome         Sexo   idade   Altura   Peso   Tipo sanguineo       ')
    for i, nome in enumerate(listaDePacientes):
       print(f'{[i]}{listaDePacientes[i][0].ljust(17)} {listaDePacientes[i][1].ljust(7)} {listaDePacientes[i][2]:<5} {(listaDePacientes[i][3]):>2.2f} {listaDePacientes[i][4]:>8.2f} {listaDePacientes[i][5]:>10}')
    print('-'*62) 


def CadastroDePaciente ():
    nome = str(input('Nome do paciente: '))
    time.sleep(1)
    sexo = str(input('Informe o sexo do paciente: '))
    time.sleep(1)
    idade = int(input('Idade do paciente: '))
    time.sleep(1)
    altura = float(input('Informe a altura do paciente: '))
    time.sleep(1)
    peso = float(input('Informe o peso do paciente: '))
    time.sleep(1)
    tipoSanguineo = str(input('Informe o tipo sanguineo do paciente: '))
    listaDePacientes.append([nome, sexo, idade, altura, peso, tipoSanguineo])
    time.sleep(2)
    print()   
    listaPacienteIndice(listaDePacientes)
    print()
  

def AlterarCadastroCliente ():
    escolha = 'S' 
    listaPacienteIndice(listaDePacientes)
    time.sleep(1)
    while escolha == 'S':
     numero = int(input('informe o numero de cadastro do paciente que deseja fazer a alteração: '))
     time.sleep(1) 
     print(f'{"Opções":^20}')
     print('-'*20)
     print('1 - Nome  \n2 - Sexo \n3 - Idade \n4 - Altura \n5 - Peso \n6 - Tipo sanquineo')
     print('-'*20)
     time.sleep(1)
     opçoes = int(input('Qual opção deseja alterar? '))
     time.sleep(1)
     if opçoes ==1:
        novonome = str(input('Informe o novo nome que deseja colocar: '))     
        listaDePacientes[numero][0] = (novonome)
        time.sleep(1)
        listaPacienteIndice(listaDePacientes)
     elif opçoes ==2:
        novosexo = str(input('Informe o novo sexo que deseja colocar: '))
        listaDePacientes[numero][1] = (novosexo)
        time.sleep(1)
        listaPacienteIndice(listaDePacientes)
     elif opçoes ==3:
        novaidade = int(input('Informe a nova idade que deseja colocar: ')) 
        listaDePacientes[numero][2] = (novaidade)
        time.sleep(1)
        listaPacienteIndice(listaDePacientes)
     elif opçoes ==4:
        novaaltura = float(input('Informe a nova altura que deseja colocar: '))  
        listaDePacientes[numero][3] = (novaaltura)
        time.sleep(1)
        listaPacienteIndice(listaDePacientes)
     elif opçoes ==5:
        novopeso = float(input('Informe o novo peso que deseja colocar: '))
        listaDePacientes[numero][4] = (novopeso) 
        time.sleep(1)     
        listaPacienteIndice(listaDePacientes)
     elif opçoes ==6:
        novotiposanguenio = str(input('Informe o novo tipo sanguineo que deseja colocar: '))
        listaDePacientes[numero][5] = (novotiposanguenio) 
        time.sleep(1) 
        listaPacienteIndice(listaDePacientes)
     
     escolha = str(input('Deseja fazer mais alguma alteração? S/N: '))   

       

def DeletarFichaDoPaciente ():
        listaPacienteIndice(listaDePacientes)
        numero = int(input('Informe o numero de cadastro a ser removido: '))
        del(listaDePacientes[numero])
        listaPacienteIndice(listaDePacientes)

def imcPaciente ():
    listaPacienteIndice(listaDePacientes)
    numero = int(input('Informe o numéro de casdastro que deseja calcular o IMC: '))
    for i, ficha in enumerate(listaDePacientes):  
        imc = float(listaDePacientes[numero][4])/(float(listaDePacientes[numero][3])*(listaDePacientes[numero][3]))  
    print(f'{imc:.2f}')
    
    if (imc < 18.5):
        print('O paciente está na magreza!')
    elif(imc > 18.5 and imc < 24.9):
        print('O paciente está normal!')
    elif(imc > 24.9 and imc < 30):
        print('O paciente está sobrepeso!')
    else:
        print('O paciente está na obesidade!')       
        



opçao = 0
while opçao !=6:
    time.sleep(1)
    print()
    print(f'{"Menu":^28}')
    print('-'*34)
    print('1 - Cadastrar novo paciente \n2 - Alterar cadastro do Paciente \n3 - Deletar cadastro do Paciente \n4 - Listar todos os pacientes \n5 - Calcular IMC do Paciente \n6 - Sair')
    print('-'*34)
    opçao = int(input('Escolha sua opção: '))
    print('-='*32)
    time.sleep(2)
    if opçao ==1:
        CadastroDePaciente  ()
    elif opçao ==2:
        AlterarCadastroCliente ()
    elif opçao ==3:
         DeletarFichaDoPaciente ()
    elif opçao ==4:
       listaPacienteIndice(listaDePacientes)
    elif opçao ==5:
        imcPaciente ()
    elif opçao ==6:
        print('Finalizando......')    
    else:
        print('Opção invalida. Tente novamente!')


time.sleep(2)     
print('>>>>>>>>>> Fim do programa!!')


   
 


