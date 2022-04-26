'''import random
print('')
print('---------------------------------------------------')
mao = str(input('Me diga: PEDRA, PAPEL OU TESOURA: ')).strip().upper()

list = ['PEDRA', 'PAPEL', 'TESOURA']
comp = list[random.randrange(len(list))]
print(f'Computador:{comp}')

if (comp == 'PAPEL' and mao == 'PEDRA') or (comp == 'TESOURA' and mao == 'PAPEL') or (comp == 'PEDRA' and mao == 'TESOURA'):
    print('Voce PERDEU')
elif (mao == 'PAPEL' and comp == 'PEDRA') or (mao == 'TESOURA' and comp == 'PAPEL') or (mao == 'PEDRA' and comp == 'TESOURA'):
    print('Voce GANHOU !!')
else:
    print('EMPATE')'''
from time import sleep
from random import randint
itens = ('Pedra','Papel','Tesoura')
comp = randint(0,2)
mao = int(input('Suas opces:\n'
            '[0] PEDRA\n'
            '[1] PAPEL\n'
            '[2] TESOURA\n'
            'Qual é a sua jogada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
print('=-'*20)
print(f'O Computador jogou: {itens[comp]}')
print(f'O jogador jogou: {itens[mao]}')
if (comp == 0 and mao == 2) or (comp == 1 and mao == 0) or (comp == 2 and mao == 1):
    print('VOCE PERDEU !!')
elif (mao == 0 and comp == 2) or (mao == 1 and comp == 0) or (mao == 2 and comp == 1):
    print('VOCE GANHOU !!')
else:
    print('EMPATE !!')
