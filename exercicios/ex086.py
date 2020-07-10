# Matriz em Python
import time
import os

matriz = []

while True:
    linha = int(input('Quantas linhas você deseja? '))
    coluna = int(input('Quantas colunas você deseja? '))

    print('')

    for i in range(0, linha):
        for j in range(0, coluna):
            num = int(input(f'Digite um número na posição [{i},{j}]: '))
            matriz.append(num)

    print('')

    cont = 1
    for num in matriz:
        print(f'[ {num:^8} ]', end=' ')
        if cont == coluna:
            print('\n')
            cont = 0
        cont += 1

    while True:
        question = str(input('Deseja reiniciar o programa? [S/N]: ')).strip().lower()[0]
        if question in 'sn':
            break
        else:
            print('\nDado inválido, tente novamente!\n')
    if question == 's':
        matriz.clear()
        print('\nReiniciando...')
        time.sleep(1.5)
        os.system('clear')
    else:
        print('\nPrograma encerrado com sucesso!\n')
        break
