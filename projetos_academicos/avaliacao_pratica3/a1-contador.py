# 1. Desenvolva o programa que leia vários valores reais e no final mostre as seguintes informações:
# A quantidade de valores digitados;
# A soma dos valores digitados;
# A média aritmética dos valores digitados;
# E a quantidade de valores digitados maior que 20.

def linhas():
    print('-' * 40)

valor = contador = contador20 = soma = media = 0

linhas()
print("Contador de valores com soma e média".center(40))
print("Digite -1 para sair da repetição".center(40))
linhas()

while True:
    try:
        valor = float(input("Digite um valor: "))
        if valor == -1:
            print("Contador encerrado!")
            break
        elif valor > 20:
            contador20 += 1
        contador += 1
        soma += valor
        media = soma / contador
    except ValueError:
        print("Erro: Insira um valor válido.\n")

linhas()
print(f"Foram inseridos {contador} valores.\nQuantos são maiores que vinte: {contador20}\nSoma de todos os valores: {soma:.2f}\nMédia aritmética: {media:.2f}")
linhas()