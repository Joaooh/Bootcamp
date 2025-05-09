def linhas():
    print("-" * 44)

linhas()
print("Ordenador crescente de dois números inteiros")
linhas()

def obter_numero(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro. Digite um número inteiro válido.")

numero1 = obter_numero("Digite o primeiro número: ")
numero2 = obter_numero("Digite o segundo número: ")

menor, maior = sorted([numero1, numero2])
linhas()
print(menor, maior, sep=" -> ")