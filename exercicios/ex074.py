# Maior e Menor Valores em Tupla
from random import randint, shuffle

while True:
    # Utiliza-se (num,) para adicionar valores a uma tupla
    # Achar o maior valor com o método max()
    # Achar o menor valor com p método min()
    ma = me = 0
    tupla = () 
    for c in range(0, 5):
        ale = randint(1, 10)
        if ale > ma:
            ma = ale
        if ale < me or me == 0:
            me = ale
        tupla += (ale,)

    for num in range(0, len(tupla)):
        if num == len(tupla) - 1:
            s = ''
        else:
            s = ', '
        print(tupla[num], end=f'{s}')
    print(f'\n\nMaior número: {ma}')
    print(f'Menor número: {me}\n')
    while True:
        choice = str(input('Deseja sortear mais 5 números? [S/N]: ')).strip().lower()[0]
        print('')
        if choice in 'sn':
            break
        else:
            print('Dado inválido, tente novamente.\n')
    if choice == 'n':
        print('Programa encerrado com sucesso.\n')
        break
