numero = (int(input('Digite um numero: ')),
          int(input('Digite outro numero: ')),
          int(input('Digite mais um numero: ')),
          int(input('Digite o ultimo numero: ')))

print(f'Os numero foram: {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}ª posição')
else:
    print('O valor 3 nao foi digitado !')
print(f'Os valores pares são:',end=' ')
for n in numero:
    if n % 2 == 0:
        print(f'{n}',end=' ')
