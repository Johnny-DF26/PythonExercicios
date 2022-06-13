aluno = dict()
aluno['nome'] = str(input("Digite o nome do aluno: "))
aluno['media'] = float(input("Digite a média do aluno: "))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 6.9:
    aluno['situacao'] = 'Recupercao'
elif aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
print("=-"*20)
for k,v in aluno.items():
    print(f" - {k} é igual a: {v}")

