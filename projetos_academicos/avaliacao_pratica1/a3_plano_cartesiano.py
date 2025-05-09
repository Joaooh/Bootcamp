from math import sqrt

def linhas():
    print("-----------------------------------------------")

linhas()
print("Distância entre dois pontos no plano cartesiano")
linhas()

x1 = float(input("Insira o valor de X₁: "))
y1 = float(input("Insira o valor de Y₁: "))
x2 = float(input("Insira o valor de X₂: "))
y2 = float(input("Insira o valor de Y₂: "))
distancia = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(f"A distância entre os pontos é: {distancia:.2f}.")