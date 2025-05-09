# 2. Implemente uma função que calcula a idade de uma pessoa. Ela recebe o ano de nascimento da pessoa, faz o cálculo e retorna à idade.
# A função principal (main) lê o ano de nascimento digitado pelo usuário, chama a função e mostra o valor retornado pela função calcula.
from datetime import datetime

def calculo(ano_nasc):
    idade = ano_atual - ano_nasc
    return idade

ano_atual = datetime.now().year
ano_nasc = int(input("Ano de nascimento: "))
print(f"Sua idade é: {calculo(ano_nasc)}")