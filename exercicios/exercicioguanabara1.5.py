num = [[], []]
valor = 0
for c in range(1 , 8):
    valor = int(input(f'DIgite o {c}º. valor: '))
    if valor % 2 ==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()        
print('-='*30)
print(f'Os valores digitados pares foram: {num[0]}') 
print(f'Os valores digitados impares foram: {num[1]}')           

