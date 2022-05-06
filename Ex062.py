'''
print('')
print('------------PROGRESSAO ARITMETICA 3.0---------------')
a1 = int(input('Digite o primeiro termo da PA: '))
# a1 vai receber um numero inteiro
razao = int(input('Digite a razao da PA: '))
# razao vai receber um numero inteiro
termo = a1
# termo vai receber a1
cont = 1
# cont recebe 1
total = 0
# total recebe 0
mais = 10
# mais recebe 10
while mais != 0:
    # enquanto mais for diferente de 0. Mais comecando com 10 >>> 10 != 0.
    total = total + mais
    # total comecando com 0, recebe total que ainda é 0, mais que comeca com 10 >>> 0 = 0 + 10.
    while cont <= total:
        # contagem que comeca com 1, enquanto 1 <= 10, entra na na aninhamento
        print(f'{termo} - ',end='')
        # escrever na tela o termo que comeca com a1, continua na mesma linha
        termo += razao
        # termo recebe a1 somado com razao
        cont += 1
        # faz uma contagem somando mais 1
    print('PAUSE')
    # escreve pause na tela
    mais = int(input('Quantos a mais voce deseja: '))
    # mais recebe o numero digitado
print(f'O total de progressoes foi de {total}')
# escreve na tela a frase e total de numeros somados com mais
'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite o numero da razao: '))
cont = 1
termo = a1
mais = 5
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}',end=' - ')
        termo += r
        cont += 1
    print('Pause')
    mais = int(input('Quantos termos voce quer mostrar a mais?'))

