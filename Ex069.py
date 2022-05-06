print('')
qtdHomens = qtdMulheres = pessoasMaior = 0
while True:
    print('--------------------CADASTRE UMA PESSOA----------------------------')
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: ')).upper().strip()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar[S/N]: ')).upper().strip()[0]
    if idade >= 18:
        pessoasMaior += 1
    if sexo == 'M':
        qtdHomens += 1
    if sexo == 'F' and idade < 20:
        qtdMulheres += 1
    if resp == 'N':
        break
print('---------------------------------------------------------------------')
print(f'Pessoas maiores de idade: {pessoasMaior}')
print(f'Quantidade de Homens é: {qtdHomens}')
print(f'Quantidade de mulhers com menos de 20 anos: {qtdMulheres}')
print('---------------------------------------------------------------------')
