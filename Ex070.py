print('')
print('======================SUPER CAIXA ELETRO==========================')
tot = menor = cont = qtdprodMaior = 0
maisBarato = ''
while True:
    prod = str(input("Qual o nome do produto: "))
    preco = float(input("Qual o preço do produto: "))
    tot += preco
    cont += 1
    if preco > 1000:
        qtdprodMaior += 1
    if cont == 1 or preco < menor:
        menor = preco
        maisBarato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer Continuar [S/N]? ")).strip().upper()
    if resp == 'N':
        break
print('==='*20)
print(f'Total gasto foi de R$: {tot:.2f}')
print(f'{qtdprodMaior} produtos custam mais de R$1000,00')
print(f'O produto mais barato é a {maisBarato} no valor de R$:{menor:.2f}')
print('==='*20)
