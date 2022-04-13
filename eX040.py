print('')
print('----------------------NOTAS--------------------------')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('\033[31mVoce está REPROVADO')
elif 5.0 <= media <= 6.9:
    print('\033[33mVoce está de RECUPERAÇÃO')
elif media > 7.0:
    print('\033[36mVoce está APROVADO')


