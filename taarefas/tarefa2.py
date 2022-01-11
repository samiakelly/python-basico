# Criar um algoritmo em Python que informe a quantidade total de calorias de uma
#refeição a partir do usuário que deverá informar o prato, a sobremesa e a bebida 
#(vejaa tabela a seguir)

print('prato')
print('1 se for vegetariano')
print('2 se for peixe')
print('3 se for frango')
print('4 se or carne')

print('sobremesa')                                       
print('5 se for abacaxi')
print('6 se for sorvete diet')
print('7 se for mouse diet')
print('8 se for mouse de chocolate')

print('bebidas')
print('9 se for chá')
print('10 se for suco de laranja')
print('11 se for suco de melão')
print('12 se for refrigerante diet')


prato = input('informe seu prato:')
sobremesa = input('informe sua sobremesa:')
bebidas = input('informe a bebida:')
calorias = float(0)
if (prato == '1'):
   calorias += 180
   print ('vegetariano')
elif (prato == '2'):
    calorias += 230
    print ('peixe')
elif (prato == '3'):
    calorias += 250
    print ('frango')
elif (prato == '4'):
    calorias += 350
    print ('carne')  

if (sobremesa == '5'):
   calorias += 75
   print ('abacaxi')
elif (sobremesa == '6'):
    calorias += 110
    print ('sorvete diet')
elif (sobremesa == '7'):
    calorias += 170
    print ('mouse diet')
elif (sobremesa == '8'):
    calorias += 200
    print ('mouse de chocolate')     

if (bebidas == '9'):
   calorias += 20
   print ('abacaxi')
elif (bebidas == '10'):
    calorias += 70
    print ('sorvete diet')
elif (bebidas == '11'):
    calorias += 100
    print ('mouse diet')
elif (bebidas == '12'):
    calorias += 65
    print ('mouse de chocolate')        


print ('seu total de calorias é ', calorias)
