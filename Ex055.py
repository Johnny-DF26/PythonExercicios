
print('')
print('-----------------PESOS E MEDIDAS--------------------')
maiorPeso = 0
menorPeso = 0
for p in range(1, 7):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        pesoMaior = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print(f'O maior peso lido foi {maiorPeso}')
print(f'O menor peso lido foi {menorPeso}')
