# 3. Construa o programa que calcule a média aritmética dos números pares e a média aritmética dos números ímpares. O usuário fornecerá os valores de entrada que pode ser um número qualquer par ou ímpar. A condição de saída será o número 0 (zero).

def linhas():
    print('-' * 42)

soma_pares = cont_pares = 0
soma_impares = cont_impares = 0

linhas()
print("Média de valores pares e ímpares inteiros".center(42))
print("Digite 0 para sair da repetição".center(42))
linhas()

while True:
    try:
        valor = int(input('Digite um valor: '))
        if valor == 0:
            break
        elif valor % 2 == 0:
            soma_pares += valor
            cont_pares += 1
        else:
            soma_impares += valor
            cont_impares += 1
    except ValueError:
        print("Erro: Valor inválido, tente novamente.")

media_pares = soma_pares / cont_pares if cont_pares > 0 else 0
media_impares = soma_impares / cont_impares if cont_impares > 0 else 0

linhas()
print(f"Média dos valores pares: {media_pares:.2f}")
print(f"Média dos valores ímpares: {media_impares:.2f}")
linhas()