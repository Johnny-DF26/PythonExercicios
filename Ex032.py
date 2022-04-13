from datetime import date
print('')
print('=======--------------ANO BISSEXTO ?----------------------=======')
ano = int(input('Digite um ano ou digite "0" para o nao atual: '))

if ano == 0:
    #ano = 2022
    ano = date.today().year
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('O ano {},É BISSEXTO'.format(ano))
else:
    print('O ano {}, NÃO É BISSEXTO'.format(ano))

print('---------=================================================-------')
