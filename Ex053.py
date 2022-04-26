print('')
print('==============================================')

#for c in range frase:
frase = str(input('Escreva uma frase palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo !')
