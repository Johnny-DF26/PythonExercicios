#from math import hypot
import math
print('')
print('-------------------TRIANGULO DAS BERMUDAS------------------')
co = float(input('Digite o numero do comprimento cateto oposto: '))
ca = float(input('Digite o numero do cateto adjacente: '))

hip = math.hypot(co,ca)

print('-----------------------------------------------------------')
print('O valor da hipotenusa é:{:.3f}'.format(hip))
print('-----------------------------------------------------------')