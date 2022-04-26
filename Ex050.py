print('')
print('==================SOMA NUMEROS INTEIROS====================')

s = 0
cont = 0
for c in range(1, 7, 1):
    num = int(input(f'Digite o {c}° numero: '))
    if num % 2 == 0:
        s += num
        cont += 1
if cont == 1:
    print(f'Apenas "{cont}" numero par')
else:
    print(f'Ao todo sao "{cont}" numeros pares')
print(f'A soma dos numeros é: "{s}"')
print('FIM')
