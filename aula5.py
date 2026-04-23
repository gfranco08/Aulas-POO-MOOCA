class Conta:
    def __init__(self):
        self.saldo = 1000

        def saldo(self):
            return self.saldo
        

conta = Conta()

print(conta.saldo)

conta.saldo = 2000

print(conta.saldo)


class conta:
    def __init__(self):
        self._saldo = 1000
    
    def saldo(self):
        return self._saldo
    

conta = Conta()

print(conta._saldo)

conta.__saldo  = 2000            

print(conta._saldo)


from dataclasses import dataclass
@dataclass(frozen=True)
class Conta:
    saldo: float = 1000
    nome : str = "Gabriel"
conta = Conta()
print (conta.saldo, conta.nome)
