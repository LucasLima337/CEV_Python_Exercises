# Valores únicos em uma Lista
from time import sleep

lista = []
pos = 1
x = ''
while True:
    while True:
        num = int(input(f'\nDigite o {pos}º número: '))
        if num in lista:
            print('\nEsse número já foi adicionado, tente novamente.')
        else:
            lista.append(num)
            pos += 1
            break
    while True:
        question = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
        if question in 'sn':
            break
        else:
            print('\nDado inválido, tente novamente.\n')
    if question == 'n':
        print('')
        lista.sort()
        print('=-=' * 10)
        print('Lista:', end=' ')
        for i, numeros in enumerate(lista):
            if i == len(lista) - 1:
                x = '.'
            elif i == len(lista) - 2:
                x = ' e '
            else:
                x = ', '
            print(numeros, end=f'{x}')
        print('')
        print('=-=' * 10)
        while True:
            question2 = str(input('Deseja reiniciar o programa? [S/N]: ')).strip().lower()[0]
            if question2 in 'sn':
                break
            else:
                print('\nDado inválido, tente novamente.\n')
        if question2 == 'n':
            print('\nPrograma encerrado com sucesso!\n')
            break
        else:
            print('\nReiniciando...\n')
            lista = []
            pos = 1
            sleep(2)
