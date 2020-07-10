# Mais sobre Matriz em Python
import time
import os

while True:
    matriz = []
    par = 0
    linhas = int(input('Digite o número de linhas: '))
    colunas = int(input('Digite o número de colunas: '))
    print('')

    for i in range(0, linhas):
        for j in range(0, colunas):
            num = int(input(f'Digite o número da posição [{i}, {j}]: '))
            matriz.append(num)
            if num % 2 == 0:
                par += num

    print('')
    cont = cont2 = cont3 = 1
    soma3 = ma = me = 0
    for n in matriz:
        print(f'[ {n:^5} ]', end=' ')
        if cont3 == 3:
            soma3 += n
            cont3 = 0
        if cont2 == 2:
            if cont == 1:
                ma = me = n
            elif n > ma:
                ma = n
            elif n < me:
                me = n
        if cont == colunas:
            print('\n')
            cont2 += 1
            cont = 0
        cont += 1
        cont3 += 1

    print('')
    print('=-=' * 13)
    print(f'Soma de todos os pares: {par}')
    print(f'Soma dos valores da 3ª coluna: {soma3}\n')
    print(f'O maior valor da segunda linha: {ma}')
    print(f'O menor valor da segunda linha: {me}')
    print('=-=' * 13)

    print('')
    while True:
        question = str(input('Deseja reiniciar o programa? [S/N]: ')).strip().lower()[0]
        if question in 'sn':
            break
        else:
            print('\nDado inválido, tente novamente!\n')
    if question == 's':
        print('\nReiniciando...')
        time.sleep(1.5)
        os.system('clear')
    elif question == 'n':
        print('\nPrograma encerrado com sucesso!\n')
        break
