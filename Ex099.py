
def maior(*num):

    print('=-'*20)
    print('Analisando os valores passados ...')
    cont = maior = 0
    for valor in num:
        print(f'{valor}',end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print('=-'*20)
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi o {maior}')


'''maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(3, 0, 8)'''

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))
maior(num1,num2,num3)
