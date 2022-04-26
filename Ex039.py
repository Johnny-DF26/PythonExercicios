from datetime import date
anoAtual = date.today().year
print('')
print('=================ALISTAMENTO====================')
sexo = str(input('Qual é o seu sexo? [F/M]: ')).strip().upper()

if sexo == 'M':
    nasc = int(input('Em que ano voce nasceu? '))
    idade = anoAtual - nasc
    print(f'Sua idade é: {anoAtual - nasc} anos')
    if idade == 18:
        print('\033[33mEsta na hora de alistar ao serviço militar Obrigatório!!\033[m')
    elif idade < 18:
        tempoFalta = 18 - (anoAtual - nasc)
        saldo = anoAtual + tempoFalta
        print(f'Voce ainda vai servir o serviço Obrigatório,\033[34m faltam {tempoFalta} Anos\033[m')
        print(f'Seu alistamento vai ser em {saldo}')
    elif idade > 18:
        tempoPassou = (anoAtual - nasc) - 18
        saldo = anoAtual - tempoPassou
        print(f'\033[31mVoce ja passou do tempo de se APRESENTAR,\033[m em {tempoPassou} anos ou já serviu !!')
        print(f'Seu alistamento foi em {saldo}')
else:
    print('Voce nao precisa se alistar o serviço militar')




