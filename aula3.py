class terreno():
    def calcularAreaDoRetangulo(self, L, C):
        area = (L*C)
        return area
    def valorTotal(self, area, valor):
       
        return  valor * area
    def taxa_financiamento(self, valor):
        return valor + (valor*0.22)
   

largura = float(input("digite a largura do retangulo: "))
comprimento = float(input("digite o comprimento do retangulo: "))
terrno1 = terreno()
areaTerreno = terrno1.calcularAreaDoRetangulo(largura, comprimento)
print(f"area do retangulo é {areaTerreno} M2")

valor = float(input("valor do terreno: "))
print(f"valor total do terreno é {terrno1.valorTotal(areaTerreno, valor)}")
print(f"valor total do terreno com financiamento é {terrno1.taxa_financiamento(terrno1.valorTotal(areaTerreno, valor))}")  