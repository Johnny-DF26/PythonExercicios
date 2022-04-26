print('')
print('====================\033[36mPESO IMC\033[m========================')

alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt ** 2)
print(f'Seu IMC é: {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Peso ideal')
elif 25 < imc < 30:
    print('Sobrepeso')
elif 30 < imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
