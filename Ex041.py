from datetime import date
print('')
print('|---------------CONFEDERAÇÃO NACIONAL DE NATAÇÃO------------------|')
ano = int(input(' Digite seu ano de nascimento: '))


idade = date.today().year - ano
print('Sua idade é \033[34m{}\033[m, sua categoria é:'.format(idade))
if idade < 9:
    print('MIRIM')
elif idade < 14:
    print('INFANTIL')
elif idade < 19:
    print('JUNIOR')
elif idade < 20:
    print('SENIOR')
else:
    print('MASTER')
