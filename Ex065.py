print('')
print('------------------')

resp = 'S'
soma = cont = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um numero: '))
    resp = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Voce digitou {cont} números e a média entre eles é: {soma/cont:.2f}')
print(f'O maior numero é: {maior}. E o menor é: {menor}')
