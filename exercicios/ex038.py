# Comparando números
from time import sleep
a = int(input('\33[1;30mDigite um número: '))
b = int(input('Digite outro número: '))
print('')
sleep(1.75)
print('ANALISANDO...')
sleep(2)
print('')
print('=-=' * 15)
if a > b:
    print(f'\033[1;36mNúmeros Escolhidos: {a} e {b}')
    print('O PRIMEIRO número é maior.')
    print(f'Número Maior: {a}\033[m')
elif b > a:
    print(f'\033[1;35mNúmeros Escolhidos: {a} e {b}')
    print('O SEGUNDO número é maior.')
    print(f'Número Maior: {b}\033[m')
else:
    print(f'\033[1;33mNúmeros Escolhidos: {a} e {b}')
    print('Esses dois números são iguais.\033[m')
print('\033[1;30m=-=\033[m' * 15)
