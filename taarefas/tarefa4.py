#FAÇA UM ALGORITMO QUE ESCREVA NA TELA QUANTOS NUMEROS PARES E IMPARES POSSUEM ATE O RESPECTIVO VALOR.
numero =int(input('Digite o valor: '))
conta = 1
par = 0
impar = 0

while conta <=numero: 
      conta +=1  
      resto = conta % 2
      if resto == 0:
         par += 1
      elif resto != 0:
         impar += 1

print ('O total de numero par são: ', par) 
print ('O total de numero impar são: ', impar)            




