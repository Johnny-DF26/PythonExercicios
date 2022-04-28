from time import sleep
print('')
print('===============\033[33mSOMA DE VALORES\033[m====================')
maior = 0
opcao = ''


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
while opcao != 5:
    print('[1] - Somar\n'
          '[2] - Multiplicar\n'
          '[3] - Maior\n'
          '[4] - novos numeros\n'
          '[5] - sair do programa')
    print('==============================================')
    opcao = int(input('Qual opção voce deseja: '))
    if opcao == 1:
        print(f'A soma entre {n1}+{n2}: \033[34m{n1 + n2}\033[m')
    elif opcao == 2:
        print(f'O valor da multiplicação entre {n1}x{n2}: \033[34m{n1 * n2}\033[m')
    elif opcao == 3:
        if n1 > n2:
            print(f''
                  f'O maior valor entre {n1} e {n2}, então o maior é \033[34m{n1}\033[m')
        elif n1 == n2:
            print('Nenhum dos numeros é maior, \033[31meles são iguais\033[m')
        else:
            print(f'O maior valor entre {n1} e {n2}, entao o maior é \033[34m{n2}\033[m')
    elif opcao == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opcao == 5:
        print('\033[33mAte a Proxima\033[m')
    else:
        print('Opcão Inválida')
    sleep(2)
    print('==============================================')



'''

opcao = 0
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
while opcao != 5:
    print('=-='*20)
    print('[1] somar\n'
          '[2] multiplicar\n'
          '[3] maior\n'
          '[4] novos números\n'
          '[5] sair do programa')
    opcao = int(input('Digite a opcão: '))
    print('=-='*20)
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma é: {soma}')
    elif opcao == 2:
        mult = valor1 * valor2
        print(f'A multiplicação pe: {mult}')
    if opcao == 3:
        if valor1 > valor2:
            maior = valor1
            print(f'O maior valor entre {valor1} e {valor2} o maior é: {maior}')
        else:
            maior = valor2
            print(f'O maior valor entre {valor1} e {valor2} o maior é: {maior}')
    elif opcao == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))
if opcao == 5:
    print('Até Logo ...')
'''