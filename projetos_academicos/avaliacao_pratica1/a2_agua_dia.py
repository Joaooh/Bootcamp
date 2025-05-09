def linhas():
    print("-" * 45)

linhas()
print("Cálculo de quanta água tomar por dia".center(45))
linhas()

while True:
    try:
        massa = float(input("Insira sua massa corporal: "))
        if massa > 0:
            break
        else:
            print("Insira um valor maior que zero.")
    except ValueError:
        print("Insira um número válido (exemplo: 62.5).")

dose_ideal = massa * 0.03
print(f"\nSua dose de água ideal por dia é de {dose_ideal:.2f}L.")