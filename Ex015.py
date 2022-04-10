print('')
print('|------------------ALUGUEL DE CARROS-------------------|')
dias = int(input('Quantos dias voce utilizou o carro: '))
km = float(input('Quantos Km voce rodou o veiculo: '))

precodias = 60 * dias
kmrodado  = 0.15 * km
Totvalor = kmrodado + precodias

print('O preço por dia ficou em R$:{:.2f}'.format(precodias))
print('O preco em km rodado ficou em R$:{:.2f}'.format(kmrodado))
print('O preço total é de R$:{:.2f}'.format(Totvalor))
print('|------------------------------------------------------|')