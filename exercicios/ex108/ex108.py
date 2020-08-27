# Formatando Moedas em Python (parte 1)

import moeda

num = float(input('Digite um valor monetário: R$'))

print('')
print('=-=' * 15)
print(f'O DOBRO de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A METADE de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}\n')
print(f'{moeda.moeda(num)} com 10% de AUMENTO é {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'{moeda.moeda(num)} com 10% de DESCONTO é {moeda.moeda(moeda.diminuir(num, 10))}')
print('=-=' * 15)
