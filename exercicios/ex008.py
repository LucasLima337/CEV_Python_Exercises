# Conversor de Medidas
m = float(input('Digite um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('=*= DADOS =*=')
print('{} metros tem:'.format(m))
print('Quilômetros: {} Km \nHectômetros: {} Hm'.format(km, hm))
print('Decâmetro: {} Dam \nDecímetro: {} Dm'.format(dam, dm))
print('Centímetro: {:.0f} cm \nMilímetro: {:.0f} mm'.format(cm, mm))
