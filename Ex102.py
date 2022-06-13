from math import factorial


def fatorial(num,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um númeo num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print(f' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f


# n = int(input('Digite um número: '))
print(fatorial(5, show=True))
