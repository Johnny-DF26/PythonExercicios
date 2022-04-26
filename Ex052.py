print('')
print('==============================================')

tot = 0
num = int(input('Digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\033[m')
if tot == 2:
    print('NÚMERO PRIMO')
else:
    print('NÚMERO NÃO É PRIMO')

print(f'O numero {num} foi divisíveis {tot} vezes')
