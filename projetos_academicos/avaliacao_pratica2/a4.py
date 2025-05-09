def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero não é permitida."
    return x / y

def formatar(valor):
    if isinstance(valor, float) and valor.is_integer():
        return int(valor)
    return f"{valor:.2f}" if isinstance(valor, float) else valor

def linhas():
    print("-" * 44)

linhas()
print("Calculadora de quatro operações".center(40))
linhas()

print("+ → Adição\n- → Subtração\n* → Multiplicação\n/ → Divisão")

while True:
    operacao = input("Escolha uma operação (+, -, *, /): ").strip()
    linhas()

    if operacao in ('+', '-', '*', '/'):
        while True:
            try:
                num1 = float(input("Digite o primeiro número: "))
                break
            except ValueError:
                print("Erro: Verifique se digitou um número válido.")

        while True:
            try:
                num2 = float(input("Digite o segundo número: "))
                break
            except ValueError:
                print("Erro: Verifique se digitou um número válido.")

        linhas()
        if operacao == '+':
            resultado = formatar(adicao(num1, num2))
            print(f"{num1} + {num2} = {resultado}")
        elif operacao == '-':
            resultado = formatar(subtracao(num1, num2))
            print(f"{num1} - {num2} = {resultado}")
        elif operacao == '*':
            resultado = formatar(multiplicacao(num1, num2))
            print(f"{num1} * {num2} = {resultado}")
        elif operacao == '/':
            resultado = divisao(num1, num2)
            print(f"{num1} / {num2} = {formatar(resultado)}")
        linhas()

        while True:
            continuar = input("Quer fazer outro cálculo? (s/n): ").strip().lower()
            if continuar in ("sim", "s"):
                break
            elif continuar in ("não", "nao", "n"):
                print("\nFinalizando a calculadora.")
                exit()
            else:
                print("Erro: Responda com s/n ou sim/não'.")