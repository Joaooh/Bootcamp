from math import pi

def linhas():
    print("-----------------------------------")

linhas()
print("Calculadora de volume de uma esfera")
linhas()

raio = float(input("Insira o raio da esfera: "))
volume = (4/3) * pi * (raio ** 3)
print(f"O volume de uma esfera de raio {raio} é {volume:.2f}m³.")