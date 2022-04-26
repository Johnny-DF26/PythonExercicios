
print('-=-' * 20)
num = int(input('Digite um numero: '))
print('Digite qual numero deseja converter:')
opcao = int(input('1- para \033[33mBinário\033[m\n'
                '2- para \033[34mOctal\033[m\n'
                '3- para \033[31mHexadecimal\033[m\n'
                'Sua Opção: '))

if opcao == 1:
    print(f'Em binario o numero é: {bin(num)[2:]}')
elif opcao == 2:
    print(f'Em octal o numero é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'Em hexadecimal o numero é: {hex(num)[2:]}')
else:
    print('Opcao invalida')
