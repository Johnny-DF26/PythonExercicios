# from math import sin,cos,tan, radians
import math
print('')
print('-----------------COSSENO E SENO------------------')
n = float(input('Digite um numero de um angulo: '))

sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))

print('O seno é: {:.2f}\nO cosseno é: {:.2f}\nA tangente é: {:.2f}'.format(sen, cos,tan))