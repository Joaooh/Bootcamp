soma = 0
for i in range(0, 11):
    dobro = i * 2
    print(dobro)
    soma += dobro
media = soma / 11
print(f"Soma total: {soma}\nMédia aritmética: {media}")
# Eu inclui o 0 pois naturais vão de 0 a 10, e isso afeta a média final em 1