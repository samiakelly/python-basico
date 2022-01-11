receita = ('ovo', 1.50 , 'farinha', 3.50 , 'leite', 5.00, 'fermento', 3.00 ,'chocolate', 4.00)
print ('-' * 40)
print (f'{"Receita":^40}')
print ('-' * 40 )
for pos in range(len(receita)):
     if pos % 2 ==0:
        print(f'{receita[pos]:.<30}',end='')
     else:
         print(f'R${receita[pos]:>7.2f}')   
print ('-' * 40 )         