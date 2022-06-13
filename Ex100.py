from random import randint


def sorteia(lista):
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ')
    print()


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de uma lista {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
