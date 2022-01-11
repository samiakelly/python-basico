#tarefa Faça um programa que conte quantos e quais caracteres não se repetem dentro de uma string
#Exemplo Hello World H = 1 e = 1 l = 3 o = 2 W = 1 r = 1 d = 1 
#O total de carcteres que não se repete são 5 e são eles : H, e, w, r , d
resultado = {}
unicos = 0
letrasUnicas = ''
caracteres = str(input('Escreva sua palavra ou sua frase: '))
for letra in caracteres:
    if letra !=' ':
      if letra not in resultado:
           resultado[letra] = 1
      else:
           resultado[letra] +=1  
    
for k,v in resultado.items():
    if v ==1:  
      unicos +=1
      letrasUnicas  += k + ',' 

print(f'O total de caracteres unicos são {unicos} são eles: { letrasUnicas[:-1]} !!')      
        
    
          
    




