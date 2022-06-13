from random import randint
from time import sleep
from operator import itemgetter

jogos = {'Jogador1': randint(1,6),
         'Jogador2': randint(1,6),
         'Jogador3': randint(1,6),
         'Jogador4': randint(1,6)}
ranking = list()
for k, v in jogos.items():
    print(f'{k} jogou o dado: {v}')
    sleep(1)
print('=-'*30)
print(' ===== RANKING ===== ')
ranking = sorted(jogos.items(), key=itemgetter(1),reverse=True)
for c,i in enumerate(ranking):
    print(f'{c+1}º {i[0]} com: {i[1]}')
print(jogos)
print(ranking)
