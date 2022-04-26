from time import sleep
print('')
print('-----------------------------------------')

num = float(input('Qual o preço do produto: '))
#pag = str(input('Qual a Condição de pagamento: ')).upper().strip()
pag = int(input('1 - A vista\n'
                '2 - A vista no Cartão\n'
                '3 - Cartão em 2x\n'
                '4 - Cartão em 3x ou mais\n'
                'Qual a Condição de pagamento: '))

if pag == 1:
    total = num - (10 / 100 * num)
    print(f'À vista esse valor tem \033[33m10% de DESCONTO\033[m, o valor fica R$:{total:.2f}')
elif pag == 2:
    total = num - (5 / 100 * num)
    print(f'No cartão a vista  tem \033[33m5% de DESCONTO\033[m, o valor fica R$:{total:.2f}')
elif pag == 3:
    total = num
    parcela = num / 2
    print(f'Sua compra será parcelada e 2x de {parcela:.2f} SEM JUROS')
    print(f'No cartão preço fica R$:{num:.2f}')
elif pag == 4:
    total = num + (20 / 100 * num)
    totParcelas = int(input('Quantas parcelas: '))
    parcela = total / totParcelas
    print(f'Sua compra será parcelada em {totParcelas}x de {parcela:.2f} COM JUROS')
    print(f'No cartão sua compra com \033[31mjuros de 20%\033[m, o valor fica R$:{total:.2f}')
else:
    total = 0
    print('OPCAO INVÁLIDA')


