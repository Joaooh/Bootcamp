# 3. Crie uma função para somar três valores. Ela recebe os três valores, calcula a soma e retorna o resultado do cálculo. 
# A função main lê os três valores inteiros, chama a função passando os valores lidos e depois mostra o valor retornado pela função, ou seja, o resultado obtido.

def calculo(num1, num2, num3):
    soma = num1 + num2 + num3
    return soma

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))
print(f"{num1} + {num2} + {num3} = {calculo(num1, num2, num3)}")