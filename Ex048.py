
print('')
print('=======================SOMA ÍMPARES==========================')
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
    print(c,end=' ')
print('')
print(f'A soma dos numeros multiplos por 3 é: {cont}')
print(f'A soma dos valores é: {s}')
