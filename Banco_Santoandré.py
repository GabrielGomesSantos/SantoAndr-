class Cliente:

    def __init__(self,nome,conta,saldo,):
        self.nome = nome 
        self.conta = conta 
        self.saldo = saldo 

    def getdados(self): 

        print("\n------------ Dados Bancarios ------------\n")
        print(f"Nome: {self.nome}\nN° da conta: {self.conta}")
        
    def transferencia(self):
        
        raise NotImplementedError ("Sei la transferencia")

class Cliente_Bronze(Cliente):

    def __init__(self, nome, conta, saldo):
        super().__init__(nome, conta, saldo) 
        self.tipo = "Cliente bronze"

    def transferir(self,valor):
    
        self.valor_descontado = valor+(valor*0.10)+15

    def getdados(self):
        super().getdados()
        print(f"Tipo: {self.tipo}\n\nSaldo: {self.saldo}")
        print("----------------------------------------\n")

class Cliente_Prata(Cliente):
    
    def __init__(self, nome, conta, saldo):
        super().__init__(nome, conta, saldo) 
        self.tipo = "Cliente Prata"

    def transferir(self,valor):
        
        self.valor_descontado = valor+(valor*0.05)+15

    def getdados(self):
        super().getdados()
        print(f"Tipo: {self.tipo}\n\nSaldo: {self.saldo}")
        print("----------------------------------------\n")

class Cliente_Ouro(Cliente):
    

    def __init__(self, nome, conta, saldo):
        super().__init__(nome, conta, saldo) 
        self.tipo = "Cliente Prata"

    def transferir(self,valor):
        
        self.valor_descontado = valor+(valor*0.02)+15

    def getdados(self):
        super().getdados()
        print(f"Tipo: {self.tipo}\n\nSaldo: {self.saldo}")
        print("----------------------------------------")

#c1 = Cliente("yan", 1001,100)
c2 = Cliente_Bronze("Peter", 1002,500)
c3 = Cliente_Prata("Fernanda",1003,500)
c4 = Cliente_Ouro("Gabriel",1004,500)

def realizar_transferencia(origem,destino,valor):
    origem.transferir(valor)
    if origem.saldo-origem.valor_descontado>0:
        origem.saldo-=origem.valor_descontado
        destino.saldo+=valor
        print(f"\nTranferência de R$ {valor} efetuada!\n")
    else:
        print("Por favor, verifique o valor de transferência!")


print("--------------------- Exemplos ---------------------")


realizar_transferencia(c4,c2,100)

print("\nConta Bronze")
c2.getdados()

print("Conta Prata")
c3.getdados()

print("Conta Ouro")
c4.getdados()
