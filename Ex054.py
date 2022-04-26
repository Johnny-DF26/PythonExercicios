from datetime import date
anoAtual = date.today().year
print('')
print('=====------------------MAIORIDADE---------------------=====')
maior = 0
menor = 0
for c in range(1, 8):
    aniv = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if anoAtual - aniv >= 21:
        maior += 1
    else:
        menor += 1
print(f'\033[31m{maior}\033[m pessoas atingiram a maioridade')
print(f'\033[31m{menor}\033[m pessoas nao atingiram a maioridade')

