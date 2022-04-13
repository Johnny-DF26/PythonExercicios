print('')
print('----------------------SALARIO--------------------------')
sal = float(input('Digite seu Salário: '))

'''if sal > 1250.00:
    print('Seu salario teve um aumento de R$: {:.2f}'.format(sal * 1.10))
else:
    print('Seu salário teve um aumneto de R$: {:.2f}'.format(sal * 1.15))'''

if sal < 1250:
    novo = sal + (sal * 15 /100)
else:
    novo = sal + (sal * 10/100)
print('Quem ganhava: R${:.2f} teve uma aumento para: R${:.2f}'.format(sal,novo))

