pessoas = dict()
total = list()
somaPessoas = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Nome: "))
    while True:
        pessoas['sexo'] = str(input("Sexo: ")).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite M ou F.")
    pessoas['idade'] = int(input("Idade: "))
    somaPessoas += pessoas['idade']
    total.append(pessoas.copy())
    resp = ' '
    while True:
        resp = str(input("Deseja continuar: ")).strip().upper()
        if resp in 'SN':
            break
        print("ERRO! Por favor, digite S ou N.")
    if resp == 'N':
        break
print("=-"*30)
print(f"A) Ao todo temos {len(total)} pessoas cadastradas.")
print(f"B) A media de idade é: {somaPessoas / len(total):.2f} anos")
print(f"C) As mulheres cadastradas foram: ")
for p in total:
    if p['sexo'] in 'F':
        print(f"- {p['nome']} ")
print(f"D) Pessoas com idade acima da média são: ")
for p in total:
    if p['idade'] > somaPessoas / len(total):
        for k, v in p.items():
            print(f"{k}; = {v}; ",end='')
        print()
print(">>>>ENCERRADO<<<<")
