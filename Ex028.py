import random
import time
print('')
print('-----------------SORTEIO----------------------')
n = int(input('Digite um numero de 0 a 5:'))

numero = random.randint(0,5)

print('PROCESSANDO...')
time.sleep(2)
print('Numero sorteado foi:{}'.format(numero))

if numero == n:
    print('Acertou o numero sorteado, VOCE VENCEU!')
else:
    print('Voce errou o numero sorteado, VOCE PERDEU!')