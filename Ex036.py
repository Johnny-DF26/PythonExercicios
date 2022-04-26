print('')
print('-----------------------EMPRESTIMO----------------------------')
casa = float(input('Qual o valor da casa para financiamento R$: '))
sal = float(input('Qual o seu salário R$: '))
tempo = int(input('Em quanto tempo em anos deseja financiar: '))

valorPrest = casa / (tempo * 12)
print(f'O valor da prestação é R$:{valorPrest:.2f}')
if valorPrest < 30/100 * sal:
    print('O seu emprestimo foi \033[36m APROVADO\033[m !!')
elif valorPrest > 30/100 * sal:
    print('O seu emprestimo foi \033[31mNEGADO\033[m !!')

print('-------------------------------------------------------------')