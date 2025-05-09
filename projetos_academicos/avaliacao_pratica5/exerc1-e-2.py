def conversao(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

inicial = int(input("Valor inicial (inteiro) em Fahrenheit: "))
final = int(input("Valor final (inteiro) em Fahrenheit: "))

print("Fahrenheit | Celsius")
if inicial < final:
    for fahrenheit in range(inicial, final+1):
        celsius = conversao(fahrenheit)
        print(f"{fahrenheit:>5d} °F | {celsius:>7.3f} °C")
elif inicial > final:
    for fahrenheit in range(inicial, final-1, -1):
        celsius = conversao(fahrenheit)
        print(f"{fahrenheit:>5d} °F | {celsius:>7.3f} °C")