# Pintando Parede
larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
a = larg * alt
tinta = a / 2
print('Para pintar uma área de {:.2f}m²'.format(a), end=' ')
print('será necessário {:.2f} litros de tinta'.format(tinta))
