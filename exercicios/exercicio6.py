#while (resposta == 'S'):
    #logica

#Informe o nome do cliente que será salvo:
#Guilherme
#Deseja salvar mais um cliente? (S/N)
#S volta pra pergunta
#N printa a lista .

opçao = 'S'
nomedosclientes = ['Fernando Noronha', 'Gilberto Cruz', 'Amanda Beatriz']
while  'S' == opçao:
       nome = input('Informe o nome do cliente: ')   
       nomedosclientes.append(nome)
       opçao =  input('Deseja adicionar mais um cliente? S/N: ')     
       
nomedosclientes.sort()      
print (f'{"Nome dos clientes":^80}')
print('-'*88)
print(nomedosclientes)   
print('-'*88)  





