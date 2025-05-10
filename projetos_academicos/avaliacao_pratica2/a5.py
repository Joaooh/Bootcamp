def linha():
    print("-" * 52)

def titulo(texto):
    linha()
    print(texto.center(52))
    linha()

def obter_lado(nome):
    while True:
        try:
            valor = float(input(f"Digite o lado {nome}: "))
            if valor <= 0:
                print("Erro. O lado deve ser maior que zero.")
            else:
                return valor
        except ValueError:
            print("Erro. Insira um número válido.")

def forma_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Triângulo equilátero (todos os lados iguais)"
    elif a == b or a == c or b == c:
        return "Triângulo isósceles (dois lados iguais)"
    else:
        return "Triângulo escaleno (todos os lados diferentes)"

def verificar_triangulo():
    while True:
        titulo("Verificador de Triângulos")

        a = obter_lado("A")
        b = obter_lado("B")
        c = obter_lado("C")

        linha()
        if forma_triangulo(a, b, c):
            print("Os valores formam um triângulo válido!")
            print(tipo_triangulo(a, b, c))
        else:
            print("Os valores **não** formam um triângulo válido.")
        linha()

        while True:
            opcao = input("\nDeseja verificar outro triângulo? (S/N): ").strip().lower()
            if opcao == "s":
                break
            elif opcao == "n":
                print("\nPrograma finalizado.")
                return
            else:
                print("Opção inválida. Digite S ou N.")

verificar_triangulo()
