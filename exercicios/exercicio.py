#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
#dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. 
def converteAnoEmDias (ano):
    return ( int(ano)*365)
def converteMesEmDias(mes):
    return (int(mes)*30)
     

def calcularDias (pAno,pMes,pDia):
    return converteAnoEmDias(pAno) + converteMesEmDias(pMes) + int(pDia)

ano = input('informe sua idade:')
mes = input('informe quantos meses:')
dia = input('informe quantos dias:')
resultado = calcularDias (ano,mes,dia)
print ('seus dias de vida são', resultado)


