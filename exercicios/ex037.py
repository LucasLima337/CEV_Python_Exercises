# Conversor de Bases Numéricas
from time import sleep
num = int(input('\033[1;30mDigite um número inteiro:\033[m '))
print('\033[1;36m1 - Binário \n2 - Octal \n3 - Hexadecimal\033[m')
c = int(input('\033[1;30mDigite 1, 2 ou 3 para escolher a base de conversão:\033[m '))
print('')
sleep(1.75)
print('\033[1;30mANALISANDO...\033[m')
sleep(2)
print('')
if c == 1:
    fri = 'BINÁRIO'
    print(f'\033[1;33m{fri:-^45}')
    print(f'Número Escolhido: {num}')
    print(f'Número Convertido: {num:b}')
    #bin(num)[2:] --> Fatiamento
    print('-' * 45)
elif c == 2:
    fri = 'OCTAL'
    print(f'\033[1;32m{fri:-^45}')
    print(f'Número Escolhido: {num}')
    print(f'Número Convertido: {num:o}')
    #oct(num)[2:] --> Fatiamento
    print('-' * 45)
elif c == 3:
    fri = 'HEXADECIMAL'
    print(f'\033[1;35m{fri:-^45}')
    print(f'Número Escolhido: {num}')
    print(f'Número Convertido: {num:x}')
    #hex(num)[2:] --> Fatiamento
    print('-' * 45)
elif c != 1 or c != 2 or c != 3:
    print('\033[1;31m-' * 45)
    fri = 'VALOR INVÁLIDO, TENTE NOVAMENTE.'
    print(f'{fri:^45}')
    print('-' * 45)
