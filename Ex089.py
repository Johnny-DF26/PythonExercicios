"""pessoas = list()
notas = list()
pessoas.append(notas)
while True:
    print("--" * 20)
    nome = str(input("Digite seu nome: "))
    pessoas.append(nome)
    for c in range(1, 3):
        nota = float(input(f"Digite sua nota {c}: "))
        notas.append(nota)
        pessoas.append(notas[:])
        notas.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar [S/N]: ")).upper().strip()[0]
    if resp == 'N':
        break

# print(pessoas[1])
# for i in notas:
#     print(i[0])

print(pessoas)
print(notas)"""

ficha = list()

while True:
    print("==" * 20)
    nome = str(input("Digite seu nome: "))
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]
    if resp == 'N':
        break
print("==" * 30)
print(f'{"N°":<4}{"Nome":<15}{"Média":>8}')
print("--" * 20)
for i, a in enumerate(ficha):
    print(f"{i + 1:<4}{a[0]:<18}{a[2]:.2f}")
while True:
    print("==" * 30)
    opc = int(input("Mostrar a nota e qual aluno(999 para finalizar!): "))
    print('')
    if opc == 999:
        print("Finalizando ...")
        break
    if (opc - 1) <= len(ficha) - 1:
        print(f'{"Nome":<15}{"Nota 1":>8}{"Nota 2":>8}')
        print("--" * 20)
        print(f'{ficha[opc -1][0]:<17}{ficha[opc -1][1][0]:<8.2f}{ficha[opc -1][1][1]:.2f}')
    print('')
print("Volte Sempre !!")
