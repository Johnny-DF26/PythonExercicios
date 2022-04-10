Comp = float(input('Qual o comprimento da parede: '))
Alt = float(input('Qual a altura da parede: '))

area = Comp * Alt
TotPint = area / 2
print('A area da parede é:{:.2f}m²'.format(area))
print('São necessário {} litros de tinta para pintar {}m²'.format(TotPint,area))