from datetime import date

print('')
print('|---------------CONFEDERAÇÃO NACIONAL DE NATAÇÃO------------------|')
ano = int(input(' Digite seu ano de nascimento: '))
idade = date.today().year - ano
print(f'Sua idade é \033[34m{idade}\033[m, sua categoria é:')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')
