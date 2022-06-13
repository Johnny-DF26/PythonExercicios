from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= 1
    if p == 0:
        p = 1
    print(f'Contagem {i} até {f} de {p} em {p}: ')
    sleep(2)
    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
            sleep(.5)
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
            sleep(.5)
        print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez! ')
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)
