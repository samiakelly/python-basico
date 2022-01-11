class Cama:
   def __init__(self, cor , tipo, situaçao= "arrumada"):
       self._cor = cor
       self._tipo = tipo
       self._situaçao = situaçao

   def arrumar(self):
       if self._situaçao == 'arrumada':
           print('A cama ja está arrumada.')
       else:
          print('A cama foi arrumada.')
          self._situaçao = 'arrumada'
    
   def dessarrumar(self):
        if self._situaçao == 'arrumada':
           print('A cama foi dessarrumada.')
           self._situaçao = 'dessarrumada'
        else:
           print('A cama ja está desarrumada.') 
          