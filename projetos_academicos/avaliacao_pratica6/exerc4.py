# 4. Elabore o problema (o enunciado) de um problema que usa função e resolva o problema proposto, ou seja, faça a implementação da função def e da função principal (main).

""" Problema: criar uma função que calcule o IMC e retorne o resultado com base na altura e peso informados pelo usuário. """

def calculo(peso, altura):
    imc = peso / altura ** 2
    return imc

peso = float(input("Digite seu peso (kg): ").replace(',', '.'))
altura = float(input("Digite sua altura (m): ").replace(',', '.'))
print(f"Seu IMC é: {calculo(peso, altura):.2f}")