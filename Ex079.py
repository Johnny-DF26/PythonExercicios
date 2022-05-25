num = list()
maior = menor = 0
while True:
    n = int(input("Digite um numero: "))
    if n not in num:
        num.append(n)
        if n == 0:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    else:
        print("Esse numero já foi digitado !!!")
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar [S/N]? ")).strip().upper()

    if resp in 'N':
        break
num.sort()
print("Sua lista de numeros em ordem crescente é: ",end='')
for c in num:
    print(f"{c}",end=' - ')
print('FIM')
print()
print(f"O maior valor é: {maior} e o menor é: {menor}")

