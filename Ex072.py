from time import sleep
print('=='*20)
contagem = ('zero','um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze',
            'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:
    num = int(input('Digite um numero de 0 a 20: '))
    if 0 <= num <= 20:
        print(f'Voce digitou o número {contagem[num]}')
    resp = str(input(f'Quer digitar novamente? [S/N]: ')).upper().strip()
    if resp != 'S':
        break
sleep(0.5)
print('Ate logo ...')
