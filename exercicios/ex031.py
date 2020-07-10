# Custo da Viagem
from time import sleep
i = str(input('De qual estado você vai sair? ')).strip().title()
f = str(input('Para qual estado você vai? ')).strip().title()
d = int(input('Digite a distância da viagem em km: '))
print('')
fri = 'Viagem pelo Brasil'
print('CALCULANDO...')
print('')
sleep(2)
print(f'{fri:-^45}')
print(f'Origem: {i}')
print(f'Destino: {f}')
print(f'Distância em km: {d}km')
if 0 != d <= 200:
    p = 0.5 * d
    print(f'Total a Pagar: R${p:.2f}')
    print('-' * 45)
if d > 200:
    p = 0.45 * d
    print(f'Total a Pagar: R${p:.2f}')
    print('-' * 45)
if d == 0:
    print('Valor inválido!!')
    print('-' * 45)
