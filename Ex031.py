
print('')
print('----=================================================----')

dist = float(input('Qual a distancia voce deseja percorrer em KM: '))
print('---------------------------------------------------------')

if dist <= 200:
    print('Nessa distancia será cobrado R$:0,50 por Km')
    print('O valor da distancia de{:.2f}km será R$:{:.2f}'.format(dist,dist * 0.5))
else:
    print('Nessa distancia será cobrado R$:0,45 por Km ')
    print('O valor da distancia de {:.2f}Km será R$:{:.2f}'.format(dist,dist *0.45))
print('---------------------------------------------------------')