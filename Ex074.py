from random import randint

cont = menor = 0
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os numeros sorteados foram:',end=' ')
for n in numeros:
    print(f'{n}',end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O maior valor sorteado foi {min(numeros)}')
