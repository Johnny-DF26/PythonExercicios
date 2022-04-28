'''import math
print('-----------------------------------------------')
sair = ''
s = ''
while s != 'SAIR':
    num = int(input('Digite um numero: '))
    res = math.factorial(num)
    print(f'O fatorial de {num}! é: {res}')
    s = str(input('Deseja sair ? ')).upper()
    print('================================================')

from math import factorial
num = ''
while num != 0:
    num = int(input('Digite um numero: '))
    fat = factorial(num)
    print(f'O fatorial de {num}! é: {fat}')

n = int(input('Digite um numero: '))
c = n
f = 1
print(f'Calculando {n}! =', end=' ')
while c > 0:
    print(c, end='')
    if c > 1:
        print('x', end='')
    else:
        print('=', end='')
    f *= c
   # print('x' if c > 1 else '=', end='')
    c -= 1
print(f)
'''

n = int(input('Digite um numero: '))
f = 1
c = n
for c in range(n,0, -1):
    f = f * c
    print(c, end=' ')
    if c > 1:
        print('x',end=' ')
    else:
        print('=', end=' ')
print(f)

