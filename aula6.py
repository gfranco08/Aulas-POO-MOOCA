class veiculo:
    def __init__(self,marca):
        self.marca = marca   

    def mover(self):
        return "Esta se movendo"
    
class carro(veiculo):
    def moverse(self):
        return "O carro esta dirigindo na estrada"
    
class Bicicleta(veiculo):
    def mover(self):
        return "a bicicleta esta sendo pedalada"

C = carro("honda")
B = Bicicleta("caloi")

print(C.marca, ">", C.mover())
print(B.marca, ">", B.mover())

#-----------------------------------------------------------------
print(40*"-")

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class estudante(pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)


e = estudante("helena","22", "123456")
print(e.nome, ">", e.matricula, ">", e.idade)
help(e)

#--------------------------------------


class animal:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        return "som generico de animal"
    
    def descrever(self):
        return f"eu sou {self.nome}, tenho {self.idade} anos"

class cachorro(animal):
    def __init__(self, nome, idade, raça):
        super().__init__(nome, idade)     
        self,raça = raça

    def fazer_som(self):
        return "au au au!"
    
    class gato(animal):
        pass
            
rex = cachorro("rex", 4, "labrador")
print(rex.descrever())
print(rex.fazer_som())
print("raça:", rex.raça())
print()

print("rex é instancia de cachorro?", isinstance(rex,cachorro))
print




#-----------------------------------
# print(40*"-")

class A: pass
class B: pass
class C(A,B): pass

print(C.__mro__)
# ou
help(C)
