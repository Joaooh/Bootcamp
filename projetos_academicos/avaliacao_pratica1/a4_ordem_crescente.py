def linhas():
    print("-" * 44)

linhas()
print("Ordenador crescente de dois números inteiros".center(44))
linhas()

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

menor, maior = sorted([valor1, valor2])
linhas()
print(menor, maior, sep=" -> ")