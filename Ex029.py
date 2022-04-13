import random
import time
print('')
print('=====================--DETRAN--===========================')
vel = float(input('Digite sua velocidade:'))
#vel = random.randint(50,150)

print('Velocidade:{:.1f}Km/h'.format(vel))
print('PROCESSANDO...')
time.sleep(2)
if vel > 80:
    print('VOCE PASSOU DA VELOCIDADE !!')
    print('VOCE SERÁ MULTADO EM R$:{:.2f}'.format((vel - 80) * 7))
print('VELOCIDADE PERMITIDA, DIRIJA COM CUIDADO')

