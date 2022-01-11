from conta import Conta
from contacorrente import ContaCorrente
from contapoupança import ContaPoupança

conta1 = Conta("nubank", 2345, 9876543, "samia kelly", 1500 )
ContaPoupança1 = ContaPoupança("nubank", 3976, 9875543, "Fernadno Noronha", 400)
ContaPoupança2 = ContaPoupança("itau", 3686, 9876643, "Samia Kelly", 100)
ContaCorrente1 = ContaCorrente("nubank", 3456, 9976543, "Pedro Henrrique", 200, 400)
ContaCorrente2 = ContaCorrente("bradesco", 3956, 9875521, "Alexia Fernanda", 200, 70)

contas = [ContaCorrente1, ContaCorrente2, ContaPoupança1, ContaPoupança2]

for conta in contas:


 conta.imprimir()




 


   





        
   

     

             

       
   












