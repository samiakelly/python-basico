#Crie  um  programa  que  permita  fazer  a  conversão  cambial  entre  Reais  e Dólares. 
#  Considere como taxa  de  câmbio  US$1,00 = R$2,40. Leia um  valor  em Reais pelo teclado e
#  mostre o correspondente em Dólares.  
#Crie  um  programa  que  permita  fazer  a  conversão  cambial  entre  Dólares  e Reais.  Considere  como  taxa  de  câmbio  US$1,00  =  R$2,40.  Leia  um  valor  em Dólares pelo teclado e mostre o correspondente em Reais.

def ReiasParaDolar (): 

    reais = float(input('informe os reais:')) 
    resultado = (reais/5.40)
    print ('seu valor em dolares sao', resultado)

def DolarEmReais ():

    dolar = float(input('informe o valor de dólares:'))
    resultado = (dolar*5.40)
    print ('seu valor em reias são', resultado)

def conveçao ():
    print ('digite 1 para converter de reais para dolar ou digite 2 para converter de dolar para reais')
    opçao = int(input('digite sua opçao:'))
    if opçao ==1:
        ReiasParaDolar()
    else:
        DolarEmReais()

conveçao ()   


    





