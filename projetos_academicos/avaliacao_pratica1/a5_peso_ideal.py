def linhas():
    print("-" * 40)

linhas()
print("Cálculo do peso ideal com base na altura".center(40))
linhas()

sexo = input("Digite seu sexo (M/F): ").strip().upper()
while sexo[:1] != "M" and sexo[:1] != "F":
    print("Opção inválida. Digite M para masculino ou F para feminino.")
    sexo = input("Digite seu sexo (M/F): ").strip().upper()

while True:
    try:
        altura = float(input("Digite sua altura: "))
        if altura > 0:
            break
        else:
            print("Por favor, digite um número maior que zero.")
    except ValueError:
        print("Tente novamente com um número válido (exemplo: 1.75).")

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

linhas()
print(f"Seu peso ideal é: {peso_ideal:.1f}kg.")