def menu(txt):
    print('--' * 20)
    print(txt)
    print('--' * 20)


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de: {a}m²')


# programa principal
menu('        Controle de Terreno       ')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
