# exercicio custo final = custo de fábrica +
#(custo de fábrica * percentual do distribuidor) +
#(custo de fábrica * percentual de impostos)
#Considerando os valores abaixo, faça um programa para calcular o custo de fabricação.
#Custo de fábrica = 10.000
#Percentual do distribuidor = 28%
#Percentual dos Impostos  = 45%
#o Resultado passando os parâmetros acima seria
#-------------->17300.



def CustoDeFabrica ():
    custo = float(input('custo de fabrica R$: '))
    distribuidor = custo * (28/100)
    impostos = custo *(45/100)
   
    resultado = custo + distribuidor + impostos
    print ('custo final é',resultado)

def calculaPercentual (percentual):
    return  percentual/100

def calculaValor (pValor, pPorcentagem):
    return pValor * calculaPercentual(pPorcentagem) 

def CustoDefabrica1 ():
    valor = float(input('custo de fabrica R$:'))
    dis = float(input('informe o valor da distribuidora:'))
    imp = float(input('informe o valor do imposto:'))

    resultado = valor + calculaValor(valor, dis) + calculaValor(valor, imp)
    print ('custo final é', resultado )


CustoDefabrica1 ()    



