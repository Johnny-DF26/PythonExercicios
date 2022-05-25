"""
from random import randint

print('')
print('=========================JOGO PAR OU ÍMPAR============================')

res = ParOuImpar = ''

while True:
    comp = randint(0,10)
    jogador = int(input('Digite um valor: '))
    while ParOuImpar not in 'PI':
        ParOuImpar = str(input('Par ou Ímpar[P/I]: ')).upper().strip()[0]
    print('---------------------------------------------------------')
    soma = comp + jogador
    if soma % 2 == 0:
        res = 'PAR'
    elif soma % 2 == 1:
        res = 'IMPAR'
    print(f'Voce jogou {jogador} e o computador {comp}. Total deu {soma}, deu {res}')
    if res == ParOuImpar:
        print('Voce Venceu !\n'
              'Vamos jogar novamente ...')
        print('---------------------------------------------------------')
    else:
        print('Voce Perdeu !\n'
              'GAMER OVER !')
        break
"""
from random import randint
v = 0
while True:
    computador = randint(0,10)
    jogador = int(input('Digite um numero: '))
    soma = jogador + computador
    tipo = ''
    while 'I' != tipo != 'P':
        tipo = str(input('Par ou Impar[P/I]: ')).upper().strip()[0]
    print(f'Voce jogou {jogador} e computador {computador}, a soma: {soma}. ',end='')
    print('Deu PAR' if soma % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Voce Ganhou')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Voce Venceu')
            v += 1
        else:
            print('Voce Perdeu')
            break
    print('Vamos jogar novamente ...')
print(f'GAME OVER! Voce venceu {v} vezes')
