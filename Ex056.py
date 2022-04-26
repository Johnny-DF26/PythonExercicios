print('')
print('====================CONSULTA NOMES========================')
print('')
totIdade = 0
maiorIdade = 0
maiorNome = ''
totmulher = 0
for p in range(1,5):
    print(f'========= {p} ªPESSOA ===========')
    nome = str(input(f'nome: ')).strip().upper()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo[F/M]: ')).upper().strip()
    totIdade += idade
    if sexo == 'M':
        if idade > maiorIdade:
            maiorIdade = idade
            maiorNome = nome
    if sexo == 'F' and idade < 20:
        totmulher += 1
mediaIdade = totIdade / 4
print(f'A média de idade do grupo é: {mediaIdade:.1f} anos')
print(f'O homem mais velho é {maiorNome} com {maiorIdade} anos')
print(f'Existem {totmulher} mulheres com menos de 20 anos')
