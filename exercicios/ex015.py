# Aluguel de Carros
print('*-- FERRO VELHO DO CEV --*')
km = int(input('Digite a quantidade de km rodados: '))
d = int(input('Digite a quantidade dias que foi alugado: '))
p = (km * 0.15) + (d * 60)
print('Calculando o preço...')
print('O total a pagar será de R${:.2f}'.format(p))
