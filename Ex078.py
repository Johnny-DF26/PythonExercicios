valores = list()
maior = menor = posicaoMaior = posicaoMenor = 0

for c in range(0,5):
    valores.append(int(input(f'Digite um valor {c}ª: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'{valores}')
for i,v in enumerate(valores):
    if v == maior:
        print(f'O maior valor foi: {maior} e esta na posição: {i}')
for i,v in enumerate(valores):
    if v == menor:
        print(f'O menor valor foi: {menor} e esta na posição: {i}')




