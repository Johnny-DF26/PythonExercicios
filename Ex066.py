
print('')
print('======================CONTADOR DE NUMEROS WHILE BREAK===========================')
cont = soma = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} e a soma entre eles é {soma}')
