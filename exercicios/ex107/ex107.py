# Exercitando módulos em Python

import moeda

num = float(input('Digite um valor monetário: R$'))

print('')
print('=-=' * 15)
print(f'O DOBRO de R${num} é R${moeda.dobro(num)}')
print(f'A METADE de R${num} é R${moeda.metade(num)}\n')
print(f'R${num} com 15% de AUMENTO é R${moeda.aumentar(num, 15)}')
print(f'R${num} com 15% de DESCONTO é R${moeda.diminuir(num, 15)}')
print('=-=' * 15)
