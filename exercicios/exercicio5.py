#FAÇA UM ALGORITIMO QUE MOSTRE O MAIOR E O MENOR NUMERO.
import sys; 



numeros = (3, 200, 4, 6, 16, 33, 201, 1, 2)
maiornumero = 0
menornumero = sys.maxsize
for valor in numeros:
    if valor > maiornumero:
        maiornumero = valor
    if valor < menornumero:
        menornumero = valor
print('O maior numero é: ', int(maiornumero))    
print('O menor numero é: ', int(menornumero))       
    

