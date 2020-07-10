# Listas com pares e ímpares
import time
import os

numeros = [[], []]
while True:
    for n in range(1, 8):
        num = int(input(f'Digite o {n}º número: '))
        if num % 2 == 0:
            numeros[0].append(num)
        else:
            numeros[1].append(num)

    numeros[0].sort()
    numeros[1].sort()

    print('=-=' * 10)
    print(f'Pares: {numeros[0]}')
    print(f'Ímpares: {numeros[1]}')
    print('=-=' * 10)

    while True:
        question = str(input('Deseja reiniciar o programa? [S/N]: ')).strip().lower()[0]
        if question in 'sn':
            break
        else:
            print('\nDado inválido, tente novamente!\n')
    if question == 's':
        print('\nReiniciando...')
        numeros[0].clear()
        numeros[1].clear()
        time.sleep(1.5)
        os.system('clear')
    elif question == 'n':
        print('\nPrograma encerrado com sucesso!\n')
        break
