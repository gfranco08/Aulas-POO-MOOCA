def taxaCalculator(tx, price):
    total = (1 + (tx / 100)) * price
    return total



value = taxaCalculator(20, 100)
print(value)

value = taxaCalculator(100, 20)
print(value)

value = taxaCalculator(price=100, tx=20)
print(value)



def taxaCalculatorDefault(price, tx=20):
    total = (1 + (tx / 100)) * price
    return f"O valor {price} adicionado de {tx}% é {total:.2f}"


response1 = taxaCalculatorDefault(100)
print(response1)

response2 = taxaCalculatorDefault(100, 15)
print(response2)



def taxaCalculatorImpure(price, tx=20):
    total = (1 + (tx / 100)) * price
    print(total)
    return f"O valor {price} adicionado de {tx}% é {total:.2f}"


response3 = taxaCalculatorImpure(100)
print(response3)



import random


def randomic(number):
    result = number + random.randint(0, 10)
    return result


print(randomic(10))


def definePar(number):
    if number % 2 == 0:
        return f"{number} é par"
    else:
        return f"{number} é ímpar"


print(definePar(10))
print(definePar(11))


def areaTriangulo(b, h):
    area = (b * h) / 2
    return area


base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))
print(f"A área do triangulo é: {areaTriangulo(base, altura)} u.a.")