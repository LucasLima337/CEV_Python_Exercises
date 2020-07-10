# Conversor de Moedas
print('=*=' * 20)
print('COTAÇÃO ANTIGA // DÓLAR')
print('== SUA CARTEIRA ==')
c = float(input('Quanto de dinheiro você tem na carteira? R$'))
conv = c / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(c, conv))
print('=*=' * 20)
print('COTAÇÃO NOVA // DÓLAR')
print('== SUA CARTEIRA ==')
r = float(input('Quanto de dinheiro você tem na carteira? R$'))
conv2 = r / 3.90
print('Com R${:.2f} você pode comprar US${:.2f}'.format(r, conv2))
print('=*=' * 20)
print('COTAÇÃO NOVA // EURO')
print('== SUA CARTEIRA ==')
real = float(input('Quanto de dinheiro você tem na carteira? R$'))
conv3 = real / 4.41
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, conv3))
print('=*=' * 20)
