def linhas():
    print("-" * 51)

linhas()
print("Maior número entre três valores (usando operadores)".center(51))
linhas()

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))

if valor1 > valor2 and valor1 > valor3:
    maior = valor1
elif valor2 > valor3:
    maior = valor2
else:
    maior = valor3
linhas()

print(f"O maior valor entre {valor1}, {valor2} e {valor3} é: {maior}.")