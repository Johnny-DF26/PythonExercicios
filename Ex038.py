print('')
print('==' * 20)
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))

if n1 > n2:
    print('O primeiro valor é \033[36mMaior\033[m')
elif n2 > n1:
    print('O segundo valor é \033[36mMaior\033[m')
else:
    print('Não existe valor maior, os dois são \033[36mIguais\033[m')
