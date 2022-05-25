pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input("Digite seu nome: ")))
    dados.append(float(input("Digite seu peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input("Deseja continuar:[S/N]: ")).upper().strip()
    if resp == 'N':
        break
print(f"Quantidade de pessoas cadastradas: {len(pessoas)}")
for p in pessoas:
    if p[1] == menor:
        print(f"A pessoa mais leve tem {menor} Kgs e é {p[0]}")
    elif p[1] == maior:
        print(f"A pessoa mais pesada tem {maior} Kgs e é {p[0]}")
