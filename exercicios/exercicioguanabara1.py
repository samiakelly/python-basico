# crie um programa que onde o usuario possa digitar sete valores numericos e cadastrios em uma lista unica
# que matenha separado os valores pares e impares, no final mostrar os valores pares e impares em ordem
# crescente.
par = list()
impar = list()
numero = 1
while numero <=7:
      valor = int(input('Informe um numero: '))
      numero +=1 
      resto = valor % 2
      if resto ==0:
          par.append(valor)
      elif resto !=0:
          impar.append(valor)


par.sort()
impar.sort()        
print('-='*26)
print('Os valores pares digitados foram', par)    
print('Os valores impares digitados foram', impar)           

