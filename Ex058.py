'''
import random

comp = ''
player = '0'
cont = 0
while player != comp:
    comp = random.randint(0, 10)
    player = int(input('Type it a number: '))
    print(f'Computador jogou foi: {comp}')
    print(f'O jogadaor foi: {player}')
    if player != comp:
        cont += 1
        print('\033[31mVoce errou \033[m')
        print('==========================================')
if player == comp:
    print('\033[34mVoce acertou !\033[m')
print(f'Voce tentou {cont} vezes')

print('========================JO KEN PO==========================')
lista = ['JO', 'KEN', 'PO']
jogador = ''
soma = 0
comp = random.choice(lista)
while jogador != comp:
    comp = random.choice(lista)
    jogador = str(input('jogue o JO,KEN,PO: ')).upper().strip()
    print(f'Voce jogou: {jogador}')
    print(f'O computador jogou: {comp}')
    if comp == jogador:
        print('Voce acertou')
    elif comp != jogador:
        soma += 1
        print('Voce errou !')
        print('Tente Novamente')
        print('===================================')
print(f'O total de tentativas foi: {soma}')
'''
from random import randint
comp = randint(0,10)
jogador = 0
tent = 0
print('')
print('Sou seu computador... Acabei de pensar em um  número entre 0 e 10.')
print('Será que voce consegue advinhar qual foi?')
while comp != jogador:
    ''''while not acertou - var: acertou = false'''''
    jogador = int(input('Qual é o seu palpite? '))
    tent += 1
    if comp > jogador:
        print('Mais... Tente mais uma vez.')
    elif comp < jogador:
        print('Menos... Tente mais uma vez.')
    else:
        print(f'Computador jogou {comp}')
        print(f'Voce acertou com {tent} tentativas. Parabéns!')

