def linhas():
    print("--------------------------------------------")

linhas()
print("Ordenador crescente de dois números inteiros")
linhas()

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
menor, maior = (valor1, valor2) if valor1 < valor2 else (valor2, valor1)
print(menor, maior, sep=" -> ")