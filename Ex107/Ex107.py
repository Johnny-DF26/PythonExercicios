import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p:.2f} é: {moeda.metade(p)}')
print(f'O dobro de {p:.2f} é: {moeda.dobro(p)}')
print(f'Aumento de 10%, temos {moeda.aumento(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
