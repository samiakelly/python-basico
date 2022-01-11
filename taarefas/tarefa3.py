#fazer um programa que recebea tres inteiros e diga qual deles e o maior e qual e o menor.

valor1 = int(input('Digite o primeiro numero: '))
valor2 = int(input('Digite o segundo numero: '))
valor3 = int(input('Digite o terceiro numero: '))


#menor = min(valor1, valor2, valor3)
##maior = max(valor1, valor2, valor3)

if valor1 < valor2 and valor1 < valor3:
    menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3

if valor1 > valor2 and valor1 > valor3:
    maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3      

print ('O menor numero é: ', menor)    
print ('O maior numero é: ', maior)  

