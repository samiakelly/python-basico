#crie um Menu 1 - Salvar novo cliente 2 - Alterar nome cliente 3 - Deletar cliente
# 4 - Listar todos os clientes 5 - sair
import time
listadeclientes = ['Fernando Noronha', 'Gilberto Cruz', 'Amanda Beatriz']

def SalvarNomeCliente  ():
    nome = str(input('Nome do cliente: '))
    listadeclientes.append(nome)

def AlterarNomeCliente ():
    nome = str(input('Nome do cliente que deseja alterar: '))
    indice = listadeclientes.index(nome)
    novonome = str(input('Informe o novo nome do cliente: '))
    listadeclientes[indice] = novonome

    

def DeletarCliente ():
    nome = str(input('Informe o nome que gostaria de deletar: '))
    indice = listadeclientes.index(nome)
    listadeclientes.pop(indice)

  

opçao = 0
while opçao !=5:
    print(f'{"Menu":^28}')
    print('-'*30)
    print('1 - Salvar novo cliente \n2 - Alterar nome do cliente \n3 - Deletar cliente \n4 - Lista todos os clientes \n5 - sair')
    print('-'*30)
    opçao = int(input('Escolha sua opção: '))
    time.sleep(2)
    if opçao ==1:
        SalvarNomeCliente  ()
        print(listadeclientes)
    elif opçao ==2:
        AlterarNomeCliente ()
        print(listadeclientes)
    elif opçao ==3:
         DeletarCliente ()
         print(listadeclientes)
    elif opçao ==4:
        print(listadeclientes)
    time.sleep(2)

print('>>>>>>>>>>>> Fim do progarama!')         





       
     






