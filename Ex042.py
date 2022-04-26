from time import sleep
print('---------------TRIANGULO DAS BERMUDAS 2------------------')
r1 = float(input('Digite um numero: '))
r2 = float(input('Digite outro numero: '))
r3 = float(input('Digite terceiro numero: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Aguarde ...')
    sleep(1)
    print('\033[35mÉ um triangulo', end=' ')
    if r1 == r2 == r3:
        print('\033[36mEquilátero\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[36mEscaleno\033[m')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:# pode ser um simplismente um else
        print('\033[36mIsósceles\033[m')

else:
    print('Aguarde ...')
    sleep(1)
    print('\033[31mNao é um triangulo !!!\033[m')




