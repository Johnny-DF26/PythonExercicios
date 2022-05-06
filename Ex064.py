'''num = 0
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero: '))
    num += 1
    soma += n

print(f'Foram digitados {num} numeros')
print(f'A soma entre ele é de: {soma}')
'''

num = cont = soma = 0
num = int(input('Digite um numero: '))
while num != 999:
    if num != 999:
        cont += 1
        soma += num
        num = int(input('Digite um numero: '))
    else:
        print('')
print(f'Foram digitados {cont - 1} numeros')
print(f'A soma entre ele é de: {soma}')
