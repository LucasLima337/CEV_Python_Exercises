# Formatando Moedas em Python (parte 2)

import moeda

num = float(input('Digite um valor monetário: R$'))

print('')
print('=-=' * 15)
print(f'O DOBRO de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A METADE de {moeda.moeda(num)} é {moeda.metade(num, True)}\n')
print(f'{moeda.moeda(num)} com 10% de AUMENTO é {moeda.aumentar(num, 10, True)}')
print(f'{moeda.moeda(num)} com 13% de DESCONTO é {moeda.diminuir(num, 13, True)}')
print('=-=' * 15)
