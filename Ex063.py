print('')
print('================SEQUENCIA FIBONACCI=====================')

n = int(input('Digite um numero: '))
# n recebe um numero inteiro
a1 = 0
# a1 recebe 0
a2 = 1
# a2 recebe 1
a3 = 0
# a3 recebe 0
cont = 3
# cont recebe 3
print(f'{a1} - {a2}',end=' - ')
# escreve na tela a1 e a2, na mesma linha
while cont <= n:
    # enquanto cont que é 3 for menor ou igual a n
    a3 = a1 + a2
    # a3 recebe a1 + a2
    print(f'{a3}',end=' - ')
    # escreve na tela a3 que é a1 + a2
    a1 = a2
    # a1 agora recebe a2
    a2 = a3
    # a2 agora recebe a3
    cont += 1
    # cont recebe + 1
print('FIM')
# escreve na tela a frase
