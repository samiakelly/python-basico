#FAÇA UM ALGORITIMO QUE CALCULE O IMC DA PESSOA E MOSTRE O RESULTADO.
peso = input('informe seu peso:')
altura = input ('informe sua altura:')
imc =  float(peso)/(float(altura)* float(altura))
print ('o seu imc é', imc) 

if (imc < 18.5):
    print('O usuario está na magreza')
elif(imc > 18.5 and imc < 24.9):
    print('O usuario está normal')
elif(imc > 24.9 and imc < 30):
    print('O usuario está sobrepeso')
else:
     print('O usuario está na obesidade')
