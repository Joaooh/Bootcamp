# 1. Desenvolva uma função que recebe uma mensagem e um número, ela mostra a mensagem e o número e não retorna nada.
# A função funcao chama a função passando os dois argumentos lidos, ou seja, digitados pelo usuário.

def funcao(mensagem, numero):
    print(mensagem)
    print(numero)

mensagem = str(input("Digite uma mensagem: "))
numero = float(input("Digite um número: "))
funcao(mensagem, numero)