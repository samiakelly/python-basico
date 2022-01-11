# ovo..........R$1.50

#            0     1        2         3       4      5       6          7       8          9
receita = ('ovo', 1.50 , 'farinha', 3.50 , 'leite', 5.00, 'fermento', 3.00 ,'chocolate', 4.00)
for variavel in range(0,len(receita),2):
   print(f'{receita[variavel]} ...............R$ {receita[variavel + 1]:>2.2f}')
   
   

