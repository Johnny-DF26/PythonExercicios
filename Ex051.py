print('')
print('==============================================')

a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Qual a razao de sua PA: '))
decimo = a1 + (10 - 1) * r
for c in range(a1, decimo + r, r):
    print(c, end='-')
print('FIM')
