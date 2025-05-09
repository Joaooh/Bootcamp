# 2. Implemente o programa que leia a nota de vários alunos de uma turma e gere uma tela de saída com as seguintes informações: a quantidade de alunos aprovados, a quantidade de alunos reprovados e a quantidade de alunos que fizeram a prova. Considere que o aluno será aprovado com nota for maior ou igual a cinco.

def linhas():
    print('-' * 34)

nota = contador = soma = 0
aprovados = reprovados = 0  # Inicializando contadores

linhas()
print("Análise de notas de X alunos".center(34))
print("Digite -1 para sair da repetição".center(34))
linhas()

while True:
    try:
        nota = float(input("Digite uma nota: ").replace(",", "."))
        if nota == -1:
            break
        elif 0 <= nota <= 10:
            contador += 1
            soma += nota
            if nota >= 5:
                aprovados += 1
            else:
                reprovados += 1
        else:
            print("Erro: Nota fora do intervalo (0 a 10).\n")
    except ValueError:
        print("Erro: Nota inválida, tente novamente.\n")

media = soma / contador if contador > 0 else 0

linhas()
print("RESULTADO FINAL".center(34))
linhas()
print(f"{'Total de alunos:':<23}{contador:>10}")
print(f"{'Aprovados:':<23}{aprovados:>10}")
print(f"{'Reprovados:':<23}{reprovados:>10}")
print(f"{'Média da turma:':<23}{media:>10.2f}")
linhas()
