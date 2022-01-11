class Pessoa:
    def __init__(self, nome, situacao="dormindo"):
        self.nome = nome
        self.situacao = situacao

    def dormir(self):
        if(self.situacao != "dormindo"):
            self.situacao = "dormindo"
            print(f'A pessoa {self.nome} foi dormir')
        else:
            print(f'A pessoa: {self.nome} já está dormindo')
            
    def acordar(self):
        if(self.situacao != "acordado"):
            self.situacao = "acordado"
            print(f'A pessoa {self.nome} foi acordada')
        else:
            print(f'A pessoa: {self.nome} já está acordada')

        
    def falar(self):
        if self.situacao in ('dormindo','falando','comendo'):
            print(f'A pessoa {self.nome} não pode falar porque está {self.situacao}')
            return
        self.situacao = "falando"
        print(f"A pessoa {self.nome}  começou a falar")      
      
    def pararDeFalar(self):
        if self.situacao == 'falando':
            print(f'A pessoa {self.nome} parou de falar')
            self.situacao = 'acordado'
        else:
            print(f'A pessoa {self.nome} não pode parar de falar, pois não esta falando')    
    
        

    def andar():
        pass
        # A pessoa nao pode estar: dormindo, andando
        # A nome.pessoa
    def andar():
        # A pessoa nao pode estar: dormindo, andando
        # A nome.pessoa nao poder andar pq ela esta pessoa.situacao
        pass
    def pararDeAndar():
        #somente se estiver andando
        # A pessoa.nome não está andando
        pass

    def comer():
        # A pessoa nao pode estar: dormindo, andando, falando
        # A nome.pessoa nao poder comer pq ela esta pessoa.situacao
        pass
    def pararDeComer():
        #somente se estiver comendo
        # A pessoa.
        pass