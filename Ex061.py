
print('=================PROGRESSÃO ARITMÉTICA===================')
a1 = int(input('Digite o primeiro termo da PA: '))
# a1 vai receber um numero inteiro que o usuário irá digitar na tela. Ex: 5
r = int(input('Digite a razão da PA: '))
# r vai receber um numero inteiro que o usuário irá digitar na tela. Ex: 5
termo = a1
# 5   = a1
cont = 1
# cont recebe 1 como parametro inicial para fazer a contagem do while.

while cont <= 10:
    # while é uma condição para verififcar se cont é menor ou igual a 10.
    print(f'{termo} ->',end=' ')
    # escrever na tela o termo = 5, e vai continuar na mesma linha = end.
    termo = termo + r
    # o termo vai receber = 5 e vai somar o 5 mais a razao que é = 5.
    cont = cont + 1
    # a contagem vai deixar de ser 1 e vai somar + 1.
print('FIM')




