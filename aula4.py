class Teste1:
    def __init__(self, teste):
        self.teste = teste
        print(f"excutando init para o objeto no endereço:{hex(id(self))}")

    def demonstra(self):
        print(f"""
            excutando demonstração de objeto no endereço:{hex(id(self))})
            valor{self.teste}
            """)

a = Teste1(2)
b = Teste1(3)

print(f"endereço A: {hex(id(a))}")
print(f"endereço B: {hex(id(b))}")
print(f"são o mesmo objeto? {a is b}")

print("." * 30)
a.demonstra()
b.demonstra()



class Teste2:
    _instance = None 

    def __new__(cls, *args, **kwargs):  
        if cls._instance is None:
            print("[__new__]: Alocando nova memoria... ")
            cls._instance = super().__new__(cls)
        else:
            print("""
            [__new__]: Objeto já existe. Reciclando endereço de memoria...
            """)
        return cls._instance
    
    def __init__(self, teste):
        print(f"[__init__]: Inicializando objeto no endereço: {hex(id(self))}")

        self.teste = teste
        print(f"Executando init para o objeto no endereço: {hex(id(self))}")

    def demonstra(self):
        print(f"""
        Executando demonstração para o objeto no endereço: {hex(id(self))}
        valor {self.teste}
            """)

print("Tentativa 1: Criando objeto 'a' ")
a = Teste2(2)

print("Tentativa 1: Criando objeto 'b' ")
b = Teste2(3)

print("\n" + "="*40)

print(f"endereço A: {hex(id(a))}")
print(f"endereço B: {hex(id(b))}")
print(f"são o mesmo objeto? {a is b}")

print("." * 30)
a.demonstra()
b.demonstra()
