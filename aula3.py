class Terreno:

    def calcular_area(self, largura, comprimento):
        return largura * comprimento

    def calcular_preco_total(self, largura, comprimento, preco_metro):
        area = self.calcular_area(largura, comprimento)
        return area * preco_metro

    def calcular_preco_financiado(self, largura, comprimento, preco_metro):
        total = self.calcular_preco_total(largura, comprimento, preco_metro)
        return total * 1.22


# Programa principal
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
preco_metro = float(input("Digite o preço do metro quadrado: "))

# Criando o objeto
terreno = Terreno()

print("Área do terreno:", terreno.calcular_area(largura, comprimento), "m²")
print("Preço total: R$", terreno.calcular_preco_total(largura, comprimento, preco_metro))
print("Preço financiado (22% juros): R$", terreno.calcular_preco_financiado(largura, comprimento, preco_metro))
