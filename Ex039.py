from datetime import date
print('')
print('=================ALISTAMENTO====================')
nasc = int(input('Em que ano voce nasceu? '))

anoAtual = date.today().year
tempoFalta = 18 - (anoAtual - nasc)
tempoPassou = (anoAtual - nasc) - 18

if anoAtual - nasc == 18:
    print('\033[33mEsta na hora de alistar ao serviço militar Obrigatório!!\033[m')
elif anoAtual - nasc < 18:
    print('Voce ainda vai servir o serviço Obrigatório,\033[34mFaltam {} Anos\033[m'.format(tempoFalta))
elif anoAtual - nasc > 18:
    print('\033[31mVoce ja passou do tempo de se APRESENTAR {} anos\033[m ou já serviu !!'.format(tempoPassou))



