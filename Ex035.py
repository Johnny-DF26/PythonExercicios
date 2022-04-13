r1 = float(input('Digite um numero: '))
r2 = float(input('Digite outro numero: '))
r3 = float(input('Digite terceiro numero: '))

if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    print('Da para formar um triangulo')
else:
    print('Nao da para formar um triangulo')
